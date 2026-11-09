# ExportJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**list_id** | **str** | ID of the Lead List whose leads were returned. | 
**leads** | **List[Optional[object]]** | Page of lead rows returned inline, each projected to the selected (or default) columns. At most &#x60;limit&#x60; rows are returned per call. | 
**total** | **int** | Total number of rows in the list (across all pages), import rows not yet enriched included. | 
**cursor** | **str** |  | [optional] 
**skipped** | **int** | Rows of this page&#39;s place in the ordering that left the list (deleted or moved) after the cursor&#39;s ordering was taken, so the page holds fewer rows than it covers. &#x60;total&#x60; minus the sum of &#x60;skipped&#x60; over every page is the number of rows returned. | [optional] [default to 0]

## Example

```python
from cleanlist_ai.aio.models.export_json_response import ExportJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportJsonResponse from a JSON string
export_json_response_instance = ExportJsonResponse.from_json(json)
# print the JSON string representation of the object
print(ExportJsonResponse.to_json())

# convert the object into a dict
export_json_response_dict = export_json_response_instance.to_dict()
# create an instance of ExportJsonResponse from a dict
export_json_response_from_dict = ExportJsonResponse.from_dict(export_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


