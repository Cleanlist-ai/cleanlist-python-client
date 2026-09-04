# EnrichPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**workflow_id** | **str** | Handle for the async enrichment workflow. Poll it via poll_url. | 
**status** | **str** | Always &#39;pending&#39; on dispatch — the workflow runs asynchronously. | 
**credits_reserved** | **int** | Upfront credit reservation cap (1/10/11 for partial/phone_only/full). Pay-for-results: the workflow refunds the unused portion at settle, so the final debit may be lower. Poll status for the actual charge. | 
**lead_list_id** | **str** | List the enriched contact will be written to on completion. | 
**poll_url** | **str** | Fully-qualified URL to poll for workflow status and results. | 

## Example

```python
from cleanlist_ai.models.enrich_person_response import EnrichPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichPersonResponse from a JSON string
enrich_person_response_instance = EnrichPersonResponse.from_json(json)
# print the JSON string representation of the object
print(EnrichPersonResponse.to_json())

# convert the object into a dict
enrich_person_response_dict = enrich_person_response_instance.to_dict()
# create an instance of EnrichPersonResponse from a dict
enrich_person_response_from_dict = EnrichPersonResponse.from_dict(enrich_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


