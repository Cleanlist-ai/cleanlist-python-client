# ListSmartAgentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**runs** | [**List[SmartAgentRun]**](SmartAgentRun.md) | Smart-agent runs, most recent first, scoped to what the caller can see (a single list when &#x60;list_id&#x60; is passed, else a rollup across accessible lists). | 
**total** | **int** | Number of runs returned in &#x60;runs&#x60; (bounded by &#x60;limit&#x60;). | 

## Example

```python
from cleanlist_ai.aio.models.list_smart_agents_response import ListSmartAgentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSmartAgentsResponse from a JSON string
list_smart_agents_response_instance = ListSmartAgentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSmartAgentsResponse.to_json())

# convert the object into a dict
list_smart_agents_response_dict = list_smart_agents_response_instance.to_dict()
# create an instance of ListSmartAgentsResponse from a dict
list_smart_agents_response_from_dict = ListSmartAgentsResponse.from_dict(list_smart_agents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


