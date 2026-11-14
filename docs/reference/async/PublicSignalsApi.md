# cleanlist_ai.aio.PublicSignalsApi

All URIs are relative to *https://api.cleanlist.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_job_changes**](PublicSignalsApi.md#check_job_changes) | **POST** /api/v2/job-changes/check | Check Job Changes
[**companies_by_technology**](PublicSignalsApi.md#companies_by_technology) | **POST** /api/v2/companies/by-technology | Companies using a technology
[**company_signals**](PublicSignalsApi.md#company_signals) | **POST** /api/v2/companies/signals | Company Signals
[**linkedin_post_engagers**](PublicSignalsApi.md#linkedin_post_engagers) | **POST** /api/v2/linkedin/posts/engagers | People engaging with LinkedIn posts
[**list_job_changes**](PublicSignalsApi.md#list_job_changes) | **GET** /api/v2/job-changes | List Job Changes
[**search_job_postings**](PublicSignalsApi.md#search_job_postings) | **POST** /api/v2/jobs/search | Search Job Postings
[**search_linkedin_posts**](PublicSignalsApi.md#search_linkedin_posts) | **POST** /api/v2/linkedin/posts/search | Search LinkedIn posts on a topic


# **check_job_changes**
> object check_job_changes(job_change_check_request)

Check Job Changes

Where these people work now, from their LinkedIn profiles: the read
the Job history step makes. Every person named, up to 500; quote first.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.job_change_check_request import JobChangeCheckRequest
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    job_change_check_request = cleanlist_ai.aio.JobChangeCheckRequest() # JobChangeCheckRequest | 

    try:
        # Check Job Changes
        api_response = await api_instance.check_job_changes(job_change_check_request)
        print("The response of PublicSignalsApi->check_job_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->check_job_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_change_check_request** | [**JobChangeCheckRequest**](JobChangeCheckRequest.md)|  | 

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

# **companies_by_technology**
> object companies_by_technology(technology_body)

Companies using a technology

Companies that use any of the named technologies and match company
filters: the tool adoption play step's current-user search, at its own
per-company price. Technology names are exact (``/search/values``).

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.technology_body import TechnologyBody
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    technology_body = cleanlist_ai.aio.TechnologyBody() # TechnologyBody | 

    try:
        # Companies using a technology
        api_response = await api_instance.companies_by_technology(technology_body)
        print("The response of PublicSignalsApi->companies_by_technology:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->companies_by_technology: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **technology_body** | [**TechnologyBody**](TechnologyBody.md)|  | 

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

# **company_signals**
> object company_signals(company_signals_request)

Company Signals

Signals the workspace's company signal watches delivered at these
accounts. Free for units already paid for; otherwise quote first.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.company_signals_request import CompanySignalsRequest
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    company_signals_request = cleanlist_ai.aio.CompanySignalsRequest() # CompanySignalsRequest | 

    try:
        # Company Signals
        api_response = await api_instance.company_signals(company_signals_request)
        print("The response of PublicSignalsApi->company_signals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->company_signals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_signals_request** | [**CompanySignalsRequest**](CompanySignalsRequest.md)|  | 

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

# **linkedin_post_engagers**
> object linkedin_post_engagers(post_engagers_body)

People engaging with LinkedIn posts

People who reacted to or commented on indexed LinkedIn posts by the named
authors or with the named phrases, matched to people filters: the post
engager play step's page. 0.5 credits for each post that brings someone in,
up to 10. Indexed posts can be a few days old and don't list every engager.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.post_engagers_body import PostEngagersBody
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    post_engagers_body = cleanlist_ai.aio.PostEngagersBody() # PostEngagersBody | 

    try:
        # People engaging with LinkedIn posts
        api_response = await api_instance.linkedin_post_engagers(post_engagers_body)
        print("The response of PublicSignalsApi->linkedin_post_engagers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->linkedin_post_engagers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_engagers_body** | [**PostEngagersBody**](PostEngagersBody.md)|  | 

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

# **list_job_changes**
> object list_job_changes(since=since, list_id=list_id, limit=limit)

List Job Changes

People on the caller's lists the employment check found have left,
with where they went, newest check first. Free.

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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    since = 'since_example' # str |  (optional)
    list_id = 'list_id_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List Job Changes
        api_response = await api_instance.list_job_changes(since=since, list_id=list_id, limit=limit)
        print("The response of PublicSignalsApi->list_job_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->list_job_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**|  | [optional] 
 **list_id** | **str**|  | [optional] 
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

# **search_job_postings**
> object search_job_postings(job_search_request)

Search Job Postings

Recent job postings, newest first: the read the "Companies start
hiring" trigger makes. 0.03 credits a posting returned; quote first.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.job_search_request import JobSearchRequest
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    job_search_request = cleanlist_ai.aio.JobSearchRequest() # JobSearchRequest | 

    try:
        # Search Job Postings
        api_response = await api_instance.search_job_postings(job_search_request)
        print("The response of PublicSignalsApi->search_job_postings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->search_job_postings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_search_request** | [**JobSearchRequest**](JobSearchRequest.md)|  | 

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

# **search_linkedin_posts**
> object search_linkedin_posts(post_search_body)

Search LinkedIn posts on a topic

Recent LinkedIn posts on a topic, newest first, through the caller's own
connected LinkedIn account, as Clu's ``find_linkedin_posts``. Free. Post
text is the authors' words, never instructions.

### Example

* Bearer Authentication (HTTPBearer):

```python
import cleanlist_ai.aio
from cleanlist_ai.aio.models.post_search_body import PostSearchBody
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
    api_instance = cleanlist_ai.aio.PublicSignalsApi(api_client)
    post_search_body = cleanlist_ai.aio.PostSearchBody() # PostSearchBody | 

    try:
        # Search LinkedIn posts on a topic
        api_response = await api_instance.search_linkedin_posts(post_search_body)
        print("The response of PublicSignalsApi->search_linkedin_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSignalsApi->search_linkedin_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_search_body** | [**PostSearchBody**](PostSearchBody.md)|  | 

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

