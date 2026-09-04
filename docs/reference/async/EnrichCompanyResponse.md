# EnrichCompanyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**company** | [**CompanyRecord**](CompanyRecord.md) | The enriched company record returned synchronously. | 
**credits_charged** | **int** | Final credits billed for this lookup (1). Settled inline before the response returns — no reserved-vs-charged ambiguity. | 

## Example

```python
from cleanlist_ai.aio.models.enrich_company_response import EnrichCompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichCompanyResponse from a JSON string
enrich_company_response_instance = EnrichCompanyResponse.from_json(json)
# print the JSON string representation of the object
print(EnrichCompanyResponse.to_json())

# convert the object into a dict
enrich_company_response_dict = enrich_company_response_instance.to_dict()
# create an instance of EnrichCompanyResponse from a dict
enrich_company_response_from_dict = EnrichCompanyResponse.from_dict(enrich_company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


