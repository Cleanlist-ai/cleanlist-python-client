# CsvImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**list_id** | **str** | Identifier of the list the CSV was imported into. | 
**rows_parsed** | **int** | Total data rows read from the CSV (excludes the header). | 
**rows_imported** | **int** | Rows that landed as importable contacts. | 
**rows_skipped** | **int** | Rows dropped during parsing (see skip_reasons). | 
**skip_reasons** | **Dict[str, Optional[int]]** | Skip counts by stable reason key (missing_required, duplicate_email, duplicate_linkedin, row_cap_exceeded). | [optional] 
**sample_skip_rows** | **List[Optional[int]]** | Up to 10 1-indexed row numbers (header is row 1) that were skipped, for spot-checking the file. | [optional] 
**workflow_id** | **str** |  | [optional] 
**enrichment_status_url** | **str** |  | [optional] 
**idempotency_replayed** | **bool** | True when served from the idempotency cache — the CSV was NOT re-imported and NO credits were re-charged. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.csv_import_response import CsvImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CsvImportResponse from a JSON string
csv_import_response_instance = CsvImportResponse.from_json(json)
# print the JSON string representation of the object
print(CsvImportResponse.to_json())

# convert the object into a dict
csv_import_response_dict = csv_import_response_instance.to_dict()
# create an instance of CsvImportResponse from a dict
csv_import_response_from_dict = CsvImportResponse.from_dict(csv_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


