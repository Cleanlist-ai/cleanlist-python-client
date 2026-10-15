# PeopleSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **object** |  | [optional] 
**criteria** | [**PeopleSearchCriteria**](PeopleSearchCriteria.md) |  | [optional] 
**company_criteria** | [**CompanySearchCriteria**](CompanySearchCriteria.md) |  | [optional] 
**crm** | **str** |  | [optional] 
**limit** | **int** | Maximum rows for this response. When criteria.maxResults is explicitly provided, the smaller of the two limits applies. Continuation pages are separate. | [optional] [default to 25]
**cursor** | **str** |  | [optional] 
**sort** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.people_search_request import PeopleSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearchRequest from a JSON string
people_search_request_instance = PeopleSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PeopleSearchRequest.to_json())

# convert the object into a dict
people_search_request_dict = people_search_request_instance.to_dict()
# create an instance of PeopleSearchRequest from a dict
people_search_request_from_dict = PeopleSearchRequest.from_dict(people_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


