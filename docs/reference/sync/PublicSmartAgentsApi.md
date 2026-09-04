# cleanlist_ai.PublicSmartAgentsApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smart_agent_results**](PublicSmartAgentsApi.md#get_smart_agent_results) | **GET** /api/v2/smart-agents/{smart_agent_task_id} | Get smart agent results
[**list_smart_agents**](PublicSmartAgentsApi.md#list_smart_agents) | **GET** /api/v2/smart-agents | List smart agent runs
[**run_smart_agent**](PublicSmartAgentsApi.md#run_smart_agent) | **POST** /api/v2/smart-agents/run | Run a smart agent


# **get_smart_agent_results**
> SmartAgentResultsResponse get_smart_agent_results(smart_agent_task_id)

Get smart agent results

Poll a smart-agent run for status, progress, and per-lead output.

Returns the run's lifecycle `status`, a `progress` percentage, and
succeeded / failed / total counters, along with a `results` array holding
each lead's agent output (or its error). Poll this after
POST /smart-agents/run until `status` is `completed` (or `failed`) — the
`results` array grows as leads finish, so a still-running run returns a
partial set. Access is checked via the run's list, and unknown or
inaccessible run ids return 404. This endpoint is free and does not
consume credits.

**📖 Docs:** https://docs.cleanlist.ai/guides/using-ai-agents

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.smart_agent_results_response import SmartAgentResultsResponse
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
    api_instance = cleanlist_ai.PublicSmartAgentsApi(api_client)
    smart_agent_task_id = 'smart_agent_task_id_example' # str | Canonical id from /smart-agents/run's `smart_agent_task_id` field

    try:
        # Get smart agent results
        api_response = api_instance.get_smart_agent_results(smart_agent_task_id)
        print("The response of PublicSmartAgentsApi->get_smart_agent_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSmartAgentsApi->get_smart_agent_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_agent_task_id** | **str**| Canonical id from /smart-agents/run&#39;s &#x60;smart_agent_task_id&#x60; field | 

### Return type

[**SmartAgentResultsResponse**](SmartAgentResultsResponse.md)

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

# **list_smart_agents**
> ListSmartAgentsResponse list_smart_agents(list_id=list_id, limit=limit)

List smart agent runs

List recent smart-agent runs with live progress counters.

Returns each run's id, target list, agent type, status, and processed /
failed / total counts so you can track in-flight and completed runs. Pass
`list_id` to scope to a single list (access-checked so a known id can't
enumerate another workspace's history); omit it for a caller-scoped rollup
across every list you can see. This endpoint is free and does not consume
credits. To read the per-lead output of any run, call
GET /smart-agents/{smart_agent_task_id}.

**📖 Docs:** https://docs.cleanlist.ai/guides/using-ai-agents

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.list_smart_agents_response import ListSmartAgentsResponse
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
    api_instance = cleanlist_ai.PublicSmartAgentsApi(api_client)
    list_id = 'list_id_example' # str | Optional lead-list UUID. When set, returns only runs for that list (access-checked). When omitted, returns a rollup of recent runs across every list the caller can see. (optional)
    limit = 20 # int | Maximum number of runs to return, most recent first. (optional) (default to 20)

    try:
        # List smart agent runs
        api_response = api_instance.list_smart_agents(list_id=list_id, limit=limit)
        print("The response of PublicSmartAgentsApi->list_smart_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSmartAgentsApi->list_smart_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| Optional lead-list UUID. When set, returns only runs for that list (access-checked). When omitted, returns a rollup of recent runs across every list the caller can see. | [optional] 
 **limit** | **int**| Maximum number of runs to return, most recent first. | [optional] [default to 20]

### Return type

[**ListSmartAgentsResponse**](ListSmartAgentsResponse.md)

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

# **run_smart_agent**
> RunSmartAgentResponse run_smart_agent(run_smart_agent_request)

Run a smart agent

Launch an AI smart agent over the leads in a list and return a run id.

Pick an `agent_type` — `custom_ai` (your own `prompt`), `cold_intro_email`
(personalized opener), or a preset research agent — and the run executes
asynchronously as a smart column, one AI call per lead. Runs are metered
per lead by agent type (e.g. `custom_ai` ≈ 1 credit/lead,
`cold_intro_email` ≈ 3 credits/lead) and require a single-use `quote_id`
from POST /credits/estimate; credits are debited as rows complete. Scope
with `lead_scope="subset"` + `max_rows` for speed and cost control — a
`lead_scope="all"` run above the approval threshold (default 500 leads)
is blocked with a 400 `approval_required` until you narrow it or route a
human approval. The response returns immediately with `status="pending"`;
poll GET /smart-agents/{smart_agent_task_id} for progress and per-lead
results.

**📖 Docs:** https://docs.cleanlist.ai/guides/using-ai-agents

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.run_smart_agent_request import RunSmartAgentRequest
from cleanlist_ai.models.run_smart_agent_response import RunSmartAgentResponse
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
    api_instance = cleanlist_ai.PublicSmartAgentsApi(api_client)
    run_smart_agent_request = cleanlist_ai.RunSmartAgentRequest() # RunSmartAgentRequest | 

    try:
        # Run a smart agent
        api_response = api_instance.run_smart_agent(run_smart_agent_request)
        print("The response of PublicSmartAgentsApi->run_smart_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSmartAgentsApi->run_smart_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_smart_agent_request** | [**RunSmartAgentRequest**](RunSmartAgentRequest.md)|  | 

### Return type

[**RunSmartAgentResponse**](RunSmartAgentResponse.md)

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

