# FindPeopleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_ids** | **List[str]** | Cleanlist company ids to find people at. Must be companies already in the list: read them from the &#x60;company_id&#x60; of the list&#39;s lead rows (GET /lead-lists/{list_id}/leads). Ids outside the list are dropped. | 
**job_titles** | **List[str]** |  | [optional] 
**seniority_levels** | **List[str]** |  | [optional] 
**limit_per_company** | **int** |  | [optional] [default to 5]
**location_state** | **str** |  | [optional] 
**location_country** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.find_people_request import FindPeopleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindPeopleRequest from a JSON string
find_people_request_instance = FindPeopleRequest.from_json(json)
# print the JSON string representation of the object
print(FindPeopleRequest.to_json())

# convert the object into a dict
find_people_request_dict = find_people_request_instance.to_dict()
# create an instance of FindPeopleRequest from a dict
find_people_request_from_dict = FindPeopleRequest.from_dict(find_people_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


