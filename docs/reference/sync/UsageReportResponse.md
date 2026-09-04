# UsageReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Length of the reporting window in days (as requested). | 
**group_by** | **str** | Dimension the rows are grouped by: &#x60;tool&#x60;, &#x60;key&#x60;, &#x60;day&#x60;, or &#x60;error&#x60;. | 
**total_calls** | **int** | Total API calls across all buckets in the window. | 
**total_credits_spent** | **float** | Total credits spent across all buckets. Currently 0.0 until the request log gains a per-row cost column. | 
**total_errors** | **int** | Total error (non-2xx) responses across all buckets. | 
**rows** | [**List[UsageGroupRow]**](UsageGroupRow.md) | Per-bucket usage rows for the requested &#x60;group_by&#x60; dimension. | 

## Example

```python
from cleanlist_ai.models.usage_report_response import UsageReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportResponse from a JSON string
usage_report_response_instance = UsageReportResponse.from_json(json)
# print the JSON string representation of the object
print(UsageReportResponse.to_json())

# convert the object into a dict
usage_report_response_dict = usage_report_response_instance.to_dict()
# create an instance of UsageReportResponse from a dict
usage_report_response_from_dict = UsageReportResponse.from_dict(usage_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


