"""Full lead-list lifecycle — create, read, update, paginate, delete. Free.

    python examples/04_lead_lists_crud.py
"""
from _common import client

from cleanlist_ai.models import CreateListRequest, PublicLeadListUpdate


def iter_all_leads(cl, list_id, page_size=500):
    """Yield every lead in a list, transparently following the cursor."""
    cursor = None
    while True:
        page = cl.lead_lists.list_leads_in_list(list_id, limit=page_size, cursor=cursor)
        yield from page.leads
        cursor = page.cursor
        if not cursor:
            break


def main() -> None:
    with client() as cl:
        # Create (idempotent on name).
        lst = cl.lead_lists.create_list(
            CreateListRequest(name="SDK — CRUD demo", description="created by the SDK example")
        )
        print(f"Created {lst.list_id} (reused={lst.reused})")

        # Read one.
        detail = cl.lead_lists.get_list(lst.list_id)
        print(f"Name={detail.name} leads={detail.lead_count} enriched={detail.enriched_count}")

        # Update (rename / edit description / move folder).
        cl.lead_lists.update_list(
            lst.list_id, PublicLeadListUpdate(description="updated by the SDK example")
        )
        print("Updated description.")

        # Paginate all leads (helper above).
        total = sum(1 for _ in iter_all_leads(cl, lst.list_id))
        print(f"Walked {total} leads across all pages.")

        # Clean up.
        cl.lead_lists.delete_list(lst.list_id)
        print("Deleted list.")


if __name__ == "__main__":
    main()
