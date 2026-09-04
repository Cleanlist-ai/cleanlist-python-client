"""Enrich a single person and poll the workflow to completion.

⚠️ Spends credits (partial scope = 1 credit if data is found; pay-for-results).

    python examples/02_enrich_person.py
"""
import time

from _common import client

from cleanlist_ai.models import CreateListRequest, EnrichPersonRequest

TERMINAL = {"completed", "failed", "cancelled"}


def main() -> None:
    with client() as cl:
        lst = cl.lead_lists.create_list(CreateListRequest(name="SDK — enrich person"))

        # Provide whatever you know: email, linkedin_url, or name + company/domain.
        job = cl.enrichment.enrich_person(
            EnrichPersonRequest(
                lead_list_id=lst.list_id,
                first_name="Ada",
                last_name="Lovelace",
                company_name="Analytical Engines",
                # include_phone=True,  # -> phone_only scope (10 credits)
            )
        )
        print(f"Dispatched workflow {job.workflow_id} (reserved {job.credits_reserved} credits)")

        # Poll until the async workflow settles.
        while True:
            status = cl.enrichment.enrichment_status(job.workflow_id)
            print(f"  status={status.status} processed={status.processed}/{status.total}")
            if status.status in TERMINAL:
                break
            time.sleep(3)

        print(f"Done: charged={status.credits_charged} refunded={status.credits_refunded}")
        if status.result is not None:
            print("Result:", status.result)


if __name__ == "__main__":
    main()
