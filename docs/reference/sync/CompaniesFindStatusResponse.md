# CompaniesFindStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**entity_kind** | **str** |  | [optional] [default to 'person']
**status** | **str** |  | 
**results** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] [default to 0]
**cursor** | **str** |  | [optional] 
**credits_charged** | **int** |  | [optional] [default to 0]
**resolved_company_count** | **int** |  | [optional] [default to 0]
**composite_warning** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.companies_find_status_response import CompaniesFindStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFindStatusResponse from a JSON string
companies_find_status_response_instance = CompaniesFindStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CompaniesFindStatusResponse.to_json())

# convert the object into a dict
companies_find_status_response_dict = companies_find_status_response_instance.to_dict()
# create an instance of CompaniesFindStatusResponse from a dict
companies_find_status_response_from_dict = CompaniesFindStatusResponse.from_dict(companies_find_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


