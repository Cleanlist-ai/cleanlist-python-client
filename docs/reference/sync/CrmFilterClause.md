# CrmFilterClause

``CrmFilterClause``: one include/exclude condition against a CRM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required, nonblank stable client id for the clause. | 
**polarity** | **str** | Whether the clause narrows (exclude) or requires (include). | [optional] [default to 'exclude']
**condition** | **str** | The /crm/exclusion-set token, e.g. current_customers, owner:&lt;id&gt;, account_status:&lt;value&gt;. | 

## Example

```python
from cleanlist_ai.models.crm_filter_clause import CrmFilterClause

# TODO update the JSON string below
json = "{}"
# create an instance of CrmFilterClause from a JSON string
crm_filter_clause_instance = CrmFilterClause.from_json(json)
# print the JSON string representation of the object
print(CrmFilterClause.to_json())

# convert the object into a dict
crm_filter_clause_dict = crm_filter_clause_instance.to_dict()
# create an instance of CrmFilterClause from a dict
crm_filter_clause_from_dict = CrmFilterClause.from_dict(crm_filter_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


