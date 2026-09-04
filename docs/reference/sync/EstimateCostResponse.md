# EstimateCostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | HMAC-signed quote handle (&#x60;qte_&lt;kid&gt;_&lt;issued_at&gt;_&lt;sig&gt;&#x60;) that the paired paid tool must present at execution time. Single-use and bound to the canonical request (tool, list/filters, scope, row_count, org). | 
**expires_at** | **int** | Unix epoch SECONDS at which the quote expires (issue time + &#x60;CLEANLIST_QUOTE_TTL_SECONDS&#x60;, 5 min default). Re-estimate after this to obtain a fresh quote. | 
**estimated_cost** | **int** | Credits this operation will cost — the authoritative signed spend cap. Execution rejects (&#x60;spend_cap_exceeded&#x60;) if the recomputed cost would exceed it. | 
**tool** | **str** | Echo of the priced tool. | 
**row_count** | **int** | Number of rows/entities the estimate priced — derived from the list or cohort when applicable, not the caller&#39;s raw input. | 
**filter_hash** | **str** | Stable digest of the canonical filter/list/cohort shape bound into the quote signature; &#x60;none&#x60; when there is no filter object. | 
**available_credits** | **int** | The organization&#39;s current credit balance at estimate time. | 
**sufficient** | **bool** | True when &#x60;available_credits &gt;&#x3D; estimated_cost&#x60;. False signals the org must top up at billing before the operation can run. | 

## Example

```python
from cleanlist_ai.models.estimate_cost_response import EstimateCostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateCostResponse from a JSON string
estimate_cost_response_instance = EstimateCostResponse.from_json(json)
# print the JSON string representation of the object
print(EstimateCostResponse.to_json())

# convert the object into a dict
estimate_cost_response_dict = estimate_cost_response_instance.to_dict()
# create an instance of EstimateCostResponse from a dict
estimate_cost_response_from_dict = EstimateCostResponse.from_dict(estimate_cost_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


