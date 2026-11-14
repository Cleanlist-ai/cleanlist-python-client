# ActionCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **object** |  | [optional] 
**session_id** | **str** |  | [optional] 
**commit** | **bool** | Code callers only: confirm the card in the same call. Without it a card is a preview and nothing runs. | [optional] [default to False]

## Example

```python
from cleanlist_ai.aio.models.action_call import ActionCall

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCall from a JSON string
action_call_instance = ActionCall.from_json(json)
# print the JSON string representation of the object
print(ActionCall.to_json())

# convert the object into a dict
action_call_dict = action_call_instance.to_dict()
# create an instance of ActionCall from a dict
action_call_from_dict = ActionCall.from_dict(action_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


