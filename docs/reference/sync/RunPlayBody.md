# RunPlayBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **object** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**commit** | **bool** | Run it. Without it, a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.run_play_body import RunPlayBody

# TODO update the JSON string below
json = "{}"
# create an instance of RunPlayBody from a JSON string
run_play_body_instance = RunPlayBody.from_json(json)
# print the JSON string representation of the object
print(RunPlayBody.to_json())

# convert the object into a dict
run_play_body_dict = run_play_body_instance.to_dict()
# create an instance of RunPlayBody from a dict
run_play_body_from_dict = RunPlayBody.from_dict(run_play_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


