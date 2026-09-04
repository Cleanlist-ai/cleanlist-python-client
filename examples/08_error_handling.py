"""Catching typed API exceptions. Free.

Every non-2xx response raises a subclass of ``ApiException`` carrying the HTTP
status, reason, and (parsed) body.

    python examples/08_error_handling.py
"""
from _common import client

from cleanlist_ai import ApiException
from cleanlist_ai.exceptions import (
    NotFoundException,
    UnauthorizedException,
    UnprocessableEntityException,
)


def main() -> None:
    with client() as cl:
        # 1. A 404 — asking for a list that doesn't exist.
        try:
            cl.lead_lists.get_list("00000000-0000-0000-0000-000000000000")
        except NotFoundException:
            print("[404] no such list — handled")
        except UnauthorizedException:
            print("[401] bad or missing API key — check CLEANLIST_API_KEY")

        # 2. A 422 — invalid request body (empty list name).
        from cleanlist_ai.models import CreateListRequest

        try:
            # Pydantic validates most shape errors *before* the request is sent;
            # server-side validation surfaces as UnprocessableEntityException.
            cl.lead_lists.create_list(CreateListRequest.model_construct(name=""))
        except UnprocessableEntityException as e:
            print(f"[422] validation failed: {e.data}")
        except ApiException as e:
            print(f"[{e.status}] {e.reason}: {e.body}")


if __name__ == "__main__":
    main()
