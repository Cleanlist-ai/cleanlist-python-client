# CompaniesFindStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | 
**poll_url** | **str** |  | 

## Example

```python
from cleanlist_ai.aio.models.companies_find_start_response import CompaniesFindStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFindStartResponse from a JSON string
companies_find_start_response_instance = CompaniesFindStartResponse.from_json(json)
# print the JSON string representation of the object
print(CompaniesFindStartResponse.to_json())

# convert the object into a dict
companies_find_start_response_dict = companies_find_start_response_instance.to_dict()
# create an instance of CompaniesFindStartResponse from a dict
companies_find_start_response_from_dict = CompaniesFindStartResponse.from_dict(companies_find_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


