# CreateGtmAgentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**settings** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.create_gtm_agent_body import CreateGtmAgentBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGtmAgentBody from a JSON string
create_gtm_agent_body_instance = CreateGtmAgentBody.from_json(json)
# print the JSON string representation of the object
print(CreateGtmAgentBody.to_json())

# convert the object into a dict
create_gtm_agent_body_dict = create_gtm_agent_body_instance.to_dict()
# create an instance of CreateGtmAgentBody from a dict
create_gtm_agent_body_from_dict = CreateGtmAgentBody.from_dict(create_gtm_agent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


