# EnrichPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_list_id** | **str** | ID of the lead list the enriched contact is written to when the workflow completes. Must be a list your API key can access. | 
**email** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**person_id** | **str** |  | [optional] 
**enrichment_type** | **str** |  | [optional] 
**include_phone** | **bool** | Legacy scope toggle, kept for back-compat. false → &#39;partial&#39;, true → &#39;phone_only&#39;. Ignored when enrichment_type is set. | [optional] [default to False]
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.enrich_person_request import EnrichPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichPersonRequest from a JSON string
enrich_person_request_instance = EnrichPersonRequest.from_json(json)
# print the JSON string representation of the object
print(EnrichPersonRequest.to_json())

# convert the object into a dict
enrich_person_request_dict = enrich_person_request_instance.to_dict()
# create an instance of EnrichPersonRequest from a dict
enrich_person_request_from_dict = EnrichPersonRequest.from_dict(enrich_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


