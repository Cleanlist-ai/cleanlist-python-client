# CohortSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_namespace** | **str** |  | [optional] [default to 'unknown']
**population_scope** | **str** |  | [optional] [default to 'unknown']
**provider_total** | **int** |  | [optional] 
**returned_count** | **int** |  | [optional] 
**retained_count** | **int** | Unique IDs accessible through this task snapshot. | 
**evidence_checked_count** | **int** |  | [optional] 
**provider_has_more** | **bool** |  | [optional] 
**retention_truncated** | **bool** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.cohort_summary import CohortSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CohortSummary from a JSON string
cohort_summary_instance = CohortSummary.from_json(json)
# print the JSON string representation of the object
print(CohortSummary.to_json())

# convert the object into a dict
cohort_summary_dict = cohort_summary_instance.to_dict()
# create an instance of CohortSummary from a dict
cohort_summary_from_dict = CohortSummary.from_dict(cohort_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


