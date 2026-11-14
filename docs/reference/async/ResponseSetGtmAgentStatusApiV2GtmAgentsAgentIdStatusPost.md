# ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization_id** | **str** |  | 
**owner_user_id** | **str** |  | 
**name** | **str** |  | 
**mark_color** | **str** |  | [optional] 
**description** | **str** |  | 
**goal** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**self_edit_instructions** | **bool** |  | 
**skill_refs** | [**List[SkillRefDto]**](SkillRefDto.md) |  | 
**knowledge** | [**KnowledgeDto**](KnowledgeDto.md) |  | 
**connections** | [**List[ConnectionDto]**](ConnectionDto.md) |  | 
**tools** | **Dict[str, bool]** |  | 
**triggers** | [**List[TriggerDto]**](TriggerDto.md) |  | 
**play_ids** | **List[str]** |  | 
**limits** | [**LimitsDto**](LimitsDto.md) |  | 
**cap_window** | **str** |  | [optional] 
**delivery** | [**DeliveryDto**](DeliveryDto.md) |  | 
**status** | **str** |  | 
**ai_managed_triggers** | **bool** |  | 
**is_favorite** | **bool** |  | 
**archived_at** | **str** |  | [optional] 
**version** | **int** |  | 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**next_run_at** | **str** |  | [optional] 
**last_run_at** | **str** |  | [optional] 
**pending_proposal_id** | **str** |  | [optional] 
**greeted_at** | **str** |  | [optional] 
**setup_completed_at** | **str** |  | [optional] 
**reopened_merges** | **int** |  | [optional] 
**blocked** | [**List[SettingsIssueDto]**](SettingsIssueDto.md) |  | [optional] 
**asks_first** | [**List[SettingsIssueDto]**](SettingsIssueDto.md) |  | [optional] 
**abilities_in_use** | **List[str]** |  | [optional] 
**play_connection_types** | **List[str]** |  | [optional] 
**app_blocks** | **Dict[str, Dict[str, str]]** |  | [optional] 
**gaps** | [**List[PlayGapDto]**](PlayGapDto.md) |  | [optional] 
**quick_replies** | **List[str]** |  | [optional] 
**built_from** | [**BuiltFromDto**](BuiltFromDto.md) |  | [optional] 
**committed** | **bool** |  | [optional] [default to False]
**action** | **str** | agent_on, run_gtm_agent or run_play. | 
**credits_max** | **float** | The most it can spend. | 
**records_max** | **int** |  | [optional] 
**effects** | **List[str]** | What its plays can do outside Cleanlist: sends, crm_writes. | 
**required_scopes** | **List[str]** | The opt-in scopes a key needs to commit it. | 
**missing_scopes** | **List[str]** | Those this credential lacks; empty on the MCP. | 
**estimate** | **object** | The POST /credits/estimate body that quotes it. | 

## Example

```python
from cleanlist_ai.aio.models.response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post import ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost from a JSON string
response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post_instance = ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost.from_json(json)
# print the JSON string representation of the object
print(ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost.to_json())

# convert the object into a dict
response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post_dict = response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post_instance.to_dict()
# create an instance of ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost from a dict
response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post_from_dict = ResponseSetGtmAgentStatusApiV2GtmAgentsAgentIdStatusPost.from_dict(response_set_gtm_agent_status_api_v2_gtm_agents_agent_id_status_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


