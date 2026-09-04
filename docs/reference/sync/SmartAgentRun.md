# SmartAgentRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Run id for this smart-agent run — poll it via GET /smart-agents/{id}. | 
**list_id** | **str** | UUID of the lead list this run targeted. | 
**column_name** | **str** | Name of the column the run wrote its output to. | 
**agent_type** | **str** | Agent / smart-column type the run executed as (e.g. &#x60;custom_ai&#x60;, &#x60;cold_intro_email&#x60;). | 
**status** | **str** | Lifecycle state: &#x60;pending&#x60;, &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;failed&#x60;. | 
**total** | **int** | Total leads scheduled for this run. | [optional] [default to 0]
**processed** | **int** | Leads processed so far (succeeded + failed). | [optional] [default to 0]
**failed** | **int** | Leads that errored during processing. | [optional] [default to 0]
**created_at** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.smart_agent_run import SmartAgentRun

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAgentRun from a JSON string
smart_agent_run_instance = SmartAgentRun.from_json(json)
# print the JSON string representation of the object
print(SmartAgentRun.to_json())

# convert the object into a dict
smart_agent_run_dict = smart_agent_run_instance.to_dict()
# create an instance of SmartAgentRun from a dict
smart_agent_run_from_dict = SmartAgentRun.from_dict(smart_agent_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


