# EstimateCostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool** | **str** | Tool to price. Must be a key in the server&#39;s cost table (e.g. &#x60;enrich_list&#x60;, &#x60;enrich_person&#x60;, &#x60;run_smart_agent&#x60;, &#x60;sync_to_crm&#x60;, &#x60;add_person_enrichments&#x60;). Unknown tools return a 400. | 
**list_id** | **str** |  | [optional] 
**filters** | **object** |  | [optional] 
**row_count** | **int** |  | [optional] 
**scope** | **str** |  | [optional] 
**agent_type** | **str** |  | [optional] 
**include_phone** | **bool** | Legacy boolean that requests phone enrichment when &#x60;enrichment_type&#x60;/&#x60;scope&#x60; are not set. Kept for back-compat; prefer &#x60;scope&#x60;/&#x60;enrichment_type&#x60;. | [optional] [default to False]
**provider** | **str** |  | [optional] 
**sub_action** | **str** |  | [optional] 
**enrichment_type** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**data_points** | **List[str]** |  | [optional] 
**entity_ids** | **List[str]** |  | [optional] 
**extra** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.estimate_cost_request import EstimateCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateCostRequest from a JSON string
estimate_cost_request_instance = EstimateCostRequest.from_json(json)
# print the JSON string representation of the object
print(EstimateCostRequest.to_json())

# convert the object into a dict
estimate_cost_request_dict = estimate_cost_request_instance.to_dict()
# create an instance of EstimateCostRequest from a dict
estimate_cost_request_from_dict = EstimateCostRequest.from_dict(estimate_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


