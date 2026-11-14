# TriggerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**schedule** | **object** |  | [optional] 
**note** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to True]
**last_fired_at** | **str** |  | [optional] 
**next_at** | **str** |  | [optional] 
**next_check_by** | **str** |  | [optional] 
**source** | **str** |  | 
**health** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.trigger_dto import TriggerDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDto from a JSON string
trigger_dto_instance = TriggerDto.from_json(json)
# print the JSON string representation of the object
print(TriggerDto.to_json())

# convert the object into a dict
trigger_dto_dict = trigger_dto_instance.to_dict()
# create an instance of TriggerDto from a dict
trigger_dto_from_dict = TriggerDto.from_dict(trigger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


