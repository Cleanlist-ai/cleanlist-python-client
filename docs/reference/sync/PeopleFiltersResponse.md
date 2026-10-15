# PeopleFiltersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**options** | [**List[FilterOption]**](FilterOption.md) |  | 

## Example

```python
from cleanlist_ai.models.people_filters_response import PeopleFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleFiltersResponse from a JSON string
people_filters_response_instance = PeopleFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(PeopleFiltersResponse.to_json())

# convert the object into a dict
people_filters_response_dict = people_filters_response_instance.to_dict()
# create an instance of PeopleFiltersResponse from a dict
people_filters_response_from_dict = PeopleFiltersResponse.from_dict(people_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


