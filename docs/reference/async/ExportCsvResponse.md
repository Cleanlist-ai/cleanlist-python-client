# ExportCsvResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | ID of the Lead List that was exported. | 
**job_id** | **str** |  | [optional] 
**status** | **str** | &#x60;completed&#x60; with a &#x60;download_url&#x60;, or &#x60;running&#x60; (HTTP 202): call again with &#x60;job_id&#x60;. | [optional] [default to 'completed']
**download_url** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**row_count** | **int** | Number of data rows written to the CSV (excludes the header row); while running, the rows being exported. | 
**file_size_bytes** | **int** |  | [optional] 
**skipped_count** | **int** | Rows of the list that changed while it was exporting (deleted, or merged into another row) and are not in the file. &#x60;row_count&#x60; + &#x60;skipped_count&#x60; is the list&#39;s row count when the export started. | [optional] [default to 0]

## Example

```python
from cleanlist_ai.aio.models.export_csv_response import ExportCsvResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCsvResponse from a JSON string
export_csv_response_instance = ExportCsvResponse.from_json(json)
# print the JSON string representation of the object
print(ExportCsvResponse.to_json())

# convert the object into a dict
export_csv_response_dict = export_csv_response_instance.to_dict()
# create an instance of ExportCsvResponse from a dict
export_csv_response_from_dict = ExportCsvResponse.from_dict(export_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


