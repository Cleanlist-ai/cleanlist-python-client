# cleanlist_ai.aio.PublicWorkspaceApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credits_balance**](PublicWorkspaceApi.md#credits_balance) | **GET** /api/v2/credits/balance | Get credit balance
[**credits_estimate**](PublicWorkspaceApi.md#credits_estimate) | **POST** /api/v2/credits/estimate | Estimate cost &amp; get a signed quote
[**list_api_keys**](PublicWorkspaceApi.md#list_api_keys) | **GET** /api/v2/api-keys | List API keys
[**usage_report**](PublicWorkspaceApi.md#usage_report) | **GET** /api/v2/usage | Get usage report
[**whoami**](PublicWorkspaceApi.md#whoami) | **GET** /api/v2/whoami | Get current identity &amp; entitlements


# **credits_balance**
> CreditsBalanceResponse credits_balance()

Get credit balance

Return the current spendable credit balance for the caller's organization.
Reads the authoritative `organizations.credits_count` and returns it with a
short `agent_instructions` nudge summarizing remaining credits. Requires the
`credits:read` scope and deducts no credits itself. Use this before large
operations, and pair it with `POST /credits/estimate` to confirm a specific
action is affordable before spending.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.credits_balance_response import CreditsBalanceResponse
from cleanlist_ai.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.aio.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.aio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with cleanlist_ai.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.aio.PublicWorkspaceApi(api_client)

    try:
        # Get credit balance
        api_response = await api_instance.credits_balance()
        print("The response of PublicWorkspaceApi->credits_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWorkspaceApi->credits_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreditsBalanceResponse**](CreditsBalanceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credits_estimate**
> EstimateCostResponse credits_estimate(estimate_cost_request)

Estimate cost & get a signed quote

Pre-flight a paid operation and mint a signed, single-use `quote_id`.
The quote binds the canonical request (tool, list_id|filters|cohort, scope,
row_count, org) via HMAC and must be presented at execution time by every
paid bulk tool (`enrich_list`, `run_smart_agent`, `sync_to_crm`,
`sync_to_sequencer`, cohort enrichments). Row count is derived
authoritatively from the list or cohort — never trusted from the caller —
so a small quote can't be replayed against a large job. Requires the
`credits:read` scope; estimating itself is free, and the response reports
whether the org has `sufficient` credits to proceed.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.estimate_cost_request import EstimateCostRequest
from cleanlist_ai.aio.models.estimate_cost_response import EstimateCostResponse
from cleanlist_ai.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.aio.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.aio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with cleanlist_ai.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.aio.PublicWorkspaceApi(api_client)
    estimate_cost_request = cleanlist_ai.aio.EstimateCostRequest() # EstimateCostRequest | 

    try:
        # Estimate cost & get a signed quote
        api_response = await api_instance.credits_estimate(estimate_cost_request)
        print("The response of PublicWorkspaceApi->credits_estimate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWorkspaceApi->credits_estimate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_cost_request** | [**EstimateCostRequest**](EstimateCostRequest.md)|  | 

### Return type

[**EstimateCostResponse**](EstimateCostResponse.md)

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

# **list_api_keys**
> ApiKeysResponse list_api_keys()

List API keys

List the caller's API keys, showing only the prefix and last 4 characters
— full secret values are never returned. Results are user-scoped and further
filtered to the calling token's organization (defense in depth), so a Clerk
user in multiple orgs only sees keys belonging to the active org. Requires
the `admin:api_keys` scope and deducts no credits. Scopes are granted
per-user today, so each key reports the caller's own scopes.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/authentication

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.api_keys_response import ApiKeysResponse
from cleanlist_ai.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.aio.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.aio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with cleanlist_ai.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.aio.PublicWorkspaceApi(api_client)

    try:
        # List API keys
        api_response = await api_instance.list_api_keys()
        print("The response of PublicWorkspaceApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWorkspaceApi->list_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKeysResponse**](ApiKeysResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_report**
> UsageReportResponse usage_report(days=days, group_by=group_by)

Get usage report

Aggregate this organization's public-API request log over the last `days`
(1-365, default 7), grouped by `tool`, `key`, `day`, or `error`. Returns
per-bucket call counts and error counts plus window totals, so admins can
audit traffic and spot failing integrations. Requires the `admin:api_keys`
scope and deducts no credits. Note: until the request log gains cost/
tool-name columns, `group_by="tool"` buckets by request path and
`credits_spent` is always 0.0.

**📖 Docs:** https://docs.cleanlist.ai/api-reference/credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.usage_report_response import UsageReportResponse
from cleanlist_ai.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.aio.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.aio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with cleanlist_ai.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.aio.PublicWorkspaceApi(api_client)
    days = 7 # int |  (optional) (default to 7)
    group_by = tool # str |  (optional) (default to tool)

    try:
        # Get usage report
        api_response = await api_instance.usage_report(days=days, group_by=group_by)
        print("The response of PublicWorkspaceApi->usage_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWorkspaceApi->usage_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 7]
 **group_by** | **str**|  | [optional] [default to tool]

### Return type

[**UsageReportResponse**](UsageReportResponse.md)

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

# **whoami**
> WhoamiResponse whoami()

Get current identity & entitlements

Introspect the authenticated principal and its effective entitlements.
Returns the caller's identity (user, org, auth type, scopes) plus the
resolved plan `tier`, any `appsumo_tier`, and the merged `features` list
the server-side gates actually enforce — letting clients (and the MCP)
tier-filter their advertised tools before hitting a gated route. This
endpoint is free and deducts no credits; for API-key auth the returned
`user_email` is masked so a leaked key can't reveal the creator's address,
and display-name lookups are best-effort (null on a transient miss).

**📖 Docs:** https://docs.cleanlist.ai/api-reference/authentication

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.whoami_response import WhoamiResponse
from cleanlist_ai.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cleanlist.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = cleanlist_ai.aio.Configuration(
    host = "https://api.cleanlist.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = cleanlist_ai.aio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with cleanlist_ai.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cleanlist_ai.aio.PublicWorkspaceApi(api_client)

    try:
        # Get current identity & entitlements
        api_response = await api_instance.whoami()
        print("The response of PublicWorkspaceApi->whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWorkspaceApi->whoami: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhoamiResponse**](WhoamiResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

