# SkillRefDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from cleanlist_ai.aio.models.skill_ref_dto import SkillRefDto

# TODO update the JSON string below
json = "{}"
# create an instance of SkillRefDto from a JSON string
skill_ref_dto_instance = SkillRefDto.from_json(json)
# print the JSON string representation of the object
print(SkillRefDto.to_json())

# convert the object into a dict
skill_ref_dto_dict = skill_ref_dto_instance.to_dict()
# create an instance of SkillRefDto from a dict
skill_ref_dto_from_dict = SkillRefDto.from_dict(skill_ref_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


