# ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed** | **bool** |  | [optional] [default to False]
**action** | **str** | agent_on, run_gtm_agent or run_play. | 
**description** | **str** |  | 
**credits_max** | **float** | The most it can spend. | 
**records_max** | **int** |  | [optional] 
**effects** | **List[str]** | What its plays can do outside Cleanlist: sends, crm_writes. | 
**required_scopes** | **List[str]** | The opt-in scopes a key needs to commit it. | 
**missing_scopes** | **List[str]** | Those this credential lacks; empty on the MCP. | 
**estimate** | **object** | The POST /credits/estimate body that quotes it. | 

## Example

```python
from cleanlist_ai.models.response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post import ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost from a JSON string
response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post_instance = ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost.from_json(json)
# print the JSON string representation of the object
print(ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost.to_json())

# convert the object into a dict
response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post_dict = response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post_instance.to_dict()
# create an instance of ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost from a dict
response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post_from_dict = ResponseRunGtmAgentApiV2GtmAgentsAgentIdRunsPost.from_dict(response_run_gtm_agent_api_v2_gtm_agents_agent_id_runs_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


