# cleanlist_ai.aio.PublicGTMTasksApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gtm_task**](PublicGTMTasksApi.md#create_gtm_task) | **POST** /api/v2/gtm-tasks | Create Gtm Task
[**get_gtm_task**](PublicGTMTasksApi.md#get_gtm_task) | **GET** /api/v2/gtm-tasks/{task_id} | Get Gtm Task
[**list_gtm_tasks**](PublicGTMTasksApi.md#list_gtm_tasks) | **GET** /api/v2/gtm-tasks | List Gtm Tasks
[**list_updates**](PublicGTMTasksApi.md#list_updates) | **GET** /api/v2/updates | List Updates
[**update_gtm_task**](PublicGTMTasksApi.md#update_gtm_task) | **PATCH** /api/v2/gtm-tasks/{task_id} | Update Gtm Task


# **create_gtm_task**
> object create_gtm_task(create_task_body)

Create Gtm Task

A task for the caller on a lead in one of the organization's sequences.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.create_task_body import CreateTaskBody
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
    api_instance = cleanlist_ai.aio.PublicGTMTasksApi(api_client)
    create_task_body = cleanlist_ai.aio.CreateTaskBody() # CreateTaskBody | 

    try:
        # Create Gtm Task
        api_response = await api_instance.create_gtm_task(create_task_body)
        print("The response of PublicGTMTasksApi->create_gtm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMTasksApi->create_gtm_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_body** | [**CreateTaskBody**](CreateTaskBody.md)|  | 

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
**201** | Successful Response |  -  |
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

# **get_gtm_task**
> object get_gtm_task(task_id)

Get Gtm Task

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
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
    api_instance = cleanlist_ai.aio.PublicGTMTasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Gtm Task
        api_response = await api_instance.get_gtm_task(task_id)
        print("The response of PublicGTMTasksApi->get_gtm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMTasksApi->get_gtm_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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

# **list_gtm_tasks**
> Dict[str, List[Dict[str, object]]] list_gtm_tasks(status=status, task_type=task_type, limit=limit)

List Gtm Tasks

The caller's tasks, as the Tasks page lists them.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
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
    api_instance = cleanlist_ai.aio.PublicGTMTasksApi(api_client)
    status = open # str |  (optional) (default to open)
    task_type =  # str |  (optional) (default to )
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List Gtm Tasks
        api_response = await api_instance.list_gtm_tasks(status=status, task_type=task_type, limit=limit)
        print("The response of PublicGTMTasksApi->list_gtm_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMTasksApi->list_gtm_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] [default to open]
 **task_type** | **str**|  | [optional] [default to ]
 **limit** | **int**|  | [optional] [default to 50]

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

# **list_updates**
> object list_updates(since=since, limit=limit)

List Updates

Everything new since ``since`` (up to 30 days back).

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
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
    api_instance = cleanlist_ai.aio.PublicGTMTasksApi(api_client)
    since = 'since_example' # str | An ISO time or a day; default 24 hours ago. (optional)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Updates
        api_response = await api_instance.list_updates(since=since, limit=limit)
        print("The response of PublicGTMTasksApi->list_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMTasksApi->list_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| An ISO time or a day; default 24 hours ago. | [optional] 
 **limit** | **int**|  | [optional] [default to 10]

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

# **update_gtm_task**
> object update_gtm_task(task_id, update_task_body)

Update Gtm Task

``done`` completes the task as the Tasks page does (a call task needs
``outcome``); ``skipped`` brings it back on its sequence's next sending
day.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.update_task_body import UpdateTaskBody
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
    api_instance = cleanlist_ai.aio.PublicGTMTasksApi(api_client)
    task_id = 'task_id_example' # str | 
    update_task_body = cleanlist_ai.aio.UpdateTaskBody() # UpdateTaskBody | 

    try:
        # Update Gtm Task
        api_response = await api_instance.update_gtm_task(task_id, update_task_body)
        print("The response of PublicGTMTasksApi->update_gtm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicGTMTasksApi->update_gtm_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **update_task_body** | [**UpdateTaskBody**](UpdateTaskBody.md)|  | 

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

