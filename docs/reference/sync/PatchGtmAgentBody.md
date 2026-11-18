# PatchGtmAgentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**settings** | **object** |  | [optional] 
**schedule** | **object** |  | [optional] 
**playbook_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.patch_gtm_agent_body import PatchGtmAgentBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchGtmAgentBody from a JSON string
patch_gtm_agent_body_instance = PatchGtmAgentBody.from_json(json)
# print the JSON string representation of the object
print(PatchGtmAgentBody.to_json())

# convert the object into a dict
patch_gtm_agent_body_dict = patch_gtm_agent_body_instance.to_dict()
# create an instance of PatchGtmAgentBody from a dict
patch_gtm_agent_body_from_dict = PatchGtmAgentBody.from_dict(patch_gtm_agent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


