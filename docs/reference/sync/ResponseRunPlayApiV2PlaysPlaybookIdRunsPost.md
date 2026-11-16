# ResponseRunPlayApiV2PlaysPlaybookIdRunsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | [optional] 
**queued** | **bool** |  | [optional] [default to False]
**reason** | **str** |  | [optional] 
**event_id** | **str** | The record&#39;s event. While queued, GET /plays/{playbook_id}/events/{event_id} answers its run_id once a run takes it. | 
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
from cleanlist_ai.models.response_run_play_api_v2_plays_playbook_id_runs_post import ResponseRunPlayApiV2PlaysPlaybookIdRunsPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseRunPlayApiV2PlaysPlaybookIdRunsPost from a JSON string
response_run_play_api_v2_plays_playbook_id_runs_post_instance = ResponseRunPlayApiV2PlaysPlaybookIdRunsPost.from_json(json)
# print the JSON string representation of the object
print(ResponseRunPlayApiV2PlaysPlaybookIdRunsPost.to_json())

# convert the object into a dict
response_run_play_api_v2_plays_playbook_id_runs_post_dict = response_run_play_api_v2_plays_playbook_id_runs_post_instance.to_dict()
# create an instance of ResponseRunPlayApiV2PlaysPlaybookIdRunsPost from a dict
response_run_play_api_v2_plays_playbook_id_runs_post_from_dict = ResponseRunPlayApiV2PlaysPlaybookIdRunsPost.from_dict(response_run_play_api_v2_plays_playbook_id_runs_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


