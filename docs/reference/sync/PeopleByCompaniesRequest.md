# PeopleByCompaniesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_filter** | **object** |  | [optional] 
**company_linkedin_urls** | **List[str]** |  | [optional] 
**person_filter** | **object** | Required PersonDB filter blob (same shape as /people/find). AND-ed with the resolved company set. | 
**limit** | **int** |  | [optional] [default to 100]
**cursor** | **str** |  | [optional] 
**sorts** | **List[Optional[object]]** |  | [optional] 
**post_processing** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.models.people_by_companies_request import PeopleByCompaniesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleByCompaniesRequest from a JSON string
people_by_companies_request_instance = PeopleByCompaniesRequest.from_json(json)
# print the JSON string representation of the object
print(PeopleByCompaniesRequest.to_json())

# convert the object into a dict
people_by_companies_request_dict = people_by_companies_request_instance.to_dict()
# create an instance of PeopleByCompaniesRequest from a dict
people_by_companies_request_from_dict = PeopleByCompaniesRequest.from_dict(people_by_companies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


