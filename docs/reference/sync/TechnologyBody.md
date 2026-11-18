# TechnologyBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | **List[str]** |  | 
**company_criteria** | **object** | Company filters, as in company search. | 
**limit** | **int** |  | [optional] [default to 25]
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.technology_body import TechnologyBody

# TODO update the JSON string below
json = "{}"
# create an instance of TechnologyBody from a JSON string
technology_body_instance = TechnologyBody.from_json(json)
# print the JSON string representation of the object
print(TechnologyBody.to_json())

# convert the object into a dict
technology_body_dict = technology_body_instance.to_dict()
# create an instance of TechnologyBody from a dict
technology_body_from_dict = TechnologyBody.from_dict(technology_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


