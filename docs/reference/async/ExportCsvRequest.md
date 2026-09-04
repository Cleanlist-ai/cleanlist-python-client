# ExportCsvRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | ID of the Lead List to export. Must be a list your API key is authorized to read. | 
**columns** | **List[str]** |  | [optional] 
**include_smart_agents** | **bool** | Append the list&#39;s configured smart-agent result columns after the selected columns. Set false to export only the base columns. | [optional] [default to True]

## Example

```python
from cleanlist_ai.aio.models.export_csv_request import ExportCsvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCsvRequest from a JSON string
export_csv_request_instance = ExportCsvRequest.from_json(json)
# print the JSON string representation of the object
print(ExportCsvRequest.to_json())

# convert the object into a dict
export_csv_request_dict = export_csv_request_instance.to_dict()
# create an instance of ExportCsvRequest from a dict
export_csv_request_from_dict = ExportCsvRequest.from_dict(export_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


