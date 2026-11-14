# BatchRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | The item&#39;s index in the request. | 
**status** | **str** |  | 
**entity_id** | **str** |  | [optional] 
**result_index** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**company** | [**CompanyRecord**](CompanyRecord.md) |  | [optional] 

## Example

```python
from cleanlist_ai.models.batch_row import BatchRow

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRow from a JSON string
batch_row_instance = BatchRow.from_json(json)
# print the JSON string representation of the object
print(BatchRow.to_json())

# convert the object into a dict
batch_row_dict = batch_row_instance.to_dict()
# create an instance of BatchRow from a dict
batch_row_from_dict = BatchRow.from_dict(batch_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


