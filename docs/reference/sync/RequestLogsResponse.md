# RequestLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[RequestLogRow]**](RequestLogRow.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.request_logs_response import RequestLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLogsResponse from a JSON string
request_logs_response_instance = RequestLogsResponse.from_json(json)
# print the JSON string representation of the object
print(RequestLogsResponse.to_json())

# convert the object into a dict
request_logs_response_dict = request_logs_response_instance.to_dict()
# create an instance of RequestLogsResponse from a dict
request_logs_response_from_dict = RequestLogsResponse.from_dict(request_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


