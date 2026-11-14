# RunGtmAgentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playbook_id** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**commit** | **bool** | Start it. Without it, a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.run_gtm_agent_body import RunGtmAgentBody

# TODO update the JSON string below
json = "{}"
# create an instance of RunGtmAgentBody from a JSON string
run_gtm_agent_body_instance = RunGtmAgentBody.from_json(json)
# print the JSON string representation of the object
print(RunGtmAgentBody.to_json())

# convert the object into a dict
run_gtm_agent_body_dict = run_gtm_agent_body_instance.to_dict()
# create an instance of RunGtmAgentBody from a dict
run_gtm_agent_body_from_dict = RunGtmAgentBody.from_dict(run_gtm_agent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


