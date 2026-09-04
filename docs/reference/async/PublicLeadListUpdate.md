# PublicLeadListUpdate

PATCH body for renaming / re-describing / re-filing a list.  All fields optional but at least one must be supplied. PATCH semantics: only the fields PRESENT in the request change. A field set to ``null`` clears it (``description``) or unfiles the list (``folder_id``); a field omitted entirely is left untouched. The omitted-vs-explicit-null distinction is read from ``model_fields_set`` in the handler — which is exactly why ``extra=\"forbid\"`` matters here: an unknown key would otherwise land in that set and be mistaken for a real field change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.public_lead_list_update import PublicLeadListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLeadListUpdate from a JSON string
public_lead_list_update_instance = PublicLeadListUpdate.from_json(json)
# print the JSON string representation of the object
print(PublicLeadListUpdate.to_json())

# convert the object into a dict
public_lead_list_update_dict = public_lead_list_update_instance.to_dict()
# create an instance of PublicLeadListUpdate from a dict
public_lead_list_update_from_dict = PublicLeadListUpdate.from_dict(public_lead_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


