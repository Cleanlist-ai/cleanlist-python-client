# SmartAgentResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**smart_agent_task_id** | **str** | The run id being polled (echoes the path parameter). | 
**status** | **str** | Run lifecycle state: &#x60;pending&#x60;, &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;failed&#x60;. | 
**progress** | **int** | Percent complete (0–100), derived from processed / total. | 
**total** | **int** | Total leads scheduled for this run. | 
**succeeded** | **int** | Leads that produced a value without error. | 
**failed** | **int** | Leads that errored during processing. | 
**results** | [**List[SmartAgentResultRow]**](SmartAgentResultRow.md) | Per-lead output rows attributed to this run. May be empty while the run is still starting up. | 

## Example

```python
from cleanlist_ai.models.smart_agent_results_response import SmartAgentResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAgentResultsResponse from a JSON string
smart_agent_results_response_instance = SmartAgentResultsResponse.from_json(json)
# print the JSON string representation of the object
print(SmartAgentResultsResponse.to_json())

# convert the object into a dict
smart_agent_results_response_dict = smart_agent_results_response_instance.to_dict()
# create an instance of SmartAgentResultsResponse from a dict
smart_agent_results_response_from_dict = SmartAgentResultsResponse.from_dict(smart_agent_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


