# EnrichCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_ticker** | **str** |  | [optional] 
**company_id** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.enrich_company_request import EnrichCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichCompanyRequest from a JSON string
enrich_company_request_instance = EnrichCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(EnrichCompanyRequest.to_json())

# convert the object into a dict
enrich_company_request_dict = enrich_company_request_instance.to_dict()
# create an instance of EnrichCompanyRequest from a dict
enrich_company_request_from_dict = EnrichCompanyRequest.from_dict(enrich_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


