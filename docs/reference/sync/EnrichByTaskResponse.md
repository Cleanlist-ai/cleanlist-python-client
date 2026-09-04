# EnrichByTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**entity_kind** | **str** | Resolved entity type of the task. &#39;person&#39; → async workflow; &#39;company&#39; → synchronous inline results. | 
**workflow_id** | **str** |  | [optional] 
**status** | **str** | &#39;pending&#39; for person tasks (workflow running); &#39;completed&#39; for company tasks (results already attached). | 
**total_entities** | **int** | Number of cohort entities dispatched for enrichment. | 
**credits_reserved** | **int** | Person tasks: upfront reservation cap; the workflow settles with actual usage and refunds the delta. Company tasks: the final billed amount (settled inline). | 
**results** | [**List[EnrichByTaskEntityResult]**](EnrichByTaskEntityResult.md) | Per-entity outcomes. Person tasks: all &#39;queued&#39;. Company tasks: &#39;enriched&#39;/&#39;skipped&#39;/&#39;failed&#39; with records attached. | 

## Example

```python
from cleanlist_ai.models.enrich_by_task_response import EnrichByTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichByTaskResponse from a JSON string
enrich_by_task_response_instance = EnrichByTaskResponse.from_json(json)
# print the JSON string representation of the object
print(EnrichByTaskResponse.to_json())

# convert the object into a dict
enrich_by_task_response_dict = enrich_by_task_response_instance.to_dict()
# create an instance of EnrichByTaskResponse from a dict
enrich_by_task_response_from_dict = EnrichByTaskResponse.from_dict(enrich_by_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


