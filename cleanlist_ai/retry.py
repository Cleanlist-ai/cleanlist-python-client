# coding: utf-8
"""Retries, idempotency keys and response metadata for the Cleanlist API.

Hand-authored (not generated) and re-applied on every regeneration by
``scripts/generate.sh``. The sync and async ``Cleanlist`` clients both use it.
"""
from __future__ import annotations

import email.utils
import random
import time
import uuid
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


def can_retry(method: str, headers: Optional[Mapping[str, Any]]) -> bool:
    """Reads always; a write only when it carries an ``Idempotency-Key``, so a retry can't run it twice."""
    return method.upper() not in WRITE_METHODS or bool(_header(headers, IDEMPOTENCY_HEADER))


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
        delay = min(8.0, 0.5 * 2 ** (attempt - 1)) + random.uniform(0, 0.25)
    if delay > MAX_RETRY_DELAY:
        return None
    return delay
