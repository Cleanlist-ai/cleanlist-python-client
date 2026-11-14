# GtmAgentStatusBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**quote_id** | **str** |  | [optional] 
**commit** | **bool** | On only: turn it on. Without it, the call is a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.gtm_agent_status_body import GtmAgentStatusBody

# TODO update the JSON string below
json = "{}"
# create an instance of GtmAgentStatusBody from a JSON string
gtm_agent_status_body_instance = GtmAgentStatusBody.from_json(json)
# print the JSON string representation of the object
print(GtmAgentStatusBody.to_json())

# convert the object into a dict
gtm_agent_status_body_dict = gtm_agent_status_body_instance.to_dict()
# create an instance of GtmAgentStatusBody from a dict
gtm_agent_status_body_from_dict = GtmAgentStatusBody.from_dict(gtm_agent_status_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


