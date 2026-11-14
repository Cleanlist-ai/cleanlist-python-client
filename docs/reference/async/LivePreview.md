# LivePreview

What a live call would do, sent back without ``commit``: nothing ran and no quote was used.

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
from cleanlist_ai.aio.models.live_preview import LivePreview

# TODO update the JSON string below
json = "{}"
# create an instance of LivePreview from a JSON string
live_preview_instance = LivePreview.from_json(json)
# print the JSON string representation of the object
print(LivePreview.to_json())

# convert the object into a dict
live_preview_dict = live_preview_instance.to_dict()
# create an instance of LivePreview from a dict
live_preview_from_dict = LivePreview.from_dict(live_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


