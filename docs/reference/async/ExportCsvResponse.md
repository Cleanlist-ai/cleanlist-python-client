# ExportCsvResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | ID of the Lead List that was exported. | 
**download_url** | **str** | Time-limited, SAS-signed URL to download the generated CSV file. The signature (&#x60;sig&#x60;) and expiry (&#x60;exp&#x60;) query params gate access; the link stops working after &#x60;expires_at&#x60;. | 
**expires_at** | **str** | ISO-8601 UTC timestamp at which &#x60;download_url&#x60; expires. Generated URLs are valid for 24 hours. | 
**row_count** | **int** | Number of data rows written to the CSV (excludes the header row). | 
**file_size_bytes** | **int** | Size of the generated CSV file in bytes. | 

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


