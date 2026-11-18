# cleanlist_ai.PublicInboxApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_inbox_threads**](PublicInboxApi.md#list_inbox_threads) | **GET** /api/v2/inbox/threads | List Inbox Threads
[**read_inbox_thread**](PublicInboxApi.md#read_inbox_thread) | **GET** /api/v2/inbox/threads/{thread_id} | Read Inbox Thread
[**reply_in_inbox_thread**](PublicInboxApi.md#reply_in_inbox_thread) | **POST** /api/v2/inbox/threads/{thread_id}/reply | Reply In Inbox Thread
[**update_inbox_thread**](PublicInboxApi.md#update_inbox_thread) | **PATCH** /api/v2/inbox/threads/{thread_id} | Update Inbox Thread


# **list_inbox_threads**
> Dict[str, List[Dict[str, object]]] list_inbox_threads(status=status, since=since, q=q, limit=limit, offset=offset)

List Inbox Threads

Inbox conversations newest first, as the Inbox lists them. ``done``
is the archived ones; ``since`` keeps those with a message on or after
that day (UTC).

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
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
    api_instance = cleanlist_ai.PublicInboxApi(api_client)
    status = open # str |  (optional) (default to open)
    since = 'since_example' # str | YYYY-MM-DD (optional)
    q = 'q_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Inbox Threads
        api_response = api_instance.list_inbox_threads(status=status, since=since, q=q, limit=limit, offset=offset)
        print("The response of PublicInboxApi->list_inbox_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicInboxApi->list_inbox_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] [default to open]
 **since** | **str**| YYYY-MM-DD | [optional] 
 **q** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

**Dict[str, List[Dict[str, object]]]**

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

# **read_inbox_thread**
> object read_inbox_thread(thread_id)

Read Inbox Thread

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
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
    api_instance = cleanlist_ai.PublicInboxApi(api_client)
    thread_id = 'thread_id_example' # str | 

    try:
        # Read Inbox Thread
        api_response = api_instance.read_inbox_thread(thread_id)
        print("The response of PublicInboxApi->read_inbox_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicInboxApi->read_inbox_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 

### Return type

**object**

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

# **reply_in_inbox_thread**
> object reply_in_inbox_thread(thread_id, reply_body)

Reply In Inbox Thread

Reply to the lead from the address the Inbox replies from. Needs
``commit: true``; without it the answer names who would get it.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.reply_body import ReplyBody
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
    api_instance = cleanlist_ai.PublicInboxApi(api_client)
    thread_id = 'thread_id_example' # str | 
    reply_body = cleanlist_ai.ReplyBody() # ReplyBody | 

    try:
        # Reply In Inbox Thread
        api_response = api_instance.reply_in_inbox_thread(thread_id, reply_body)
        print("The response of PublicInboxApi->reply_in_inbox_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicInboxApi->reply_in_inbox_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **reply_body** | [**ReplyBody**](ReplyBody.md)|  | 

### Return type

**object**

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

# **update_inbox_thread**
> object update_inbox_thread(thread_id, update_thread_body)

Update Inbox Thread

``done`` archives the conversation and closes its Reply task; ``open``
brings it back.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.update_thread_body import UpdateThreadBody
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
    api_instance = cleanlist_ai.PublicInboxApi(api_client)
    thread_id = 'thread_id_example' # str | 
    update_thread_body = cleanlist_ai.UpdateThreadBody() # UpdateThreadBody | 

    try:
        # Update Inbox Thread
        api_response = api_instance.update_inbox_thread(thread_id, update_thread_body)
        print("The response of PublicInboxApi->update_inbox_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicInboxApi->update_inbox_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **update_thread_body** | [**UpdateThreadBody**](UpdateThreadBody.md)|  | 

### Return type

**object**

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

