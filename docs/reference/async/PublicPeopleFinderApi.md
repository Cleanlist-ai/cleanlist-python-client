# cleanlist_ai.aio.PublicPeopleFinderApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_find_start**](PublicPeopleFinderApi.md#companies_find_start) | **POST** /api/v2/people/find-at-companies | Find people at companies by filter (async discovery)
[**companies_find_status**](PublicPeopleFinderApi.md#companies_find_status) | **GET** /api/v2/people/find-at-companies/status/{task_id} | Poll a find-people-at-companies search
[**compile_search**](PublicPeopleFinderApi.md#compile_search) | **POST** /api/v2/people/find/compile | Compile criteria without running the search
[**search_filters_people**](PublicPeopleFinderApi.md#search_filters_people) | **GET** /api/v2/people/find/filters | Search Filters People
[**search_people**](PublicPeopleFinderApi.md#search_people) | **POST** /api/v2/people/find | Search People


# **companies_find_start**
> CompaniesFindStartResponse companies_find_start(people_by_companies_request)

Find people at companies by filter (async discovery)

Start an async "find people at these companies" search. FREE — credits are
spent at enrichment / save time.

Returns a ``task_id`` immediately; poll ``poll_url``
(GET /people/find-at-companies/status/{task_id}) until ``status`` is terminal.
One job returns one result block; page by re-calling with the returned
``cursor``.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.companies_find_start_response import CompaniesFindStartResponse
from cleanlist_ai.aio.models.people_by_companies_request import PeopleByCompaniesRequest
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
    api_instance = cleanlist_ai.aio.PublicPeopleFinderApi(api_client)
    people_by_companies_request = cleanlist_ai.aio.PeopleByCompaniesRequest() # PeopleByCompaniesRequest | 

    try:
        # Find people at companies by filter (async discovery)
        api_response = await api_instance.companies_find_start(people_by_companies_request)
        print("The response of PublicPeopleFinderApi->companies_find_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPeopleFinderApi->companies_find_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **people_by_companies_request** | [**PeopleByCompaniesRequest**](PeopleByCompaniesRequest.md)|  | 

### Return type

[**CompaniesFindStartResponse**](CompaniesFindStartResponse.md)

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

# **companies_find_status**
> CompaniesFindStatusResponse companies_find_status(task_id)

Poll a find-people-at-companies search

Poll a search started by ``POST /people/find-at-companies``. Free and
idempotent —
call until ``status`` is terminal (``completed`` / ``failed``). Cross-tenant
task ids fail closed as 404.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.companies_find_status_response import CompaniesFindStatusResponse
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
    api_instance = cleanlist_ai.aio.PublicPeopleFinderApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Poll a find-people-at-companies search
        api_response = await api_instance.companies_find_status(task_id)
        print("The response of PublicPeopleFinderApi->companies_find_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPeopleFinderApi->companies_find_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**CompaniesFindStatusResponse**](CompaniesFindStatusResponse.md)

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

# **compile_search**
> CompileResponse compile_search(compile_request)

Compile criteria without running the search

Show what a search would do, without doing it. FREE.

Returns the compiled query, the route the search would take, and the
exclusions that would apply. Use it to check an unfamiliar combination of
criteria before spending a search, and to explain to a user why a result
is bounded: a by-companies route resolves a limited company set first, and
incomplete CRM exclusions block compilation with an actionable error.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.compile_request import CompileRequest
from cleanlist_ai.aio.models.compile_response import CompileResponse
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
    api_instance = cleanlist_ai.aio.PublicPeopleFinderApi(api_client)
    compile_request = cleanlist_ai.aio.CompileRequest() # CompileRequest | 

    try:
        # Compile criteria without running the search
        api_response = await api_instance.compile_search(compile_request)
        print("The response of PublicPeopleFinderApi->compile_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPeopleFinderApi->compile_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compile_request** | [**CompileRequest**](CompileRequest.md)|  | 

### Return type

[**CompileResponse**](CompileResponse.md)

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

# **search_filters_people**
> PeopleFiltersResponse search_filters_people(var_field, query=query)

Search Filters People

Valid filter values for people search. ZERO CREDITS.

Fixed-enum fields (seniority, management_levels, departments,
job_functions, company_headcount) return a canned list — Crustdata
accepts these values verbatim, no autocomplete needed.

Autocompletable fields (titles, locations, company_industries)
delegate to Crustdata's autocomplete with the friendly field name
translated via `_PEOPLE_AUTOCOMPLETE_FIELD_MAP`.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.people_filters_response import PeopleFiltersResponse
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
    api_instance = cleanlist_ai.aio.PublicPeopleFinderApi(api_client)
    var_field = 'var_field_example' # str | 
    query = 'query_example' # str |  (optional)

    try:
        # Search Filters People
        api_response = await api_instance.search_filters_people(var_field, query=query)
        print("The response of PublicPeopleFinderApi->search_filters_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPeopleFinderApi->search_filters_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_field** | **str**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**PeopleFiltersResponse**](PeopleFiltersResponse.md)

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

# **search_people**
> PeopleSearchResponse search_people(people_search_request)

Search People

Search people. FREE — credits are spent at enrichment / save time.

Delegates to the internal staging handler so the 5-step filter
pipeline (location component expansion → region contains expansion
→ column mapping → enum alias expansion → Crustdata format
transform) runs unchanged. We pass the caller's actual tier so
FREE-tier callers get the 25-row preview cap.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.people_search_request import PeopleSearchRequest
from cleanlist_ai.aio.models.people_search_response import PeopleSearchResponse
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
    api_instance = cleanlist_ai.aio.PublicPeopleFinderApi(api_client)
    people_search_request = cleanlist_ai.aio.PeopleSearchRequest() # PeopleSearchRequest | 

    try:
        # Search People
        api_response = await api_instance.search_people(people_search_request)
        print("The response of PublicPeopleFinderApi->search_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPeopleFinderApi->search_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **people_search_request** | [**PeopleSearchRequest**](PeopleSearchRequest.md)|  | 

### Return type

[**PeopleSearchResponse**](PeopleSearchResponse.md)

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

