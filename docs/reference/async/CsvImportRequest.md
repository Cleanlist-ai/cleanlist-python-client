# CsvImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_content_base64** | **str** | Full CSV file body, base64-encoded. UTF-8 (with or without BOM). v1 hard-caps the raw body at 150 KB / ~600 rows — past that the base64 payload starts hitting tool-call output limits in the agent before any server cap fires. Above the cap the endpoint returns 413; chunk the file upstream. | 
**column_mapping** | **Dict[str, Optional[str]]** | { canonical_field: csv_header_name }. The MCP agent reads the CSV header line and supplies the mapping; the server never guesses. CSV columns not mapped are dropped. Mapping a field that isn&#39;t in the CSV header returns 400 missing_column with the bad header name in &#x60;details&#x60;. | 
**dispatch_enrichment** | **bool** | When True (default), the import dispatches a BulkEnrichmentWorkflow immediately after the RawPeople rows land. When False, rows land as RawPerson(status&#x3D;pending) and the caller dispatches enrichment separately via enrich_list. | [optional] [default to True]
**enrichment_type** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.csv_import_request import CsvImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvImportRequest from a JSON string
csv_import_request_instance = CsvImportRequest.from_json(json)
# print the JSON string representation of the object
print(CsvImportRequest.to_json())

# convert the object into a dict
csv_import_request_dict = csv_import_request_instance.to_dict()
# create an instance of CsvImportRequest from a dict
csv_import_request_from_dict = CsvImportRequest.from_dict(csv_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


