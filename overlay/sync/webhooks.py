# coding: utf-8
"""Verifies the ``Cleanlist-Signature`` header on webhook deliveries.

Hand-authored (not generated) and re-applied on every regeneration by
``scripts/generate.sh``.

The header is ``t=<unix seconds>,v1=<hex HMAC-SHA256 of "<t>.<raw body>">``,
keyed with the secret ``POST /api/v2/webhooks`` returned once::

    from cleanlist_ai import verify_webhook_signature

    ok = verify_webhook_signature(request.body, request.headers.get("Cleanlist-Signature"), secret)
"""
from __future__ import annotations

import hashlib
import hmac
import re
import time
from typing import Optional, Union

SIGNATURE_HEADER = "Cleanlist-Signature"

#: Deliveries signed longer ago than this are refused, so a captured one
#: can't be replayed later.
DEFAULT_TOLERANCE_SECONDS = 300

_HEX_SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


def verify_webhook_signature(
    payload: Union[bytes, str],
    signature_header: Optional[str],
    secret: str,
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: Optional[int] = None,
) -> bool:
    """True when ``signature_header`` is a valid, fresh signature of ``payload``.

    ``payload`` is the raw request body exactly as received; re-serialized JSON
    won't match.
    """
    if not signature_header or not secret:
        return False

    timestamp: Optional[str] = None
    signatures = []
    for part in signature_header.split(","):
        key, sep, value = part.partition("=")
        if not sep:
            continue
        key, value = key.strip(), value.strip()
        if key == "t":
            timestamp = value
        elif key == "v1" and _HEX_SHA256.match(value):
            signatures.append(value.lower())
    if not timestamp or not (timestamp.isascii() and timestamp.isdigit()) or not signatures:
        return False

    current = int(time.time()) if now is None else now
    if abs(current - int(timestamp)) > tolerance_seconds:
        return False

    body = payload.encode("utf-8") if isinstance(payload, str) else bytes(payload)
    expected = hmac.new(secret.encode("utf-8"), timestamp.encode() + b"." + body, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, candidate) for candidate in signatures)
