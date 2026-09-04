# CompanyRecord

Synchronous company enrichment result. Shape follows what CompanyDB returns, but with stable field names independent of Crustdata's response shape drift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**industries** | **List[str]** |  | [optional] 
**employee_count** | **int** |  | [optional] 
**employee_count_range** | **str** |  | [optional] 
**revenue_range** | **str** |  | [optional] 
**hq_location** | **str** |  | [optional] 
**funding_stage** | **str** |  | [optional] 
**total_funding_usd** | **int** |  | [optional] 
**tech_stack** | **List[str]** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.company_record import CompanyRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyRecord from a JSON string
company_record_instance = CompanyRecord.from_json(json)
# print the JSON string representation of the object
print(CompanyRecord.to_json())

# convert the object into a dict
company_record_dict = company_record_instance.to_dict()
# create an instance of CompanyRecord from a dict
company_record_from_dict = CompanyRecord.from_dict(company_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


