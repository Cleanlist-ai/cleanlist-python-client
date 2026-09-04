# RunSmartAgentResponse

Three identifiers can live on this response (T1-6 ID-space rename):  - `smart_agent_task_id` — canonical id for polling   `get_smart_agent_results`. - `smart_agent_task_ids` — dict keyed by column type when   `process_smart_columns` returns multiple underlying task ids. - `task_id` (from EnvelopeFields) — kept populated for back-compat   with v1.0 callers that read it from the envelope.  The three are distinct identifiers. A smart-column run's id is NOT an MCP cohort handle, but the envelope still carries `task_id` for transitional compat. New callers should read `smart_agent_task_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**smart_agent_task_id** | **str** | Canonical run id. Pass this to GET /smart-agents/{id} to poll progress and per-lead results. | 
**smart_agent_task_ids** | **Dict[str, str]** | Underlying task ids keyed by column type. Usually a single entry; populated when the run fans out to more than one smart-column task. | [optional] 
**status** | **str** | Initial run status; always &#39;pending&#39; at launch. | 
**list_id** | **str** | UUID of the lead list the run was launched against. | 
**column_name** | **str** | Name of the column that will hold each lead&#39;s output. | 
**estimated_cost** | **int** | Credits expected for this run (per-lead rate × row count). Actual debit happens as rows complete and may be lower if leads fail. | 

## Example

```python
from cleanlist_ai.models.run_smart_agent_response import RunSmartAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunSmartAgentResponse from a JSON string
run_smart_agent_response_instance = RunSmartAgentResponse.from_json(json)
# print the JSON string representation of the object
print(RunSmartAgentResponse.to_json())

# convert the object into a dict
run_smart_agent_response_dict = run_smart_agent_response_instance.to_dict()
# create an instance of RunSmartAgentResponse from a dict
run_smart_agent_response_from_dict = RunSmartAgentResponse.from_dict(run_smart_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


