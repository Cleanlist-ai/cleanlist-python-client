# cleanlist_ai.aio.PublicPlaysApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_play_event**](PublicPlaysApi.md#get_play_event) | **GET** /api/v2/plays/{playbook_id}/events/{event_id} | Get Play Event
[**list_plays**](PublicPlaysApi.md#list_plays) | **GET** /api/v2/plays | List Plays
[**run_play**](PublicPlaysApi.md#run_play) | **POST** /api/v2/plays/{playbook_id}/runs | Run Play


# **get_play_event**
> PlayEventDto get_play_event(playbook_id, event_id)

Get Play Event

A record a play run admitted: whether a run took it yet, and which.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.play_event_dto import PlayEventDto
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
    api_instance = cleanlist_ai.aio.PublicPlaysApi(api_client)
    playbook_id = 'playbook_id_example' # str | 
    event_id = 'event_id_example' # str | 

    try:
        # Get Play Event
        api_response = await api_instance.get_play_event(playbook_id, event_id)
        print("The response of PublicPlaysApi->get_play_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPlaysApi->get_play_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_id** | **str**|  | 
 **event_id** | **str**|  | 

### Return type

[**PlayEventDto**](PlayEventDto.md)

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

# **list_plays**
> List[PlayDto] list_plays()

List Plays

This organization's agent plays, each with the inputs its webhook
trigger reads. A play without one has no inputs.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.play_dto import PlayDto
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
    api_instance = cleanlist_ai.aio.PublicPlaysApi(api_client)

    try:
        # List Plays
        api_response = await api_instance.list_plays()
        print("The response of PublicPlaysApi->list_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPlaysApi->list_plays: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlayDto]**](PlayDto.md)

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

# **run_play**
> ResponseRunPlayApiV2PlaysPlaybookIdRunsPost run_play(playbook_id, run_play_body, x_confirm_channel=x_confirm_channel)

Run Play

Run the play on one record made of ``inputs``, as its webhook would: a
preview without ``commit``, and with it a quote and the approval the
play needs.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.response_run_play_api_v2_plays_playbook_id_runs_post import ResponseRunPlayApiV2PlaysPlaybookIdRunsPost
from cleanlist_ai.aio.models.run_play_body import RunPlayBody
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
    api_instance = cleanlist_ai.aio.PublicPlaysApi(api_client)
    playbook_id = 'playbook_id_example' # str | 
    run_play_body = cleanlist_ai.aio.RunPlayBody() # RunPlayBody | 
    x_confirm_channel = 'x_confirm_channel_example' # str |  (optional)

    try:
        # Run Play
        api_response = await api_instance.run_play(playbook_id, run_play_body, x_confirm_channel=x_confirm_channel)
        print("The response of PublicPlaysApi->run_play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPlaysApi->run_play: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_id** | **str**|  | 
 **run_play_body** | [**RunPlayBody**](RunPlayBody.md)|  | 
 **x_confirm_channel** | **str**|  | [optional] 

### Return type

[**ResponseRunPlayApiV2PlaysPlaybookIdRunsPost**](ResponseRunPlayApiV2PlaysPlaybookIdRunsPost.md)

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

