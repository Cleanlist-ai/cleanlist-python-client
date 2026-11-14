# CompanySignalsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_types** | **List[str]** | Any of job_posting, news, funding, headcount. | 
**company_domains** | **List[str]** | The accounts&#39; domains, up to 500. | 
**since** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.company_signals_request import CompanySignalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySignalsRequest from a JSON string
company_signals_request_instance = CompanySignalsRequest.from_json(json)
# print the JSON string representation of the object
print(CompanySignalsRequest.to_json())

# convert the object into a dict
company_signals_request_dict = company_signals_request_instance.to_dict()
# create an instance of CompanySignalsRequest from a dict
company_signals_request_from_dict = CompanySignalsRequest.from_dict(company_signals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


