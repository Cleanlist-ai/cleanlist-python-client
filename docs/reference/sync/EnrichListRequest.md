# EnrichListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | The lead list to enrich in bulk. Every lead in the list runs through the provider waterfall. Must be non-empty and accessible to your API key. | 
**scope** | **str** | Enrichment scope per lead. &#39;partial&#39; &#x3D; email + LinkedIn + title + company (1 credit); &#39;phone-only&#39; &#x3D; phone only (10 credits); &#39;full&#39; &#x3D; email AND phone (11 credits). | [optional] [default to 'partial']
**quote_id** | **str** | Required. Obtain via POST /credits/estimate first (bound to this list_id + scope + lead count). Bulk spend must be pre-approved; cost is capped at the quote&#39;s max_credits. | 

## Example

```python
from cleanlist_ai.models.enrich_list_request import EnrichListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichListRequest from a JSON string
enrich_list_request_instance = EnrichListRequest.from_json(json)
# print the JSON string representation of the object
print(EnrichListRequest.to_json())

# convert the object into a dict
enrich_list_request_dict = enrich_list_request_instance.to_dict()
# create an instance of EnrichListRequest from a dict
enrich_list_request_from_dict = EnrichListRequest.from_dict(enrich_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


