# PeopleMatchEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**scope** | **str** |  | [optional] [default to 'current_role_and_company']
**title_match_mode** | **str** |  | [optional] 
**company_scope_match** | **bool** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.people_match_evidence import PeopleMatchEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleMatchEvidence from a JSON string
people_match_evidence_instance = PeopleMatchEvidence.from_json(json)
# print the JSON string representation of the object
print(PeopleMatchEvidence.to_json())

# convert the object into a dict
people_match_evidence_dict = people_match_evidence_instance.to_dict()
# create an instance of PeopleMatchEvidence from a dict
people_match_evidence_from_dict = PeopleMatchEvidence.from_dict(people_match_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


