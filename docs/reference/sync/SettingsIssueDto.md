# SettingsIssueDto

A step of one of the agent's plays under the agent's settings (``tool_policy.play_findings``): blocked, or asking someone first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_id** | **str** |  | 
**node_id** | **str** |  | [optional] 
**code** | **str** |  | 
**message** | **str** |  | 
**fix** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**connection** | **str** |  | [optional] 
**approver** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.settings_issue_dto import SettingsIssueDto

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsIssueDto from a JSON string
settings_issue_dto_instance = SettingsIssueDto.from_json(json)
# print the JSON string representation of the object
print(SettingsIssueDto.to_json())

# convert the object into a dict
settings_issue_dto_dict = settings_issue_dto_instance.to_dict()
# create an instance of SettingsIssueDto from a dict
settings_issue_dto_from_dict = SettingsIssueDto.from_dict(settings_issue_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


