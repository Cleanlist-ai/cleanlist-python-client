# BatchCompaniesLookupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[object]** | Up to 1,000 companies, each &#x60;{domain}&#x60; or &#x60;{linkedin_url}&#x60;. | 
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.batch_companies_lookup_request import BatchCompaniesLookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCompaniesLookupRequest from a JSON string
batch_companies_lookup_request_instance = BatchCompaniesLookupRequest.from_json(json)
# print the JSON string representation of the object
print(BatchCompaniesLookupRequest.to_json())

# convert the object into a dict
batch_companies_lookup_request_dict = batch_companies_lookup_request_instance.to_dict()
# create an instance of BatchCompaniesLookupRequest from a dict
batch_companies_lookup_request_from_dict = BatchCompaniesLookupRequest.from_dict(batch_companies_lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


