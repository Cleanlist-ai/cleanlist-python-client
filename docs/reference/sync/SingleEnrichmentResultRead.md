# SingleEnrichmentResultRead

Inline enriched-lead payload for single-workflow polls.  Populated by `enrich_status` only when the workflow is a single- lead `enrich_person` run AND has reached a terminal state. Read from the workflow's returned `EnrichmentResult` via Temporal's history — no extra DB round-trip, no race with backend visibility. Bulk-list runs leave `result=None` on the parent response (the aggregate counters carry the cohort's progress instead).  `status` here is the EnrichmentResult-level outcome (\"completed\" / \"failed\"), NOT the outer workflow status. Use it to distinguish a real enrichment (Lead persisted, lead_id set) from a workflow that returned cleanly with no usable Lead (e.g. provider cascade exhausted — `lead_id` will be empty).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **str** | ID of the persisted Lead. Empty when the provider cascade was exhausted with no usable result. | 
**status** | **str** | EnrichmentResult-level outcome: &#39;completed&#39; (lead persisted) or &#39;failed&#39;. Distinct from the outer workflow status. | 
**full_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_status** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**enrichment_type** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.single_enrichment_result_read import SingleEnrichmentResultRead

# TODO update the JSON string below
json = "{}"
# create an instance of SingleEnrichmentResultRead from a JSON string
single_enrichment_result_read_instance = SingleEnrichmentResultRead.from_json(json)
# print the JSON string representation of the object
print(SingleEnrichmentResultRead.to_json())

# convert the object into a dict
single_enrichment_result_read_dict = single_enrichment_result_read_instance.to_dict()
# create an instance of SingleEnrichmentResultRead from a dict
single_enrichment_result_read_from_dict = SingleEnrichmentResultRead.from_dict(single_enrichment_result_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


