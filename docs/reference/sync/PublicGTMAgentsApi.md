# cleanlist_ai.PublicGTMAgentsApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gtm_agent**](PublicGTMAgentsApi.md#create_gtm_agent) | **POST** /api/v2/gtm-agents | Create Gtm Agent
[**get_gtm_agent**](PublicGTMAgentsApi.md#get_gtm_agent) | **GET** /api/v2/gtm-agents/{agent_id} | Get Gtm Agent
[**get_gtm_run**](PublicGTMAgentsApi.md#get_gtm_run) | **GET** /api/v2/gtm-runs/{run_id} | Get Gtm Run
[**list_gtm_agent_runs**](PublicGTMAgentsApi.md#list_gtm_agent_runs) | **GET** /api/v2/gtm-agents/{agent_id}/runs | List Gtm Agent Runs
[**list_gtm_agents**](PublicGTMAgentsApi.md#list_gtm_agents) | **GET** /api/v2/gtm-agents | List Gtm Agents
[**list_gtm_run_records**](PublicGTMAgentsApi.md#list_gtm_run_records) | **GET** /api/v2/gtm-runs/{run_id}/records | List Gtm Run Records
[**patch_gtm_agent**](PublicGTMAgentsApi.md#patch_gtm_agent) | **PATCH** /api/v2/gtm-agents/{agent_id} | Patch Gtm Agent
[**run_gtm_agent**](PublicGTMAgentsApi.md#run_gtm_agent) | **POST** /api/v2/gtm-agents/{agent_id}/runs | Run Gtm Agent
[**set_gtm_agent_status**](PublicGTMAgentsApi.md#set_gtm_agent_status) | **POST** /api/v2/gtm-agents/{agent_id}/status | Set Gtm Agent Status


# **create_gtm_agent**
> AgentDto create_gtm_agent(create_gtm_agent_body)

Create Gtm Agent

A draft agent, off, with no play, owned by the caller, with any settings.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.agent_dto import AgentDto
from cleanlist_ai.models.create_gtm_agent_body import CreateGtmAgentBody
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    create_gtm_agent_body = cleanlist_ai.CreateGtmAgentBody() # CreateGtmAgentBody | 

    try:
        # Create Gtm Agent
        api_response = api_instance.create_gtm_agent(create_gtm_agent_body)
        print("The response of PublicGTMAgentsApi->create_gtm_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->create_gtm_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_gtm_agent_body** | [**CreateGtmAgentBody**](CreateGtmAgentBody.md)|  | 

### Return type

[**AgentDto**](AgentDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gtm_agent**
> AgentDto get_gtm_agent(agent_id)

Get Gtm Agent

One agent, with its plays and status.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.agent_dto import AgentDto
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Gtm Agent
        api_response = api_instance.get_gtm_agent(agent_id)
        print("The response of PublicGTMAgentsApi->get_gtm_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->get_gtm_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**AgentDto**](AgentDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gtm_run**
> RunDetailDto get_gtm_run(run_id)

Get Gtm Run

One run: its status, counts and per-step stats.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.run_detail_dto import RunDetailDto
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Get Gtm Run
        api_response = api_instance.get_gtm_run(run_id)
        print("The response of PublicGTMAgentsApi->get_gtm_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->get_gtm_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 

### Return type

[**RunDetailDto**](RunDetailDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gtm_agent_runs**
> List[RunSummaryDto] list_gtm_agent_runs(agent_id)

List Gtm Agent Runs

The agent's runs, newest first.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.run_summary_dto import RunSummaryDto
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # List Gtm Agent Runs
        api_response = api_instance.list_gtm_agent_runs(agent_id)
        print("The response of PublicGTMAgentsApi->list_gtm_agent_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->list_gtm_agent_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**List[RunSummaryDto]**](RunSummaryDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gtm_agents**
> List[AgentDto] list_gtm_agents()

List Gtm Agents

This organization's agents, newest first.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.agent_dto import AgentDto
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)

    try:
        # List Gtm Agents
        api_response = api_instance.list_gtm_agents()
        print("The response of PublicGTMAgentsApi->list_gtm_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->list_gtm_agents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AgentDto]**](AgentDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |
**422** | Request failed validation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gtm_run_records**
> RecordsPageDto list_gtm_run_records(run_id, node_id=node_id, status=status, cursor=cursor, limit=limit, include=include)

List Gtm Run Records

A page of the run's records, and with ``include=outputs`` what each
step wrote for them.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.records_page_dto import RecordsPageDto
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    run_id = 'run_id_example' # str | 
    node_id = 'node_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    include = 'include_example' # str | `outputs` adds each record's step outputs. (optional)

    try:
        # List Gtm Run Records
        api_response = api_instance.list_gtm_run_records(run_id, node_id=node_id, status=status, cursor=cursor, limit=limit, include=include)
        print("The response of PublicGTMAgentsApi->list_gtm_run_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->list_gtm_run_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **node_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **include** | **str**| &#x60;outputs&#x60; adds each record&#39;s step outputs. | [optional] 

### Return type

[**RecordsPageDto**](RecordsPageDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_gtm_agent**
> AgentDto patch_gtm_agent(agent_id, patch_gtm_agent_body)

Patch Gtm Agent

Change the name, settings or schedule, by the portal's PATCH rules. An
agent that is on changes only its name, description and favorite.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.agent_dto import AgentDto
from cleanlist_ai.models.patch_gtm_agent_body import PatchGtmAgentBody
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    patch_gtm_agent_body = cleanlist_ai.PatchGtmAgentBody() # PatchGtmAgentBody | 

    try:
        # Patch Gtm Agent
        api_response = api_instance.patch_gtm_agent(agent_id, patch_gtm_agent_body)
        print("The response of PublicGTMAgentsApi->patch_gtm_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->patch_gtm_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **patch_gtm_agent_body** | [**PatchGtmAgentBody**](PatchGtmAgentBody.md)|  | 

### Return type

[**AgentDto**](AgentDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_gtm_agent**
> ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost run_gtm_agent(agent_id, run_gtm_agent_body, x_confirm_channel=x_confirm_channel)

Run Gtm Agent

Start one live run of the agent's play now: a preview without
``commit``, and with it a quote and the approval its play needs. Answers
``{run_id, agent_id, status, message}``, or ``queued`` with no run yet
when a CRM cleanup play waits for its scan.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post import ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost
from cleanlist_ai.models.run_gtm_agent_body import RunGtmAgentBody
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    run_gtm_agent_body = cleanlist_ai.RunGtmAgentBody() # RunGtmAgentBody | 
    x_confirm_channel = 'x_confirm_channel_example' # str |  (optional)

    try:
        # Run Gtm Agent
        api_response = api_instance.run_gtm_agent(agent_id, run_gtm_agent_body, x_confirm_channel=x_confirm_channel)
        print("The response of PublicGTMAgentsApi->run_gtm_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->run_gtm_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **run_gtm_agent_body** | [**RunGtmAgentBody**](RunGtmAgentBody.md)|  | 
 **x_confirm_channel** | **str**|  | [optional] 

### Return type

[**ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost**](ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_gtm_agent_status**
> ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost set_gtm_agent_status(agent_id, gtm_agent_status_body, x_confirm_channel=x_confirm_channel)

Set Gtm Agent Status

Turn an agent off, or on with the On toggle's checks: a preview
without ``commit``, and with it a quote and the approval its plays need
(see the module note).

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.gtm_agent_status_body import GtmAgentStatusBody
from cleanlist_ai.models.response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post import ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost
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
    api_instance = cleanlist_ai.PublicGTMAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    gtm_agent_status_body = cleanlist_ai.GtmAgentStatusBody() # GtmAgentStatusBody | 
    x_confirm_channel = 'x_confirm_channel_example' # str |  (optional)

    try:
        # Set Gtm Agent Status
        api_response = api_instance.set_gtm_agent_status(agent_id, gtm_agent_status_body, x_confirm_channel=x_confirm_channel)
        print("The response of PublicGTMAgentsApi->set_gtm_agent_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMAgentsApi->set_gtm_agent_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **gtm_agent_status_body** | [**GtmAgentStatusBody**](GtmAgentStatusBody.md)|  | 
 **x_confirm_channel** | **str**|  | [optional] 

### Return type

[**ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost**](ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request failed validation. |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required or invalid. |  -  |
**403** | Permission denied or feature not enabled. |  -  |
**404** | Resource not found. |  -  |
**409** | Resource conflict. |  -  |
**429** | Rate limited. |  -  |
**500** | Internal error. |  -  |
**502** | Upstream provider error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

