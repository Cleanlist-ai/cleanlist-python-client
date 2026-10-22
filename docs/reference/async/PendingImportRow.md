# PendingImportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_person_id** | **str** | Imported RawPerson UUID, never a saved lead_id. | 
**status** | [**RawPersonStatus**](RawPersonStatus.md) |  | 
**source_row_index** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**company_domain** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.pending_import_row import PendingImportRow

# TODO update the JSON string below
json = "{}"
# create an instance of PendingImportRow from a JSON string
pending_import_row_instance = PendingImportRow.from_json(json)
# print the JSON string representation of the object
print(PendingImportRow.to_json())

# convert the object into a dict
pending_import_row_dict = pending_import_row_instance.to_dict()
# create an instance of PendingImportRow from a dict
pending_import_row_from_dict = PendingImportRow.from_dict(pending_import_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


