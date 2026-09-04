# cleanlist_ai.PublicLeadListsApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_leads_to_list**](PublicLeadListsApi.md#add_leads_to_list) | **POST** /api/v2/lead-lists/{list_id}/leads | Add leads to a list
[**create_list**](PublicLeadListsApi.md#create_list) | **POST** /api/v2/lead-lists | Create a lead list
[**csv_import**](PublicLeadListsApi.md#csv_import) | **POST** /api/v2/lead-lists/{list_id}/csv-import | Import leads from CSV
[**delete_list**](PublicLeadListsApi.md#delete_list) | **DELETE** /api/v2/lead-lists/{list_id} | Delete a lead list
[**get_list**](PublicLeadListsApi.md#get_list) | **GET** /api/v2/lead-lists/{list_id} | Get a lead list
[**list_leads_in_list**](PublicLeadListsApi.md#list_leads_in_list) | **GET** /api/v2/lead-lists/{list_id}/leads | List leads in a list
[**list_lists**](PublicLeadListsApi.md#list_lists) | **GET** /api/v2/lead-lists | List lead lists
[**remove_leads_from_list**](PublicLeadListsApi.md#remove_leads_from_list) | **DELETE** /api/v2/lead-lists/{list_id}/leads | Remove leads from a list
[**update_list**](PublicLeadListsApi.md#update_list) | **PATCH** /api/v2/lead-lists/{list_id} | Update a lead list


# **add_leads_to_list**
> AddLeadsResponse add_leads_to_list(list_id, body)

Add leads to a list

Add leads to a list in one of two mutually-exclusive modes.

Mode A (`lead_ids`): add already-materialized leads by UUID.
Mode B (`task_id` [+ `entity_ids`]): materialize a prior search
cohort into the list (search rows carry integer search-DB ids, not
lead UUIDs, so they can't go through Mode A).

The body is an exclusive `oneOf` union (`AddByLeadIds | AddByCohort`):
both-set or neither-set bodies are rejected at the schema layer (422),
so this handler only sees a well-formed single mode. Filter-based add
is rejected — the MCP description tells the agent to translate filters
into a cohort task_id (or lead_ids) first.

Import / "Add to list" is FREE — materializing leads costs no credits;
only enrichment is billed separately. Pass an optional `idempotency_key`
so a retried add inserts exactly once. Requires the `lists:write` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.add_leads_response import AddLeadsResponse
from cleanlist_ai.models.body import Body
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 
    body = cleanlist_ai.Body() # Body | 

    try:
        # Add leads to a list
        api_response = api_instance.add_leads_to_list(list_id, body)
        print("The response of PublicLeadListsApi->add_leads_to_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->add_leads_to_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**AddLeadsResponse**](AddLeadsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ListDetailResponse create_list(create_list_request)

Create a lead list

Create a private LeadList in the caller's workspace.

Idempotent on name: MCP agents sometimes fire create_list twice for one
"make a list" request (seconds apart), leaving an orphan empty list. If
the caller already OWNS an exact same-name list (case-insensitive),
reuse it instead of inserting a duplicate — returns 200 + `reused: true`.
Strictly caller-scoped: a user never reuses a teammate's org-visible
list, and match is exact name only, so "Q3 Leads" never reuses
"Q3 Leads List".

Requires the `lists:write` scope. Public-tier keys carry no contact-list
cap, but the cap is still enforced defensively (403 `list_cap_reached`).
Pass an optional `folder_id` you own to file the new list on creation.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.create_list_request import CreateListRequest
from cleanlist_ai.models.list_detail_response import ListDetailResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    create_list_request = cleanlist_ai.CreateListRequest() # CreateListRequest | 

    try:
        # Create a lead list
        api_response = api_instance.create_list(create_list_request)
        print("The response of PublicLeadListsApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->create_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_request** | [**CreateListRequest**](CreateListRequest.md)|  | 

### Return type

[**ListDetailResponse**](ListDetailResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csv_import**
> CsvImportResponse csv_import(list_id, csv_import_request)

Import leads from CSV

Import a CSV into a lead list and optionally dispatch bulk enrichment.

Pipeline:
    1. Authz: `lists:write` always; `enrich:write` additionally when
       `dispatch_enrichment=True` (the workflow spends credits).
    2. Feature flag gate — disabled-by-default kill switch returns 503.
    3. Idempotency cache lookup (org-wide, 24h TTL).
    4. Base64 decode + parse via `parse_csv_to_rawpeople`.
    5. If dispatching: verify quote (if provided), open reservation,
       redeem quote.
    6. Bulk-insert RawPeople into the list. UUIDs are stamped
       Python-side so we can hand them to the workflow.
    7. If dispatching: kick off `start_bulk_enrichment` with the
       parsed prospects + raw_person_ids. The workflow's per-Lead
       `insert_lead_to_list` activity handles prospect_count
       updates per the existing pattern; import-only path bumps
       prospect_count here directly.
    8. Cache the response under `idempotency_key` (if provided).

Cross-list dedup: this endpoint dedupes ONLY within the upload. A
row whose identity already exists as a Lead elsewhere in the
workspace still imports as a RawPerson here; the workflow's
`persist_enrichment_result` then deduplicates against existing
Leads by public_identifier / prospect_id (existing behavior).
Net effect: no duplicate Lead, but the RawPerson stub persists
until the workflow processes it.

Send the file as base64 in `csv_content_base64` (≤150 KB / ~600 rows)
with a `column_mapping` from canonical field to CSV header. Requires the
`lists:write` scope, plus `enrich:write` when `dispatch_enrichment=true`
(the enrichment spend). Importing rows is free; when dispatching,
enrichment is billed on top (partial 1cr, phone_only 10cr, full 11cr per
lead). Pass an `idempotency_key` to make retries safe.

**📖 Docs:** https://docs.cleanlist.ai/guides/bulk-enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.csv_import_request import CsvImportRequest
from cleanlist_ai.models.csv_import_response import CsvImportResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 
    csv_import_request = cleanlist_ai.CsvImportRequest() # CsvImportRequest | 

    try:
        # Import leads from CSV
        api_response = api_instance.csv_import(list_id, csv_import_request)
        print("The response of PublicLeadListsApi->csv_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->csv_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **csv_import_request** | [**CsvImportRequest**](CsvImportRequest.md)|  | 

### Return type

[**CsvImportResponse**](CsvImportResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> DeleteListResponse delete_list(list_id)

Delete a lead list

Delete a list and its lead memberships. Leads survive.

Hard delete via `delete_with_dependencies` (mirrors the portal):
smart/action columns, CRM-contact links, per-user state, shares,
raw-person stubs, and junction rows are removed; the Lead rows
themselves are global entities and are NOT deleted — they stay
findable via search_people and in any other list they belong to.

Owner-only + is_protected guards mirror the portal. There is no
in-flight-workflow guard (the portal has none either; the MCP
confirm-gate already prevents accidental deletes off a fuzzy name
match). Re-deleting an unknown/already-deleted list returns 404.

Owner-only: a non-owner gets 404 (indistinguishable from missing) and a
protected list gets 403 `list_protected`. Requires the `lists:write`
scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.delete_list_response import DeleteListResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Delete a lead list
        api_response = api_instance.delete_list(list_id)
        print("The response of PublicLeadListsApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**DeleteListResponse**](DeleteListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> ListDetailResponse get_list(list_id)

Get a lead list

Return one LeadList accessible to the caller.

`lead_count` is derived from a live membership COUNT rather than the
denormalized `prospect_count` column, so a just-completed add/remove is
reflected immediately and any historical counter drift can't surface a
wrong number here.

Resolves any list you can access — owned, org-visible, or shared with
you — and 404s otherwise so private lists never leak. Requires the
`lists:read` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.list_detail_response import ListDetailResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Get a lead list
        api_response = api_instance.get_list(list_id)
        print("The response of PublicLeadListsApi->get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**ListDetailResponse**](ListDetailResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_leads_in_list**
> LeadsPageResponse list_leads_in_list(list_id, limit=limit, cursor=cursor)

List leads in a list

Paginate leads in a list.

Fields like `first_name`, `last_name`, `title`, `company` come from
the joined Prospect + Company relations — the Lead row itself only
carries enrichment results (email, phone, linkedin URL).

Page forward with `limit` (1–500, default 100) and the opaque `cursor`.
The response also carries a `task_id` cohort handle for the page so a
follow-up `add_person_enrichments` can operate on these leads without
re-passing lead_ids. Requires the `lists:read` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.leads_page_response import LeadsPageResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List leads in a list
        api_response = api_instance.list_leads_in_list(list_id, limit=limit, cursor=cursor)
        print("The response of PublicLeadListsApi->list_leads_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->list_leads_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **cursor** | **str**|  | [optional] 

### Return type

[**LeadsPageResponse**](LeadsPageResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lists**
> ListsPageResponse list_lists(folder_id=folder_id, limit=limit, cursor=cursor)

List lead lists

Paginate the lead lists the caller can access (owned, org-wide, shared).

Returns a page of `ListSummary` rows with live lead counts and owner
names. Page forward with `limit` (1–100, default 50) and the opaque
`cursor` from the previous response; omit `cursor` to start at the top.
Pass `folder_id` to scope the page to one folder. Requires the
`lists:read` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.lists_page_response import ListsPageResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    folder_id = 'folder_id_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List lead lists
        api_response = api_instance.list_lists(folder_id=folder_id, limit=limit, cursor=cursor)
        print("The response of PublicLeadListsApi->list_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->list_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **cursor** | **str**|  | [optional] 

### Return type

[**ListsPageResponse**](ListsPageResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_leads_from_list**
> RemoveLeadsResponse remove_leads_from_list(list_id, remove_leads_request)

Remove leads from a list

Remove leads from a list (max 100 per call).

Removes the membership row only — the Lead itself stays in the
workspace (still findable via `search_people`, still in other lists
it belonged to). Non-existent lead_ids are silently no-op so the
caller can dedupe loosely without 404s.

Removing leads is free — no credits are refunded or charged. Requires the
`lists:write` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.remove_leads_request import RemoveLeadsRequest
from cleanlist_ai.models.remove_leads_response import RemoveLeadsResponse
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 
    remove_leads_request = cleanlist_ai.RemoveLeadsRequest() # RemoveLeadsRequest | 

    try:
        # Remove leads from a list
        api_response = api_instance.remove_leads_from_list(list_id, remove_leads_request)
        print("The response of PublicLeadListsApi->remove_leads_from_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->remove_leads_from_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **remove_leads_request** | [**RemoveLeadsRequest**](RemoveLeadsRequest.md)|  | 

### Return type

[**RemoveLeadsResponse**](RemoveLeadsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ListDetailResponse update_list(list_id, public_lead_list_update)

Update a lead list

Rename a list (and optionally re-describe it / move it between folders).

PATCH semantics: only the fields present in the body change. A `null`
`description` clears it; a `null` `folder_id` unfiles the list; an
omitted field is left untouched. Renaming to the current name is an
idempotent 200 no-op. Owner-only + is_protected guards mirror the
portal's edit path.

At least one of `name`, `description`, or `folder_id` must be present;
an empty body is a 422. Requires the `lists:write` scope.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/lead-lists · https://docs.cleanlist.ai/guides/managing-lists

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.list_detail_response import ListDetailResponse
from cleanlist_ai.models.public_lead_list_update import PublicLeadListUpdate
from cleanlist_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cleanlist_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.PublicLeadListsApi(api_client)
    list_id = 'list_id_example' # str | 
    public_lead_list_update = cleanlist_ai.PublicLeadListUpdate() # PublicLeadListUpdate | 

    try:
        # Update a lead list
        api_response = api_instance.update_list(list_id, public_lead_list_update)
        print("The response of PublicLeadListsApi->update_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLeadListsApi->update_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **public_lead_list_update** | [**PublicLeadListUpdate**](PublicLeadListUpdate.md)|  | 

### Return type

[**ListDetailResponse**](ListDetailResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

