# cleanlist_ai.aio.PublicWebhooksApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](PublicWebhooksApi.md#create_webhook) | **POST** /api/v2/webhooks | Subscribe a URL to events
[**delete_webhook**](PublicWebhooksApi.md#delete_webhook) | **DELETE** /api/v2/webhooks/{webhook_id} | Remove a webhook
[**list_webhook_deliveries**](PublicWebhooksApi.md#list_webhook_deliveries) | **GET** /api/v2/webhooks/deliveries | List webhook deliveries
[**list_webhooks**](PublicWebhooksApi.md#list_webhooks) | **GET** /api/v2/webhooks | List webhooks


# **create_webhook**
> CreatedWebhook create_webhook(create_webhook_request)

Subscribe a URL to events

Subscribe a public HTTPS URL to event types. Returns the signing
secret once: verify each delivery's `Cleanlist-Signature` header
(`t=<unix>,v1=<hex HMAC-SHA256 of "<t>.<raw body>">`) with it.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.create_webhook_request import CreateWebhookRequest
from cleanlist_ai.aio.models.created_webhook import CreatedWebhook
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
    api_instance = cleanlist_ai.aio.PublicWebhooksApi(api_client)
    create_webhook_request = cleanlist_ai.aio.CreateWebhookRequest() # CreateWebhookRequest | 

    try:
        # Subscribe a URL to events
        api_response = await api_instance.create_webhook(create_webhook_request)
        print("The response of PublicWebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**CreatedWebhook**](CreatedWebhook.md)

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

# **delete_webhook**
> DeletedWebhook delete_webhook(webhook_id)

Remove a webhook

Stop sending events to a subscription. Its delivery log stays.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.deleted_webhook import DeletedWebhook
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
    api_instance = cleanlist_ai.aio.PublicWebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Remove a webhook
        api_response = await api_instance.delete_webhook(webhook_id)
        print("The response of PublicWebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**DeletedWebhook**](DeletedWebhook.md)

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

# **list_webhook_deliveries**
> object list_webhook_deliveries(workflow_id, limit=limit)

List webhook deliveries

Delivery attempts for a `workflow_id`, newest first: the v1 route. For
a subscription's event, pass the event id (`evt_...`); the log's
`webhook_id` is the subscription's id.

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
    api_instance = cleanlist_ai.aio.PublicWebhooksApi(api_client)
    workflow_id = 'workflow_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List webhook deliveries
        api_response = await api_instance.list_webhook_deliveries(workflow_id, limit=limit)
        print("The response of PublicWebhooksApi->list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebhooksApi->list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]

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

# **list_webhooks**
> WebhooksResponse list_webhooks()

List webhooks

List this organization's active webhook subscriptions. Secrets are
never returned after creation.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.webhooks_response import WebhooksResponse
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
    api_instance = cleanlist_ai.aio.PublicWebhooksApi(api_client)

    try:
        # List webhooks
        api_response = await api_instance.list_webhooks()
        print("The response of PublicWebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicWebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

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

