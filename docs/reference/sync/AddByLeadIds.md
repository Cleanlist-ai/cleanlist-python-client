# AddByLeadIds

Mode A: add already-materialized leads by UUID.  These come from `list_leads_in_list` (real lead UUIDs) or a list already owned by the workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_ids** | **List[str]** | Lead UUIDs to add (from list_leads_in_list / an owned list). | 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.add_by_lead_ids import AddByLeadIds

# TODO update the JSON string below
json = "{}"
# create an instance of AddByLeadIds from a JSON string
add_by_lead_ids_instance = AddByLeadIds.from_json(json)
# print the JSON string representation of the object
print(AddByLeadIds.to_json())

# convert the object into a dict
add_by_lead_ids_dict = add_by_lead_ids_instance.to_dict()
# create an instance of AddByLeadIds from a dict
add_by_lead_ids_from_dict = AddByLeadIds.from_dict(add_by_lead_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


