# PersonRefDto

A member a connection names: first name (else email), and whether they have left the organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** |  | 
**left** | **bool** |  | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.person_ref_dto import PersonRefDto

# TODO update the JSON string below
json = "{}"
# create an instance of PersonRefDto from a JSON string
person_ref_dto_instance = PersonRefDto.from_json(json)
# print the JSON string representation of the object
print(PersonRefDto.to_json())

# convert the object into a dict
person_ref_dto_dict = person_ref_dto_instance.to_dict()
# create an instance of PersonRefDto from a dict
person_ref_dto_from_dict = PersonRefDto.from_dict(person_ref_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


