# EnrichByTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task handle from a prior search_people / search_companies / list_leads_in_list call. Org-scoped and time-limited; re-run the search to refresh an expired handle. | 
**data_points** | **List[str]** | Fields to enrich. Person tasks accept Email, Phone, LinkedIn; company tasks accept Industry, Employees, Revenue, Funding, TechStack, Domain. Must match the task&#39;s entity type. For person cohorts, Email+Phone → &#39;full&#39;, Phone → &#39;phone_only&#39;, else &#39;partial&#39;. | 
**entity_ids** | **List[str]** |  | [optional] 
**lead_list_id** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.enrich_by_task_request import EnrichByTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichByTaskRequest from a JSON string
enrich_by_task_request_instance = EnrichByTaskRequest.from_json(json)
# print the JSON string representation of the object
print(EnrichByTaskRequest.to_json())

# convert the object into a dict
enrich_by_task_request_dict = enrich_by_task_request_instance.to_dict()
# create an instance of EnrichByTaskRequest from a dict
enrich_by_task_request_from_dict = EnrichByTaskRequest.from_dict(enrich_by_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


