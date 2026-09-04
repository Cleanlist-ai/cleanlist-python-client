# Cleanlist SDK — runnable examples

Copy-paste-able scripts that exercise the real v2 API with the `cleanlist-ai` SDK.

## Setup

```bash
pip install cleanlist-ai
export CLEANLIST_API_KEY="clapi_live_..."   # from app.cleanlist.ai → Settings → API Keys
```

Point at a local backend instead of production with:

```bash
export CLEANLIST_HOST="http://localhost:8000"
```

## Examples

| File | What it shows |
| ---- | ------------- |
| [`01_quickstart.py`](01_quickstart.py) | whoami, credit balance, create a list — the 60-second tour. |
| [`02_enrich_person.py`](02_enrich_person.py) | Enrich a single contact and poll the workflow to completion. |
| [`03_bulk_enrich_with_quote.py`](03_bulk_enrich_with_quote.py) | The estimate → quote → bulk-enrich credit flow. |
| [`04_lead_lists_crud.py`](04_lead_lists_crud.py) | Full lead-list lifecycle: create, update, add/remove leads, paginate, delete. |
| [`05_smart_agent.py`](05_smart_agent.py) | Run a custom AI smart-agent column over a list and read results. |
| [`06_export.py`](06_export.py) | Export a list to CSV (signed URL) and stream it as JSON. |
| [`07_async_quickstart.py`](07_async_quickstart.py) | The async client (`cleanlist_ai.aio`) end to end. |
| [`08_error_handling.py`](08_error_handling.py) | Catching typed API exceptions. |

Run any of them:

```bash
python examples/01_quickstart.py
```

> ⚠️ Examples that enrich or run smart agents **spend credits** (they estimate first and
> print the cost). Read each script's header before running.
