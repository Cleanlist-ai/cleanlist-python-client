# Cleanlist AI Python SDK (`cleanlist-ai`)

Official Python client for the **[Cleanlist AI](https://cleanlist.ai) API (v2)** — B2B lead
discovery, waterfall enrichment, lead lists, smart agents, and export.

The package ships **both a standard and an asynchronous client** generated from the
public v2 OpenAPI schema, plus a small `Cleanlist` convenience facade so you can get
productive in a few lines.

```python
from cleanlist_ai import Cleanlist

with Cleanlist(access_token="clapi_live_...") as cl:
    print(cl.workspace.whoami().organization_name)
    lst = cl.lead_lists.create_list({"name": "Q3 outbound"})
    print("created list:", lst.list_id)
```

- ✅ Fully typed (Pydantic v2 models for every request & response)
- ✅ Standard (`cleanlist_ai`) **and** async (`cleanlist_ai.aio`) — same method names
- ✅ Bearer-token auth, sensible production defaults
- ✅ Generated from the same schema the API serves, so it never drifts

---

## Table of contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Quickstart (standard)](#quickstart-standard)
- [Quickstart (async)](#quickstart-async)
- [Configuration](#configuration)
- [Core concepts](#core-concepts)
  - [Credits & the estimate → quote flow](#credits--the-estimate--quote-flow)
  - [Enrichment is asynchronous — poll for results](#enrichment-is-asynchronous--poll-for-results)
- [Endpoint reference](#endpoint-reference)
  - [Workspace](#workspace-clworkspace)
  - [Lead Lists](#lead-lists-cllead_lists)
  - [Enrichment](#enrichment-clenrichment)
  - [Smart Agents](#smart-agents-clsmart_agents)
  - [Export](#export-clexport)
- [Error handling](#error-handling)
- [Pagination](#pagination)
- [Using the generated API classes directly](#using-the-generated-api-classes-directly)
- [Regenerating from the schema](#regenerating-from-the-schema)
- [Support](#support)

---

## Installation

```bash
pip install cleanlist-ai
```

Requires Python 3.8+. Installing pulls in both the standard (`urllib3`) and async
(`aiohttp`) runtimes, so both clients work out of the box.

## Authentication

Every request is authenticated with a **Cleanlist API key**, sent as an
`Authorization: Bearer <key>` header. Create one in the portal under
**[Settings → API Keys](https://app.cleanlist.ai/api-keys)** (keys look like
`clapi_live_...`).

Pass it explicitly, or set the `CLEANLIST_API_KEY` environment variable and let the
client pick it up:

```python
from cleanlist_ai import Cleanlist

cl = Cleanlist(access_token="clapi_live_...")   # explicit
cl = Cleanlist()                                # reads CLEANLIST_API_KEY
```

```bash
export CLEANLIST_API_KEY="clapi_live_..."
```

> **Keep keys secret.** Never commit them. Prefer environment variables or a secrets
> manager over hard-coding.

## Quickstart (standard)

```python
from cleanlist_ai import Cleanlist
from cleanlist_ai.models import CreateListRequest, EnrichPersonRequest

with Cleanlist() as cl:                                     # CLEANLIST_API_KEY
    # 1. Who am I? (identity, tier, credit-affecting scopes)
    me = cl.workspace.whoami()
    print(f"Org: {me.organization_name} | tier: {me.tier}")

    # 2. Check credit balance
    print("credits:", cl.workspace.credits_balance().credits)

    # 3. Create a lead list
    lst = cl.lead_lists.create_list(CreateListRequest(name="Demo — API"))
    print("list id:", lst.list_id)

    # 4. Enrich a single person into that list (async workflow — returns a handle)
    job = cl.enrichment.enrich_person(
        EnrichPersonRequest(
            lead_list_id=lst.list_id,
            first_name="Ada",
            last_name="Lovelace",
            company_name="Analytical Engines",
        )
    )
    print("enrichment workflow:", job.workflow_id, "| reserved:", job.credits_reserved)

    # 5. Poll until it settles
    status = cl.enrichment.enrichment_status(job.workflow_id)
    print("status:", status.status)
```

## Quickstart (async)

Everything is identical, but under `cleanlist_ai.aio`, awaited, and driven from an
`async with` block:

```python
import asyncio
from cleanlist_ai.aio import Cleanlist
from cleanlist_ai.aio.models import CreateListRequest

async def main():
    async with Cleanlist() as cl:                          # CLEANLIST_API_KEY
        me = await cl.workspace.whoami()
        print("org:", me.organization_name)

        lst = await cl.lead_lists.create_list(CreateListRequest(name="Demo — async"))
        print("list id:", lst.list_id)

asyncio.run(main())
```

> Import models from `cleanlist_ai.aio.models` when using the async client (they are the
> same shapes as `cleanlist_ai.models`; both are accepted, kept separate for typing).

## Configuration

`Cleanlist(...)` accepts:

| Argument        | Default                    | Description                                                            |
| --------------- | -------------------------- | ---------------------------------------------------------------------- |
| `access_token`  | `$CLEANLIST_API_KEY`       | Your API key. Sent as `Authorization: Bearer …`.                       |
| `host`          | `https://api.cleanlist.ai` | API base URL. Use `http://localhost:8000` for local dev.               |
| `configuration` | `None`                     | A pre-built `Configuration` for advanced needs (proxy, retries, etc.). |

For finer control, build a `Configuration` yourself:

```python
from cleanlist_ai import Cleanlist, Configuration

config = Configuration(host="https://api.cleanlist.ai", access_token="clapi_live_...")
config.retries = 3            # urllib3 retry count (standard)
cl = Cleanlist(configuration=config)
```

Per-request timeouts are supported on every method via `_request_timeout` (seconds, or a
`(connect, read)` tuple):

```python
cl.workspace.whoami(_request_timeout=10)
```

## Core concepts

### Credits & the estimate → quote flow

Search and list management are free; **enrichment and smart-agent runs cost credits**.
Bulk/paid operations (`enrich_list`, `run_smart_agent`, and CSV import with enrichment)
require a **signed quote** obtained from `credits_estimate` first. The quote pins the
price and is single-use:

```python
from cleanlist_ai.models import EstimateCostRequest, EnrichListRequest

quote = cl.workspace.credits_estimate(
    EstimateCostRequest(tool="enrich_list", list_id=lst.list_id, scope="full")
)
print(f"cost={quote.estimated_cost} sufficient={quote.sufficient} quote={quote.quote_id}")

if quote.sufficient:
    run = cl.enrichment.enrich_list(
        EnrichListRequest(list_id=lst.list_id, scope="full", quote_id=quote.quote_id)
    )
    print("bulk workflow:", run.workflow_id)
```

Enrichment **scopes** (what you pay for per lead):

| Scope        | Returns                            | Cost       |
| ------------ | ---------------------------------- | ---------- |
| `partial`    | email + LinkedIn + title + company | 1 credit   |
| `phone_only` | phone only                         | 10 credits |
| `full`       | email **and** phone                | 11 credits |

Pricing is **pay-for-results** — the reservation (`credits_reserved`) is a cap; the
unused portion is refunded when the workflow settles.

### Enrichment is asynchronous — poll for results

`enrich_person`, `enrich_company`, `enrich_by_task`, and `enrich_list` **dispatch a
workflow** and return immediately with a `workflow_id` (and a `poll_url`). Poll
`enrichment_status(workflow_id)` until `status` is `completed` (or `failed`):

```python
import time

job = cl.enrichment.enrich_person(EnrichPersonRequest(lead_list_id=lst.list_id, email="ada@example.com"))
while True:
    s = cl.enrichment.enrichment_status(job.workflow_id)
    print(s.status, s.processed, "/", s.total)
    if s.status in ("completed", "failed", "cancelled"):
        break
    time.sleep(3)
print("charged:", s.credits_charged, "refunded:", s.credits_refunded)
```

See [`examples/`](examples/) for a complete, runnable polling helper (standard & async).

---

## Endpoint reference

The v2 surface is 24 operations across five resource groups, exposed on the `Cleanlist`
facade as `cl.workspace`, `cl.lead_lists`, `cl.enrichment`, `cl.smart_agents`, and
`cl.export`. All examples below use the standard client; prepend `await` (and import from
`cleanlist_ai.aio…`) for async.

Auto-generated, field-by-field docs for every model live in
[`docs/reference/`](docs/reference/).

### Workspace (`cl.workspace`)

Identity, credits, API keys, and usage.

| Method                                  | HTTP                            | Description                                            |
| --------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| `whoami()`                              | `GET /api/v2/whoami`            | Current identity, org, tier, scopes & feature grants.  |
| `credits_balance()`                     | `GET /api/v2/credits/balance`   | Spendable credit balance for the org.                  |
| `credits_estimate(EstimateCostRequest)` | `POST /api/v2/credits/estimate` | Price an operation and get a signed, single-use quote. |
| `list_api_keys()`                       | `GET /api/v2/api-keys`          | List the org's API keys (metadata only).               |
| `usage_report(days=…, group_by=…)`      | `GET /api/v2/usage`             | Credit-usage report over a window.                     |

```python
me      = cl.workspace.whoami()
balance = cl.workspace.credits_balance()
keys    = cl.workspace.list_api_keys()
usage   = cl.workspace.usage_report(days=30, group_by="tool")

quote = cl.workspace.credits_estimate(
    EstimateCostRequest(tool="enrich_person", scope="full", row_count=1)
)
```

### Lead Lists (`cl.lead_lists`)

Create and manage lists and the leads inside them.

| Method                                                | HTTP                                           | Description                              |
| ----------------------------------------------------- | ---------------------------------------------- | ---------------------------------------- |
| `create_list(CreateListRequest)`                      | `POST /api/v2/lead-lists`                      | Create a list (idempotent on name).      |
| `list_lists(folder_id=…, limit=…, cursor=…)`          | `GET /api/v2/lead-lists`                       | List your lead lists (paginated).        |
| `get_list(list_id)`                                   | `GET /api/v2/lead-lists/{list_id}`             | Fetch one list.                          |
| `update_list(list_id, PublicLeadListUpdate)`          | `PATCH /api/v2/lead-lists/{list_id}`           | Rename / move / edit description.        |
| `delete_list(list_id)`                                | `DELETE /api/v2/lead-lists/{list_id}`          | Delete a list.                           |
| `list_leads_in_list(list_id, limit=…, cursor=…)`      | `GET /api/v2/lead-lists/{list_id}/leads`       | Page through leads.                      |
| `add_leads_to_list(list_id, Body)`                    | `POST /api/v2/lead-lists/{list_id}/leads`      | Add leads by id or from a search cohort. |
| `remove_leads_from_list(list_id, RemoveLeadsRequest)` | `DELETE /api/v2/lead-lists/{list_id}/leads`    | Remove up to 100 leads.                  |
| `csv_import(list_id, CsvImportRequest)`               | `POST /api/v2/lead-lists/{list_id}/csv-import` | Import leads from a base64 CSV.          |

```python
from cleanlist_ai.models import (
    CreateListRequest, PublicLeadListUpdate, Body, AddByLeadIds, RemoveLeadsRequest,
)

lst = cl.lead_lists.create_list(CreateListRequest(name="Prospects — West"))

cl.lead_lists.update_list(lst.list_id, PublicLeadListUpdate(description="US west region"))

page = cl.lead_lists.list_leads_in_list(lst.list_id, limit=100)
print(page.total, "leads")

# Add leads you already have ids for (Body is a one-of: ids OR a search cohort)
cl.lead_lists.add_leads_to_list(
    lst.list_id, Body(AddByLeadIds(lead_ids=["lead_abc", "lead_def"]))
)

cl.lead_lists.remove_leads_from_list(lst.list_id, RemoveLeadsRequest(lead_ids=["lead_abc"]))
```

### Enrichment (`cl.enrichment`)

Run the provider waterfall to find emails/phones. All dispatch an async workflow (poll
`enrichment_status`).

| Method                                 | HTTP                                          | Description                                    |
| -------------------------------------- | --------------------------------------------- | ---------------------------------------------- |
| `enrich_person(EnrichPersonRequest)`   | `POST /api/v2/enrichment/person`              | Enrich one contact into a list.                |
| `enrich_company(EnrichCompanyRequest)` | `POST /api/v2/enrichment/company`             | Enrich a company by domain/name/ticker.        |
| `enrich_by_task(EnrichByTaskRequest)`  | `POST /api/v2/enrichment/by-task`             | Enrich entities from a prior search/list task. |
| `enrich_list(EnrichListRequest)`       | `POST /api/v2/enrichment/bulk`                | Bulk-enrich a whole list (needs a `quote_id`). |
| `enrichment_status(workflow_id)`       | `GET /api/v2/enrichment/status/{workflow_id}` | Poll a workflow's progress & results.          |

```python
from cleanlist_ai.models import (
    EnrichPersonRequest, EnrichCompanyRequest, EnrichByTaskRequest, EnrichListRequest,
)

person = cl.enrichment.enrich_person(
    EnrichPersonRequest(lead_list_id=lst.list_id, linkedin_url="https://linkedin.com/in/ada")
)

company = cl.enrichment.enrich_company(EnrichCompanyRequest(domain="stripe.com"))

status = cl.enrichment.enrichment_status(person.workflow_id)
```

### Smart Agents (`cl.smart_agents`)

Run AI columns over a list (custom prompts, cold intros, preset research agents).

| Method                                         | HTTP                                             | Description                                           |
| ---------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| `run_smart_agent(RunSmartAgentRequest)`        | `POST /api/v2/smart-agents/run`                  | Run an agent as a new AI column (needs a `quote_id`). |
| `list_smart_agents(list_id=…, limit=…)`        | `GET /api/v2/smart-agents`                       | Recent agent runs (optionally per-list).              |
| `get_smart_agent_results(smart_agent_task_id)` | `GET /api/v2/smart-agents/{smart_agent_task_id}` | Fetch a run's per-lead output.                        |

```python
from cleanlist_ai.models import EstimateCostRequest, RunSmartAgentRequest

quote = cl.workspace.credits_estimate(
    EstimateCostRequest(tool="run_smart_agent", list_id=lst.list_id, agent_type="custom_ai", row_count=50)
)
run = cl.smart_agents.run_smart_agent(
    RunSmartAgentRequest(
        list_id=lst.list_id,
        agent_type="custom_ai",
        column_name="Personalized angle",
        prompt="In one sentence, suggest a cold-outreach angle for this lead.",
        max_rows=50,
        quote_id=quote.quote_id,
    )
)
results = cl.smart_agents.get_smart_agent_results(run.smart_agent_task_id)
```

### Export (`cl.export`)

| Method                                                 | HTTP                                 | Description                                          |
| ------------------------------------------------------ | ------------------------------------ | ---------------------------------------------------- |
| `export_csv(ExportCsvRequest)`                         | `POST /api/v2/export/csv/signed-url` | Export a list to CSV; returns a signed download URL. |
| `export_json(list_id, limit=…, cursor=…, columns=[…])` | `GET /api/v2/export/json`            | Export list rows inline as JSON (paginated).         |

```python
from cleanlist_ai.models import ExportCsvRequest

signed = cl.export.export_csv(ExportCsvRequest(list_id=lst.list_id))
print("download:", signed.download_url)   # signed URL, valid until signed.expires_at

data = cl.export.export_json(lst.list_id, limit=500)
for row in data.leads:
    print(row)
```

## Error handling

Non-2xx responses raise `ApiException` (subclasses expose `status`, `reason`, `body`,
and parsed `data` where available):

```python
from cleanlist_ai import ApiException
from cleanlist_ai.exceptions import NotFoundException, UnauthorizedException

try:
    cl.lead_lists.get_list("does-not-exist")
except NotFoundException:
    print("no such list")
except UnauthorizedException:
    print("bad or missing API key")
except ApiException as e:
    print(f"API error {e.status}: {e.body}")
```

Validation errors (HTTP 422) come back as `HTTPValidationError` in `e.data`.

## Pagination

List endpoints return a page plus an opaque `cursor`. Pass it back to fetch the next
page; a falsy cursor means you've reached the end:

```python
cursor = None
while True:
    page = cl.lead_lists.list_leads_in_list(lst.list_id, limit=500, cursor=cursor)
    for lead in page.leads:
        ...
    cursor = page.cursor
    if not cursor:
        break
```

## Using the generated API classes directly

The `Cleanlist` facade is optional sugar. You can wire the generated pieces yourself:

```python
from cleanlist_ai import ApiClient, Configuration
from cleanlist_ai.api import PublicWorkspaceApi

config = Configuration(host="https://api.cleanlist.ai", access_token="clapi_live_...")
with ApiClient(config) as api_client:
    workspace = PublicWorkspaceApi(api_client)
    print(workspace.whoami())
```

The async equivalents live under `cleanlist_ai.aio` (`ApiClient`, `Configuration`,
`cleanlist_ai.aio.api.*`).

## Regenerating from the schema

This SDK is generated from the backend's public v2 OpenAPI schema with
[`openapi-generator-cli`](https://openapi-generator.tech) (pinned in
`openapitools.json`). To refresh after an API change:

```bash
# 1. Re-export openapi/cleanse-api-v2.oas.json from the backend, then:
PYTHON=python3 bash scripts/generate.sh
```

`scripts/generate.sh` cleans the operation ids into readable method names
(`scripts/prepare_spec.py`), generates the standard + async clients, and re-applies the
`Cleanlist` facade overlay.

## Support

- Interactive API docs (OpenAPI): <https://api.cleanlist.ai/docs>
- Docs & guides: <https://docs.cleanlist.ai>
- Dashboard: <https://app.cleanlist.ai>
- Email: [sal@cleanlist.ai](mailto:sal@cleanlist.ai)

Licensed under the [MIT License](LICENSE).
