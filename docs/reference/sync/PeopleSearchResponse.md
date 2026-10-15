# PeopleSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**entity_kind** | **str** |  | [optional] [default to 'person']
**search_handoff** | [**SearchHandoff**](SearchHandoff.md) |  | [optional] 
**route** | **object** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**exclusions_applied** | **Dict[str, int]** |  | [optional] 
**results** | [**List[PeopleSearchResultRow]**](PeopleSearchResultRow.md) |  | 
**total** | **int** |  | 
**cursor** | **str** |  | [optional] 
**credits_charged** | **int** |  | 
**truncation_warning** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.people_search_response import PeopleSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearchResponse from a JSON string
people_search_response_instance = PeopleSearchResponse.from_json(json)
# print the JSON string representation of the object
print(PeopleSearchResponse.to_json())

# convert the object into a dict
people_search_response_dict = people_search_response_instance.to_dict()
# create an instance of PeopleSearchResponse from a dict
people_search_response_from_dict = PeopleSearchResponse.from_dict(people_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


