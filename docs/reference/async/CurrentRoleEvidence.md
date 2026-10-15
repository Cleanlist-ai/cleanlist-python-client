# CurrentRoleEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**company_linkedin_url** | **str** |  | [optional] 
**company_founded_year** | **int** |  | [optional] 
**company_industry** | **str** |  | [optional] 
**company_industries** | **List[str]** |  | [optional] 
**company_industries_truncated** | **bool** |  | [optional] 
**company_headcount** | **int** |  | [optional] 
**company_headcount_range** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.current_role_evidence import CurrentRoleEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentRoleEvidence from a JSON string
current_role_evidence_instance = CurrentRoleEvidence.from_json(json)
# print the JSON string representation of the object
print(CurrentRoleEvidence.to_json())

# convert the object into a dict
current_role_evidence_dict = current_role_evidence_instance.to_dict()
# create an instance of CurrentRoleEvidence from a dict
current_role_evidence_from_dict = CurrentRoleEvidence.from_dict(current_role_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


