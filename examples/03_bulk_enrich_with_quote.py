"""The estimate -> quote -> bulk-enrich credit flow.

Bulk operations must be pre-priced: you call ``credits_estimate`` to get a signed,
single-use ``quote_id`` and pass it to ``enrich_list``. The quote caps the spend.

⚠️ Spends credits for every lead in the list. This script stops before dispatch if
the balance is insufficient, and prints the cost so you can confirm.

    python examples/03_bulk_enrich_with_quote.py <list_id>
"""
import sys
import time

from _common import client

from cleanlist_ai.models import EstimateCostRequest, EnrichListRequest

TERMINAL = {"completed", "failed", "cancelled"}
SCOPE = "full"  # partial | phone_only | full


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python examples/03_bulk_enrich_with_quote.py <list_id>")
    list_id = sys.argv[1]

    with client() as cl:
        # 1. Price it — bound to this list + scope + current lead count.
        quote = cl.workspace.credits_estimate(
            EstimateCostRequest(tool="enrich_list", list_id=list_id, scope=SCOPE)
        )
        print(
            f"Estimate: {quote.estimated_cost} credits for {quote.row_count} leads "
            f"(you have {quote.available_credits}, sufficient={quote.sufficient})"
        )
        if not quote.sufficient:
            sys.exit("Not enough credits — top up at app.cleanlist.ai/billing.")

        # 2. Redeem the quote to dispatch the bulk workflow.
        run = cl.enrichment.enrich_list(
            EnrichListRequest(list_id=list_id, scope=SCOPE, quote_id=quote.quote_id)
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
