# cleanlist_ai.PublicExportApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_csv**](PublicExportApi.md#export_csv) | **POST** /api/v2/export/csv/signed-url | Export a list to CSV (signed URL)
[**export_json**](PublicExportApi.md#export_json) | **GET** /api/v2/export/json | Export a list as JSON


# **export_csv**
> ExportCsvResponse export_csv(export_csv_request)

Export a list to CSV (signed URL)

Export a Lead List to CSV and return a time-limited signed download URL.

Streams the list's leads through a temporary spooled file, uploads the
result to blob storage, and responds with a SAS-signed `download_url`
that expires 24 hours after generation (see `expires_at`). Pass `columns`
to control which fields — and their order — are written, or omit it to use
the default column set; set `include_smart_agents=false` to skip any
configured smart-agent result columns. This export is free and does not
consume credits.

**📖 Docs:** https://docs.cleanlist.ai/guides/exporting-data

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.export_csv_request import ExportCsvRequest
from cleanlist_ai.models.export_csv_response import ExportCsvResponse
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
    api_instance = cleanlist_ai.PublicExportApi(api_client)
    export_csv_request = cleanlist_ai.ExportCsvRequest() # ExportCsvRequest | 

    try:
        # Export a list to CSV (signed URL)
        api_response = api_instance.export_csv(export_csv_request)
        print("The response of PublicExportApi->export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicExportApi->export_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_csv_request** | [**ExportCsvRequest**](ExportCsvRequest.md)|  | 

### Return type

[**ExportCsvResponse**](ExportCsvResponse.md)

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

# **export_json**
> ExportJsonResponse export_json(list_id, limit=limit, cursor=cursor, columns=columns)

Export a list as JSON

Export a Lead List as JSON rows returned inline in the response.

Returns a page of leads (default 100, max 500 per call) projected to the
same columns as the CSV export and wrapped in the standard response
envelope. Use the opaque `cursor` from each response to fetch the next
page; a malformed cursor returns 400 rather than silently rewinding to
page 0. This export is free and does not consume credits.

**📖 Docs:** https://docs.cleanlist.ai/guides/exporting-data

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai
from cleanlist_ai.models.export_json_response import ExportJsonResponse
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
    api_instance = cleanlist_ai.PublicExportApi(api_client)
    list_id = 'list_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    cursor = 'cursor_example' # str |  (optional)
    columns = ['columns_example'] # List[str] |  (optional)

    try:
        # Export a list as JSON
        api_response = api_instance.export_json(list_id, limit=limit, cursor=cursor, columns=columns)
        print("The response of PublicExportApi->export_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicExportApi->export_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **cursor** | **str**|  | [optional] 
 **columns** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ExportJsonResponse**](ExportJsonResponse.md)

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

