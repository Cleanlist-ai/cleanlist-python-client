# coding: utf-8
"""Retries, idempotency keys and response metadata for the Cleanlist API.

Hand-authored (not generated) and re-applied on every regeneration by
``scripts/generate.sh``. The sync and async ``Cleanlist`` clients both use it.
"""
from __future__ import annotations

import email.utils
import json
import random
import re
import time
import uuid
from urllib.parse import urlsplit
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

#: Total tries per request, the first one included.
DEFAULT_MAX_ATTEMPTS = 3

#: A ``Retry-After`` longer than this (seconds) is returned to the caller
#: instead of waited out.
MAX_RETRY_DELAY = 60.0

#: Methods that get an automatic ``Idempotency-Key``.
WRITE_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})

IDEMPOTENCY_HEADER = "Idempotency-Key"

#: Single-use writes that are never retried: a second try after a lost
#: response can't be told apart from a repeat.
_NEVER_RETRY_PATH = re.compile(r"/api/v2/(actions/confirm|inbox/threads/[^/]+/reply)/?$")


@dataclass(frozen=True)
class RateLimit:
    """``X-RateLimit-*`` of the tightest bucket that applied. ``reset`` is unix seconds."""

    limit: int
    remaining: int
    reset: int


@dataclass(frozen=True)
class ResponseMeta:
    status: int
    #: ``None`` when the response carried no rate-limit headers.
    rate_limit: Optional[RateLimit]
    #: ``"test"`` for a test key's sandbox workspace, from ``Cleanlist-Mode``.
    mode: Optional[str]
    #: True when the server replayed a stored response for a repeated key.
    idempotent_replayed: bool


def _header(headers: Optional[Mapping[str, Any]], name: str) -> Optional[str]:
    if not headers:
        return None
    value = headers.get(name)
    if value is None:
        lowered = name.lower()
        for key, candidate in headers.items():
            if str(key).lower() == lowered:
                value = candidate
                break
    return None if value is None else str(value).strip()


def _int_header(headers: Optional[Mapping[str, Any]], name: str) -> Optional[int]:
    raw = _header(headers, name)
    if not raw:
        return None
    try:
        return int(float(raw))
    except ValueError:
        return None


def read_response_meta(status: int, headers: Optional[Mapping[str, Any]]) -> ResponseMeta:
    """Reads rate-limit, mode and replay headers, e.g. off ``ApiException.headers``."""
    limit = _int_header(headers, "X-RateLimit-Limit")
    remaining = _int_header(headers, "X-RateLimit-Remaining")
    reset = _int_header(headers, "X-RateLimit-Reset")
    mode = (_header(headers, "Cleanlist-Mode") or _header(headers, "X-Cleanlist-Mode") or "").lower()
    return ResponseMeta(
        status=status,
        rate_limit=(
            RateLimit(limit, remaining, reset)
            if limit is not None and remaining is not None and reset is not None
            else None
        ),
        mode=mode if mode in ("live", "test") else None,
        idempotent_replayed=(_header(headers, "Idempotent-Replayed") or "").lower() == "true",
    )


def add_idempotency_key(method: str, headers: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Adds a fresh key to a write unless the caller passed one (``_headers={"Idempotency-Key": ...}``)."""
    headers = dict(headers or {})
    if method.upper() in WRITE_METHODS and _header(headers, IDEMPOTENCY_HEADER) is None:
        headers[IDEMPOTENCY_HEADER] = str(uuid.uuid4())
    return headers


def can_retry(method: str, url: str) -> bool:
    """False for ``POST /api/v2/actions/confirm`` and inbox replies, whatever the outcome."""
    if method.upper() not in WRITE_METHODS:
        return True
    return not _NEVER_RETRY_PATH.search(urlsplit(url).path)


def can_retry_network_error(method: str, headers: Optional[Mapping[str, Any]]) -> bool:
    """No response came back. Reads always; a write only with an ``Idempotency-Key``."""
    return method.upper() not in WRITE_METHODS or bool(_header(headers, IDEMPOTENCY_HEADER))


def _error_code(body: Optional[bytes]) -> Optional[str]:
    try:
        payload = json.loads(body or b"")
    except (TypeError, ValueError):
        return None
    if not isinstance(payload, dict):
        return None
    error = payload.get("error")
    return error.get("code") if isinstance(error, dict) else payload.get("code")


def can_retry_status(method: str, status: int, body: Optional[bytes]) -> bool:
    """Reads retry on 429 and 5xx. Writes retry on 429 and a 503 ``idempotency_unavailable``
    (refused before the route ran); any other 5xx may have run the route, and the server
    doesn't store 5xx under the key, so a retry would run it again."""
    if status == 429:
        return True
    if method.upper() not in WRITE_METHODS:
        return status >= 500
    return status == 503 and _error_code(body) == "idempotency_unavailable"


def _backoff(attempt: int) -> float:
    return min(8.0, 0.5 * 2 ** (attempt - 1)) + random.uniform(0, 0.25)


def network_retry_delay(attempt: int, max_attempts: int) -> Optional[float]:
    """Seconds to wait before try ``attempt + 1`` after a network error, or ``None`` to raise."""
    return None if attempt >= max_attempts else _backoff(attempt)


def _parse_retry_after(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when is None:
        return None
    return max(0.0, when.timestamp() - time.time())


def retry_delay(status: int, retry_after: Optional[str], attempt: int, max_attempts: int) -> Optional[float]:
    """Seconds to wait before try ``attempt + 1``, or ``None`` to stop and return the response."""
    if attempt >= max_attempts or not (status == 429 or status >= 500):
        return None
    delay = _parse_retry_after(retry_after)
    if delay is None:
        delay = _backoff(attempt)
    if delay > MAX_RETRY_DELAY:
        return None
    return delay
