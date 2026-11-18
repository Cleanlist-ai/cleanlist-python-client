# BuiltFromDto

What the build kit built the agent's play from: a recipe (its title and slug), the org's saved skill (its name) or none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.built_from_dto import BuiltFromDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuiltFromDto from a JSON string
built_from_dto_instance = BuiltFromDto.from_json(json)
# print the JSON string representation of the object
print(BuiltFromDto.to_json())

# convert the object into a dict
built_from_dto_dict = built_from_dto_instance.to_dict()
# create an instance of BuiltFromDto from a dict
built_from_dto_from_dict = BuiltFromDto.from_dict(built_from_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


