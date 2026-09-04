"""Shared helpers for the example scripts.

Reads the API key from ``CLEANLIST_API_KEY`` and an optional base URL from
``CLEANLIST_HOST`` (handy for pointing at a local backend). Import and call
``client()`` / ``aclient()`` to get a ready-to-use SDK instance.
"""
from __future__ import annotations

import os
import sys


def _require_key() -> str:
    key = os.getenv("CLEANLIST_API_KEY")
    if not key:
        sys.exit("Set CLEANLIST_API_KEY first (app.cleanlist.ai → Settings → API Keys).")
    return key


def client():
    """A ready-to-use synchronous Cleanlist client."""
    from cleanlist_ai import Cleanlist

    host = os.getenv("CLEANLIST_HOST", "https://api.cleanlist.ai")
    return Cleanlist(access_token=_require_key(), host=host)


def aclient():
    """A ready-to-use asynchronous Cleanlist client."""
    from cleanlist_ai.aio import Cleanlist

    host = os.getenv("CLEANLIST_HOST", "https://api.cleanlist.ai")
    return Cleanlist(access_token=_require_key(), host=host)
