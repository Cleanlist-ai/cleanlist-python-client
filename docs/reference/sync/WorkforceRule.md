# WorkforceRule

One CompanyDB role distribution or role growth rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Workforce role, one of WORKFORCE_ROLES. | 
**metric** | **str** | Role distribution percent, six-month growth (growth_6m), or year-over-year growth (growth_yoy). | 
**op** | **str** | Comparison direction. | 
**threshold** | [**Threshold**](Threshold.md) |  | 

## Example

```python
from cleanlist_ai.models.workforce_rule import WorkforceRule

# TODO update the JSON string below
json = "{}"
# create an instance of WorkforceRule from a JSON string
workforce_rule_instance = WorkforceRule.from_json(json)
# print the JSON string representation of the object
print(WorkforceRule.to_json())

# convert the object into a dict
workforce_rule_dict = workforce_rule_instance.to_dict()
# create an instance of WorkforceRule from a dict
workforce_rule_from_dict = WorkforceRule.from_dict(workforce_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


