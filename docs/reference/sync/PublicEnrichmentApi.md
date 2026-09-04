# cleanlist_ai.PublicEnrichmentApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrich_by_task**](PublicEnrichmentApi.md#enrich_by_task) | **POST** /api/v2/enrichment/by-task | Enrich entities from a prior task
[**enrich_company**](PublicEnrichmentApi.md#enrich_company) | **POST** /api/v2/enrichment/company | Enrich a company
[**enrich_list**](PublicEnrichmentApi.md#enrich_list) | **POST** /api/v2/enrichment/bulk | Enrich a whole lead list
[**enrich_person**](PublicEnrichmentApi.md#enrich_person) | **POST** /api/v2/enrichment/person | Enrich a single person
[**enrichment_status**](PublicEnrichmentApi.md#enrichment_status) | **GET** /api/v2/enrichment/status/{workflow_id} | Poll an enrichment workflow


# **enrich_by_task**
> EnrichByTaskResponse enrich_by_task(enrich_by_task_request)

Enrich entities from a prior task

Enrich a cohort of entities referenced by a `task_id` returned from a
prior search, without re-listing every identifier.

The task's entity type decides the flow. Person (or lead) tasks dispatch
an asynchronous workflow — the response carries a `workflow_id` with every
entity `queued`, and results land in `lead_list_id` (a hidden per-user
scratch list is auto-created when none is given); poll status for
progress. Company tasks run synchronously — each entity returns an
inline `enriched`/`skipped`/`failed` result with no workflow. Both paths
are billed per entity and REQUIRE a `quote_id` from POST /credits/estimate
(person cohort cost follows the requested data points; company cohort is
~1 credit per 10 companies), settling with pay-for-results semantics.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment
**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment-types
**📖 Docs:** https://docs.cleanlist.ai/guides/bulk-enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.enrich_by_task_request import EnrichByTaskRequest
from cleanlist_ai.models.enrich_by_task_response import EnrichByTaskResponse
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
    api_instance = cleanlist_ai.PublicEnrichmentApi(api_client)
    enrich_by_task_request = cleanlist_ai.EnrichByTaskRequest() # EnrichByTaskRequest | 

    try:
        # Enrich entities from a prior task
        api_response = api_instance.enrich_by_task(enrich_by_task_request)
        print("The response of PublicEnrichmentApi->enrich_by_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicEnrichmentApi->enrich_by_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrich_by_task_request** | [**EnrichByTaskRequest**](EnrichByTaskRequest.md)|  | 

### Return type

[**EnrichByTaskResponse**](EnrichByTaskResponse.md)

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

# **enrich_company**
> EnrichCompanyResponse enrich_company(enrich_company_request)

Enrich a company

Look up firmographics for a single company and return the full record
synchronously.

Unlike person enrichment, this path is synchronous — it performs a
CompanyDB single-record lookup inline (no Temporal workflow, no
`workflow_id`) and returns the enriched `CompanyRecord` in the response,
billing a flat 1 credit that settles before the response returns. Pass
any of `domain` (most reliable), `company_id`, `company_name`, or
`company_ticker`; a ticker is resolved to a domain via Finnhub (24h Redis
cache) and falls back to a `company_name` fuzzy match when the symbol is
unknown. `quote_id` is optional and, when present, verified and redeemed.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment
**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment-types
**📖 Docs:** https://docs.cleanlist.ai/guides/bulk-enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.enrich_company_request import EnrichCompanyRequest
from cleanlist_ai.models.enrich_company_response import EnrichCompanyResponse
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
    api_instance = cleanlist_ai.PublicEnrichmentApi(api_client)
    enrich_company_request = cleanlist_ai.EnrichCompanyRequest() # EnrichCompanyRequest | 

    try:
        # Enrich a company
        api_response = api_instance.enrich_company(enrich_company_request)
        print("The response of PublicEnrichmentApi->enrich_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicEnrichmentApi->enrich_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrich_company_request** | [**EnrichCompanyRequest**](EnrichCompanyRequest.md)|  | 

### Return type

[**EnrichCompanyResponse**](EnrichCompanyResponse.md)

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

# **enrich_list**
> EnrichListResponse enrich_list(enrich_list_request)

Enrich a whole lead list

Run the provider waterfall over every lead in an existing list in one
call.

This is an asynchronous, fan-out workflow: it reserves the estimated cost,
returns a `workflow_id` immediately, then enriches all leads in parallel
background child workflows — poll `poll_url` for aggregate progress and
the settled billing. `scope` sets the per-lead enrichment type
(`partial` = 1 credit, `phone-only` = 10, `full` = 11). A `quote_id` from
POST /credits/estimate is REQUIRED and bound to this list + scope + lead
count; the actual charge is the recomputed cost capped at the quote's
`max_credits`, and pay-for-results refunds the unused reservation for
leads where nothing was found.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment
**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment-types
**📖 Docs:** https://docs.cleanlist.ai/guides/bulk-enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.enrich_list_request import EnrichListRequest
from cleanlist_ai.models.enrich_list_response import EnrichListResponse
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
    api_instance = cleanlist_ai.PublicEnrichmentApi(api_client)
    enrich_list_request = cleanlist_ai.EnrichListRequest() # EnrichListRequest | 

    try:
        # Enrich a whole lead list
        api_response = api_instance.enrich_list(enrich_list_request)
        print("The response of PublicEnrichmentApi->enrich_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicEnrichmentApi->enrich_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrich_list_request** | [**EnrichListRequest**](EnrichListRequest.md)|  | 

### Return type

[**EnrichListResponse**](EnrichListResponse.md)

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

# **enrich_person**
> EnrichPersonResponse enrich_person(enrich_person_request)

Enrich a single person

Resolve email and/or phone for one contact through the provider
waterfall and write the result to a lead list.

This is an asynchronous workflow: it reserves credits up front, returns
a `workflow_id` immediately, then runs the provider cascade in the
background — poll `poll_url` (GET /enrichment/status/{workflow_id}) until
`status` is terminal. Cost is set by `enrichment_type`: 1 credit for
`partial` (email only), 10 for `phone_only`, or 11 for `full` (email +
phone); the legacy `include_phone` boolean is used when the field is
unset. Pay-for-results means the final debit may be lower than
`credits_reserved`. `quote_id` is optional here — single-call scale
doesn't require it, but a supplied quote is verified and redeemed so the
caller can pre-commit spend.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment
**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment-types
**📖 Docs:** https://docs.cleanlist.ai/guides/bulk-enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.enrich_person_request import EnrichPersonRequest
from cleanlist_ai.models.enrich_person_response import EnrichPersonResponse
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
    api_instance = cleanlist_ai.PublicEnrichmentApi(api_client)
    enrich_person_request = cleanlist_ai.EnrichPersonRequest() # EnrichPersonRequest | 

    try:
        # Enrich a single person
        api_response = api_instance.enrich_person(enrich_person_request)
        print("The response of PublicEnrichmentApi->enrich_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicEnrichmentApi->enrich_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrich_person_request** | [**EnrichPersonRequest**](EnrichPersonRequest.md)|  | 

### Return type

[**EnrichPersonResponse**](EnrichPersonResponse.md)

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

# **enrichment_status**
> WorkflowStatusResponse enrichment_status(workflow_id)

Poll an enrichment workflow

Poll the status, progress, and settled billing of an enrichment
workflow started by `enrich_person`, `enrich_list`, or `enrich_by_task`.

This read is free and idempotent — call it repeatedly until `status`
reaches a terminal state (`completed` / `failed` / `cancelled`). It
accepts EITHER a `workflow_id` (e.g. `enrich-...` / `bulk-enrich-...`) OR
an MCPTask cohort `task_id` (`cl-task_...`), resolving the latter to the
workflow bound at dispatch so the agent can keep using the one handle it
already has. Terminal single-lead runs include the inline enriched `result`;
bulk runs report aggregate counters instead. When a prepaid-via-MCP run
ends in failure, `refund_status` surfaces `pending_review` (credits are
not auto-refunded).

**📖 Docs:** https://docs.cleanlist.ai/api-reference/enrichment

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.workflow_status_response import WorkflowStatusResponse
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
    api_instance = cleanlist_ai.PublicEnrichmentApi(api_client)
    workflow_id = 'workflow_id_example' # str | 

    try:
        # Poll an enrichment workflow
        api_response = api_instance.enrichment_status(workflow_id)
        print("The response of PublicEnrichmentApi->enrichment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicEnrichmentApi->enrichment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 

### Return type

[**WorkflowStatusResponse**](WorkflowStatusResponse.md)

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

