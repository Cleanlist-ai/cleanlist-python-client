# JobChangeCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_ids** | **List[str]** |  | [optional] 
**linkedin_urls** | **List[str]** |  | [optional] 
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.job_change_check_request import JobChangeCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobChangeCheckRequest from a JSON string
job_change_check_request_instance = JobChangeCheckRequest.from_json(json)
# print the JSON string representation of the object
print(JobChangeCheckRequest.to_json())

# convert the object into a dict
job_change_check_request_dict = job_change_check_request_instance.to_dict()
# create an instance of JobChangeCheckRequest from a dict
job_change_check_request_from_dict = JobChangeCheckRequest.from_dict(job_change_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


