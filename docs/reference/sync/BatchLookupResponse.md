# BatchLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | 
**total_rows** | **int** |  | 
**accepted_rows** | **int** |  | 
**workflow_id** | **str** |  | [optional] 
**list_id** | **str** |  | [optional] 
**credits_reserved** | **int** |  | [optional] [default to 0]
**credits_charged** | **int** |  | [optional] 
**read_back_url** | **str** |  | [optional] 
**poll_url** | **str** |  | [optional] 
**rows** | [**List[BatchRow]**](BatchRow.md) |  | 

## Example

```python
from cleanlist_ai.models.batch_lookup_response import BatchLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLookupResponse from a JSON string
batch_lookup_response_instance = BatchLookupResponse.from_json(json)
# print the JSON string representation of the object
print(BatchLookupResponse.to_json())

# convert the object into a dict
batch_lookup_response_dict = batch_lookup_response_instance.to_dict()
# create an instance of BatchLookupResponse from a dict
batch_lookup_response_from_dict = BatchLookupResponse.from_dict(batch_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


