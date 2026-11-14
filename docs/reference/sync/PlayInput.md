# PlayInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**required** | **bool** |  | 

## Example

```python
from cleanlist_ai.models.play_input import PlayInput

# TODO update the JSON string below
json = "{}"
# create an instance of PlayInput from a JSON string
play_input_instance = PlayInput.from_json(json)
# print the JSON string representation of the object
print(PlayInput.to_json())

# convert the object into a dict
play_input_dict = play_input_instance.to_dict()
# create an instance of PlayInput from a dict
play_input_from_dict = PlayInput.from_dict(play_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


