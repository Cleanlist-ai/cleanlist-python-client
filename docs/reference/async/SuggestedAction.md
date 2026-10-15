# SuggestedAction

A follow-up suggestion the agent can present or call directly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**tool** | **str** |  | [optional] 
**arguments** | **object** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.suggested_action import SuggestedAction

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedAction from a JSON string
suggested_action_instance = SuggestedAction.from_json(json)
# print the JSON string representation of the object
print(SuggestedAction.to_json())

# convert the object into a dict
suggested_action_dict = suggested_action_instance.to_dict()
# create an instance of SuggestedAction from a dict
suggested_action_from_dict = SuggestedAction.from_dict(suggested_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


