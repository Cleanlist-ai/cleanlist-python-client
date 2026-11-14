# PlayEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**status** | **str** | pending (waiting for a run), claimed (a run is starting), seeded (in its run), rejected or expired. | 
**run_id** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.play_event_dto import PlayEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayEventDto from a JSON string
play_event_dto_instance = PlayEventDto.from_json(json)
# print the JSON string representation of the object
print(PlayEventDto.to_json())

# convert the object into a dict
play_event_dto_dict = play_event_dto_instance.to_dict()
# create an instance of PlayEventDto from a dict
play_event_dto_from_dict = PlayEventDto.from_dict(play_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


