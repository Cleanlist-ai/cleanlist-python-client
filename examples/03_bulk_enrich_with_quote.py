"""The quote -> bulk-enrich credit flow.

Bulk operations must be pre-priced: ``enrich_list`` requires a signed, single-use
``quote_id`` (bound to the list + scope + lead count). The quote caps the spend.
The pricing endpoint (``POST /api/v2/credits/estimate``) is no longer part of the
public API spec, so this SDK cannot request a quote — pass one you already have.

⚠️ Spends credits for every lead in the list.

    python examples/03_bulk_enrich_with_quote.py <list_id> <quote_id>
"""
import sys
import time

from _common import client

from cleanlist_ai.models import EnrichListRequest

TERMINAL = {"completed", "failed", "cancelled"}
SCOPE = "full"  # partial | phone_only | full


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("Usage: python examples/03_bulk_enrich_with_quote.py <list_id> <quote_id>")
    list_id, quote_id = sys.argv[1], sys.argv[2]

    with client() as cl:
        # 1. Show the balance before spending.
        balance = cl.workspace.credits_balance()
        print(f"Balance: {balance}")

        # 2. Redeem the quote to dispatch the bulk workflow.
        run = cl.enrichment.enrich_list(
            EnrichListRequest(list_id=list_id, scope=SCOPE, quote_id=quote_id)
        )
        print(f"Bulk workflow dispatched: {run.workflow_id}")

        # 3. Poll progress.
        while True:
            status = cl.enrichment.enrichment_status(run.workflow_id)
            print(f"  {status.status}: {status.processed}/{status.total} "
                  f"(ok={status.completed} failed={status.failed})")
            if status.status in TERMINAL:
                break
            time.sleep(5)

        print(f"Finished: charged={status.credits_charged} refunded={status.credits_refunded}")


if __name__ == "__main__":
    main()
