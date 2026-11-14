# PlayDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playbook_id** | **str** |  | 
**agent_id** | **str** |  | 
**name** | **str** |  | 
**inputs** | [**List[PlayInput]**](PlayInput.md) |  | 

## Example

```python
from cleanlist_ai.models.play_dto import PlayDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayDto from a JSON string
play_dto_instance = PlayDto.from_json(json)
# print the JSON string representation of the object
print(PlayDto.to_json())

# convert the object into a dict
play_dto_dict = play_dto_instance.to_dict()
# create an instance of PlayDto from a dict
play_dto_from_dict = PlayDto.from_dict(play_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


