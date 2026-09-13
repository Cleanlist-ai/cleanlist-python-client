# SmartAgentResultRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **str** | UUID of the lead this result row belongs to. | 
**value** | **object** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.smart_agent_result_row import SmartAgentResultRow

# TODO update the JSON string below
json = "{}"
# create an instance of SmartAgentResultRow from a JSON string
smart_agent_result_row_instance = SmartAgentResultRow.from_json(json)
# print the JSON string representation of the object
print(SmartAgentResultRow.to_json())

# convert the object into a dict
smart_agent_result_row_dict = smart_agent_result_row_instance.to_dict()
# create an instance of SmartAgentResultRow from a dict
smart_agent_result_row_from_dict = SmartAgentResultRow.from_dict(smart_agent_result_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


