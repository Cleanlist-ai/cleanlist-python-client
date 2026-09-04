# WorkflowStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**workflow_id** | **str** | The workflow (or cohort task) handle being polled. | 
**status** | **str** | Outer workflow status: e.g. &#39;pending&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;cancelled&#39;. | 
**progress** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**processed** | **int** |  | [optional] 
**completed** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**enrichment_type** | **str** |  | [optional] 
**lead_list_id** | **str** |  | [optional] 
**summary** | **object** |  | [optional] 
**refund_status** | **str** |  | [optional] 
**refund_message** | **str** |  | [optional] 
**result** | [**SingleEnrichmentResultRead**](SingleEnrichmentResultRead.md) |  | [optional] 
**credits_charged** | **int** |  | [optional] 
**credits_refunded** | **int** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.workflow_status_response import WorkflowStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStatusResponse from a JSON string
workflow_status_response_instance = WorkflowStatusResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowStatusResponse.to_json())

# convert the object into a dict
workflow_status_response_dict = workflow_status_response_instance.to_dict()
# create an instance of WorkflowStatusResponse from a dict
workflow_status_response_from_dict = WorkflowStatusResponse.from_dict(workflow_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


