# RequestLogRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time** | **datetime** |  | 
**method** | **str** |  | 
**path** | **str** |  | 
**status** | **int** |  | 
**duration_ms** | **int** |  | 
**tool** | **str** |  | [optional] 
**credits** | **float** |  | 
**key_prefix** | **str** |  | [optional] 
**client** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.request_log_row import RequestLogRow

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLogRow from a JSON string
request_log_row_instance = RequestLogRow.from_json(json)
# print the JSON string representation of the object
print(RequestLogRow.to_json())

# convert the object into a dict
request_log_row_dict = request_log_row_instance.to_dict()
# create an instance of RequestLogRow from a dict
request_log_row_from_dict = RequestLogRow.from_dict(request_log_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


