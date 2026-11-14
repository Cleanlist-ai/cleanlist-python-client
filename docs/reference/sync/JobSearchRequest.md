# JobSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**titles** | **List[str]** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**company_domains** | **List[str]** |  | [optional] 
**company_criteria** | **object** |  | [optional] 
**locations** | **List[str]** |  | [optional] 
**posted_within_days** | **int** |  | [optional] 
**limit** | **int** | Postings at most, 1 to 10000. | [optional] [default to 25]
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.job_search_request import JobSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobSearchRequest from a JSON string
job_search_request_instance = JobSearchRequest.from_json(json)
# print the JSON string representation of the object
print(JobSearchRequest.to_json())

# convert the object into a dict
job_search_request_dict = job_search_request_instance.to_dict()
# create an instance of JobSearchRequest from a dict
job_search_request_from_dict = JobSearchRequest.from_dict(job_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


