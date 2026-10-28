# BulkContactResult

One contact of a bulk run, returned when polling with `include_results=true`. `lead` is the same row `GET /lead-lists/{id}/leads` returns, so contact fields follow the same reveal rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position of this contact in the run. | 
**status** | **str** | pending / processing / completed / failed while known; &#39;unavailable&#39; once the per-contact record has expired (24h). | 
**failure_class** | **str** |  | [optional] 
**lead** | [**LeadRow**](LeadRow.md) |  | [optional] 

## Example

```python
from cleanlist_ai.models.bulk_contact_result import BulkContactResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkContactResult from a JSON string
bulk_contact_result_instance = BulkContactResult.from_json(json)
# print the JSON string representation of the object
print(BulkContactResult.to_json())

# convert the object into a dict
bulk_contact_result_dict = bulk_contact_result_instance.to_dict()
# create an instance of BulkContactResult from a dict
bulk_contact_result_from_dict = BulkContactResult.from_dict(bulk_contact_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


