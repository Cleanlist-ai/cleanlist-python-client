# AgentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization_id** | **str** |  | 
**owner_user_id** | **str** |  | 
**name** | **str** |  | 
**mark_color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
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

## Example

```python
from cleanlist_ai.models.agent_dto import AgentDto

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDto from a JSON string
agent_dto_instance = AgentDto.from_json(json)
# print the JSON string representation of the object
print(AgentDto.to_json())

# convert the object into a dict
agent_dto_dict = agent_dto_instance.to_dict()
# create an instance of AgentDto from a dict
agent_dto_from_dict = AgentDto.from_dict(agent_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


