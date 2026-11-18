# PlayGapDto

What one of the agent's saved plays doesn't do yet (``play_completeness``, CLE-478): its code, Clu's line, why (CRM sync off: not_added, not_connected, disconnected, declined) and the reply that asks Clu to propose the fix (none once declined).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**reason** | **str** |  | [optional] 
**quick_reply** | **str** |  | [optional] 
**play_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.play_gap_dto import PlayGapDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayGapDto from a JSON string
play_gap_dto_instance = PlayGapDto.from_json(json)
# print the JSON string representation of the object
print(PlayGapDto.to_json())

# convert the object into a dict
play_gap_dto_dict = play_gap_dto_instance.to_dict()
# create an instance of PlayGapDto from a dict
play_gap_dto_from_dict = PlayGapDto.from_dict(play_gap_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


