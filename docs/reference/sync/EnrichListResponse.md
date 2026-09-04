# EnrichListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**workflow_id** | **str** | Handle for the bulk enrichment workflow. Poll it via poll_url. | 
**status** | **str** | Always &#39;pending&#39; on dispatch — the bulk workflow runs async. | 
**total_leads** | **int** | Number of leads in the list submitted for enrichment. | 
**estimated_cost** | **int** | Recomputed cost for the run, capped at the quote&#39;s max_credits. | 
**credits_reserved** | **int** | Upfront reservation cap. Pay-for-results: leads with no email/phone found aren&#39;t charged, so settle refunds the unused portion. Poll status for the final debit. | 
**poll_url** | **str** | Fully-qualified URL to poll for aggregate progress and billing. | 

## Example

```python
from cleanlist_ai.models.enrich_list_response import EnrichListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichListResponse from a JSON string
enrich_list_response_instance = EnrichListResponse.from_json(json)
# print the JSON string representation of the object
print(EnrichListResponse.to_json())

# convert the object into a dict
enrich_list_response_dict = enrich_list_response_instance.to_dict()
# create an instance of EnrichListResponse from a dict
enrich_list_response_from_dict = EnrichListResponse.from_dict(enrich_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


