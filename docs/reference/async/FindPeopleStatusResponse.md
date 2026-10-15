# FindPeopleStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**workflow_id** | **str** |  | 
**status** | **str** |  | 
**people_found** | **int** |  | [optional] 
**people_imported** | **int** |  | [optional] 
**credits_used** | **float** |  | [optional] 
**lead_ids** | **List[str]** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.find_people_status_response import FindPeopleStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindPeopleStatusResponse from a JSON string
find_people_status_response_instance = FindPeopleStatusResponse.from_json(json)
# print the JSON string representation of the object
print(FindPeopleStatusResponse.to_json())

# convert the object into a dict
find_people_status_response_dict = find_people_status_response_instance.to_dict()
# create an instance of FindPeopleStatusResponse from a dict
find_people_status_response_from_dict = FindPeopleStatusResponse.from_dict(find_people_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


