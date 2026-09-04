# EnrichByTaskEntityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The cohort entity id this result belongs to. | 
**status** | **str** | Per-entity outcome. Person tasks return &#39;queued&#39; (results land asynchronously). Company tasks return &#39;enriched&#39; (record attached), &#39;skipped&#39; (no cached identifier), or &#39;failed&#39; (lookup error / not found). | 
**error** | **str** |  | [optional] 
**company** | [**CompanyRecord**](CompanyRecord.md) |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.enrich_by_task_entity_result import EnrichByTaskEntityResult

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichByTaskEntityResult from a JSON string
enrich_by_task_entity_result_instance = EnrichByTaskEntityResult.from_json(json)
# print the JSON string representation of the object
print(EnrichByTaskEntityResult.to_json())

# convert the object into a dict
enrich_by_task_entity_result_dict = enrich_by_task_entity_result_instance.to_dict()
# create an instance of EnrichByTaskEntityResult from a dict
enrich_by_task_entity_result_from_dict = EnrichByTaskEntityResult.from_dict(enrich_by_task_entity_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


