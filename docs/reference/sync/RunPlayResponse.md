# RunPlayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | [optional] 
**queued** | **bool** |  | [optional] [default to False]
**reason** | **str** |  | [optional] 
**event_id** | **str** | The record&#39;s event. While queued, GET /plays/{playbook_id}/events/{event_id} answers its run_id once a run takes it. | 

## Example

```python
from cleanlist_ai.models.run_play_response import RunPlayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunPlayResponse from a JSON string
run_play_response_instance = RunPlayResponse.from_json(json)
# print the JSON string representation of the object
print(RunPlayResponse.to_json())

# convert the object into a dict
run_play_response_dict = run_play_response_instance.to_dict()
# create an instance of RunPlayResponse from a dict
run_play_response_from_dict = RunPlayResponse.from_dict(run_play_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


