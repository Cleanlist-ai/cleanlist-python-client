# LeadRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **str** | Stable lead identifier. Reusable as an add/remove lead_id. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.lead_row import LeadRow

# TODO update the JSON string below
json = "{}"
# create an instance of LeadRow from a JSON string
lead_row_instance = LeadRow.from_json(json)
# print the JSON string representation of the object
print(LeadRow.to_json())

# convert the object into a dict
lead_row_dict = lead_row_instance.to_dict()
# create an instance of LeadRow from a dict
lead_row_from_dict = LeadRow.from_dict(lead_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


