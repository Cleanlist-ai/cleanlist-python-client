#!/usr/bin/env python3
"""Prepare the raw backend v2 OpenAPI export for client generation.

FastAPI emits verbose default operationIds of the form
``<function_name>_api_v2_<path>_<method>`` (e.g. ``whoami_api_v2_whoami_get``).
Fed straight into openapi-generator those become unusable method names.

The clean, human-authored part is always the segment *before* ``_api_v2_``
(the route function name), so we recover a tidy snake_case method name from it.
The result is written to a build-only spec that the generator consumes; the
pristine backend export at ``openapi/cleanse-api-v2.oas.json`` is left untouched.

Usage:
    python scripts/prepare_spec.py <input.json> <output.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


def clean_operation_id(operation_id: str) -> str:
    """`create_list_api_v2_lead_lists_post` -> `create_list`."""
    name = operation_id.split("_api_v2_", 1)[0]
    # A few routes carry an `_endpoint` suffix on the function name; drop it so
    # the method reads naturally (`list_api_keys_endpoint` -> `list_api_keys`).
    if name.endswith("_endpoint"):
        name = name[: -len("_endpoint")]
    return name


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    spec = json.loads(src.read_text())

    seen: dict[str, str] = {}
    for path, item in (spec.get("paths") or {}).items():
        for method, operation in item.items():
            if method.lower() not in _HTTP_METHODS or not isinstance(operation, dict):
                continue
            original = operation.get("operationId")
            if not original:
                continue
            cleaned = clean_operation_id(original)
            if cleaned in seen and seen[cleaned] != original:
                raise SystemExit(
                    f"operationId collision: '{cleaned}' from both "
                    f"'{seen[cleaned]}' and '{original}' ({method.upper()} {path})"
                )
            seen[cleaned] = original
            operation["operationId"] = cleaned

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(spec, indent=2))
    print(f"Prepared spec with {len(seen)} cleaned operationIds -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
