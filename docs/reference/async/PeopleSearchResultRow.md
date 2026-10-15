# PeopleSearchResultRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**confidence_score** | **int** |  | [optional] 
**company_linkedin_url** | **str** |  | [optional] 
**company_founded_year** | **int** |  | [optional] 
**company_industry** | **str** |  | [optional] 
**company_industries** | **List[str]** |  | [optional] 
**company_industries_truncated** | **bool** |  | [optional] 
**company_headcount** | **int** |  | [optional] 
**company_headcount_range** | **str** |  | [optional] 
**current_roles** | [**List[CurrentRoleEvidence]**](CurrentRoleEvidence.md) |  | [optional] 
**match_evidence** | [**PeopleMatchEvidence**](PeopleMatchEvidence.md) |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.people_search_result_row import PeopleSearchResultRow

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearchResultRow from a JSON string
people_search_result_row_instance = PeopleSearchResultRow.from_json(json)
# print the JSON string representation of the object
print(PeopleSearchResultRow.to_json())

# convert the object into a dict
people_search_result_row_dict = people_search_result_row_instance.to_dict()
# create an instance of PeopleSearchResultRow from a dict
people_search_result_row_from_dict = PeopleSearchResultRow.from_dict(people_search_result_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


