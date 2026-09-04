"""Run a custom AI smart-agent column over a list and read the per-lead results.

⚠️ Spends credits (priced per processed row). Estimates first and prints the cost.

    python examples/05_smart_agent.py <list_id>
"""
import sys
import time

from _common import client

from cleanlist_ai.models import EstimateCostRequest, RunSmartAgentRequest

MAX_ROWS = 25


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python examples/05_smart_agent.py <list_id>")
    list_id = sys.argv[1]

    with client() as cl:
        # Price the run for the exact request shape.
        quote = cl.workspace.credits_estimate(
            EstimateCostRequest(
                tool="run_smart_agent",
                list_id=list_id,
                agent_type="custom_ai",
                row_count=MAX_ROWS,
            )
        )
        print(f"Cost: {quote.estimated_cost} credits (sufficient={quote.sufficient})")
        if not quote.sufficient:
            sys.exit("Not enough credits.")

        run = cl.smart_agents.run_smart_agent(
            RunSmartAgentRequest(
                list_id=list_id,
                agent_type="custom_ai",
                column_name="Outreach angle",
                prompt="In one sentence, suggest a cold-outreach angle for this lead.",
                lead_scope="subset",
                max_rows=MAX_ROWS,
                quote_id=quote.quote_id,
            )
        )
        print(f"Started smart agent: {run.smart_agent_task_id} (status={run.status})")

        # Poll the run's results endpoint until it finishes.
        while True:
            res = cl.smart_agents.get_smart_agent_results(run.smart_agent_task_id)
            print(f"  {res.status}: ok={res.succeeded} failed={res.failed}/{res.total}")
            if res.status in ("completed", "failed", "cancelled"):
                break
            time.sleep(5)

        for row in (res.results or [])[:10]:
            print(f"  lead={row.lead_id} -> {row.value!r}")


if __name__ == "__main__":
    main()
