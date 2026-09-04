"""Quickstart — the 60-second tour. Free (no credits spent).

    python examples/01_quickstart.py
"""
from _common import client

from cleanlist_ai.models import CreateListRequest


def main() -> None:
    with client() as cl:
        # Who am I? — identity, org, plan tier, granted scopes.
        me = cl.workspace.whoami()
        print(f"Authenticated as org '{me.organization_name}' (tier: {me.tier})")
        print(f"Scopes: {', '.join(me.scopes)}")

        # How many credits does the org have?
        balance = cl.workspace.credits_balance()
        print(f"Credit balance: {balance.credits}")

        # Create a lead list (idempotent on name — safe to re-run).
        lst = cl.lead_lists.create_list(CreateListRequest(name="SDK quickstart"))
        print(f"List ready: {lst.list_id}")

        # List your most recent lead lists.
        page = cl.lead_lists.list_lists(limit=5)
        print("Recent lists:")
        for summary in page.lists:
            print(f"  - {summary.name} ({summary.lead_count} leads)")


if __name__ == "__main__":
    main()
