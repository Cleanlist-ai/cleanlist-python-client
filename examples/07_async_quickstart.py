"""The async client end to end — concurrent calls with asyncio. Mostly free.

Uses ``cleanlist_ai.aio`` and awaits every call. Note how ``asyncio.gather`` fires
independent requests concurrently over one shared connection.

    python examples/07_async_quickstart.py
"""
import asyncio

from _common import aclient

from cleanlist_ai.aio.models import CreateListRequest


async def main() -> None:
    async with aclient() as cl:
        # Fire three independent reads concurrently.
        me, balance, lists = await asyncio.gather(
            cl.workspace.whoami(),
            cl.workspace.credits_balance(),
            cl.lead_lists.list_lists(limit=5),
        )
        print(f"Org: {me.organization_name} | credits: {balance.credits}")
        print(f"Recent lists: {[s.name for s in lists.lists]}")

        # Writes work the same way, just awaited.
        lst = await cl.lead_lists.create_list(CreateListRequest(name="SDK — async demo"))
        print(f"Created list: {lst.list_id}")


if __name__ == "__main__":
    asyncio.run(main())
