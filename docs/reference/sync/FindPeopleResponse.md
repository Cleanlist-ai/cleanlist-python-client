# FindPeopleResponse


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
**total_companies** | **int** |  | 
**estimated_credits** | **float** |  | 
**lead_list_id** | **str** |  | 
**poll_url** | **str** |  | 

## Example

```python
from cleanlist_ai.models.find_people_response import FindPeopleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindPeopleResponse from a JSON string
find_people_response_instance = FindPeopleResponse.from_json(json)
# print the JSON string representation of the object
print(FindPeopleResponse.to_json())

# convert the object into a dict
find_people_response_dict = find_people_response_instance.to_dict()
# create an instance of FindPeopleResponse from a dict
find_people_response_from_dict = FindPeopleResponse.from_dict(find_people_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


