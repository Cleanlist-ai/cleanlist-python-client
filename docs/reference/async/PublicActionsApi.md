# cleanlist_ai.aio.PublicActionsApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_action**](PublicActionsApi.md#call_action) | **POST** /api/v2/actions/{name} | Call an action
[**confirm_card**](PublicActionsApi.md#confirm_card) | **POST** /api/v2/actions/confirm | Confirm a card
[**list_actions**](PublicActionsApi.md#list_actions) | **GET** /api/v2/actions | List actions


# **call_action**
> ActionResult call_action(name, action_call)

Call an action

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.action_call import ActionCall
from cleanlist_ai.aio.models.action_result import ActionResult
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
    api_instance = cleanlist_ai.aio.PublicActionsApi(api_client)
    name = 'name_example' # str | 
    action_call = cleanlist_ai.aio.ActionCall() # ActionCall | 

    try:
        # Call an action
        api_response = await api_instance.call_action(name, action_call)
        print("The response of PublicActionsApi->call_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicActionsApi->call_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **action_call** | [**ActionCall**](ActionCall.md)|  | 

### Return type

[**ActionResult**](ActionResult.md)

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

# **confirm_card**
> ConfirmResult confirm_card(confirm_call)

Confirm a card

Run a card's held arguments once, after the person said yes.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.confirm_call import ConfirmCall
from cleanlist_ai.aio.models.confirm_result import ConfirmResult
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
    api_instance = cleanlist_ai.aio.PublicActionsApi(api_client)
    confirm_call = cleanlist_ai.aio.ConfirmCall() # ConfirmCall | 

    try:
        # Confirm a card
        api_response = await api_instance.confirm_card(confirm_call)
        print("The response of PublicActionsApi->confirm_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicActionsApi->confirm_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_call** | [**ConfirmCall**](ConfirmCall.md)|  | 

### Return type

[**ConfirmResult**](ConfirmResult.md)

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

# **list_actions**
> Manifest list_actions()

List actions

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.manifest import Manifest
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
    api_instance = cleanlist_ai.aio.PublicActionsApi(api_client)

    try:
        # List actions
        api_response = await api_instance.list_actions()
        print("The response of PublicActionsApi->list_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicActionsApi->list_actions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Manifest**](Manifest.md)

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

