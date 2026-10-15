# CrmFilterSections

``CrmFilterSections``: clauses grouped by the CRM they resolve against.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salesforce** | [**List[CrmFilterClause]**](CrmFilterClause.md) | Clauses resolved against Salesforce. | [optional] 
**hubspot** | [**List[CrmFilterClause]**](CrmFilterClause.md) | Clauses resolved against HubSpot. | [optional] 

## Example

```python
from cleanlist_ai.models.crm_filter_sections import CrmFilterSections

# TODO update the JSON string below
json = "{}"
# create an instance of CrmFilterSections from a JSON string
crm_filter_sections_instance = CrmFilterSections.from_json(json)
# print the JSON string representation of the object
print(CrmFilterSections.to_json())

# convert the object into a dict
crm_filter_sections_dict = crm_filter_sections_instance.to_dict()
# create an instance of CrmFilterSections from a dict
crm_filter_sections_from_dict = CrmFilterSections.from_dict(crm_filter_sections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


