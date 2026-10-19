# PersonPresentationRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | 1-based position in the returned rows. | 
**entity_id** | **str** |  | [optional] 
**name** | [**PresentationLink**](PresentationLink.md) |  | 
**title** | **str** |  | 
**company** | [**PresentationLink**](PresentationLink.md) |  | 
**location** | **str** |  | 
**headcount** | **str** |  | 
**headcount_discrepancy** | **bool** | The latest count falls outside the returned size band; both are observations. | [optional] [default to False]
**industry** | **str** |  | 
**industry_truncated** | **bool** | Provider industry labels were shortened or omitted upstream. | [optional] [default to False]
**evidence_status** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**extra** | **Dict[str, str]** | Cells for the requested extra columns, keyed by column name. | [optional] 

## Example

```python
from cleanlist_ai.models.person_presentation_row import PersonPresentationRow

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPresentationRow from a JSON string
person_presentation_row_instance = PersonPresentationRow.from_json(json)
# print the JSON string representation of the object
print(PersonPresentationRow.to_json())

# convert the object into a dict
person_presentation_row_dict = person_presentation_row_instance.to_dict()
# create an instance of PersonPresentationRow from a dict
person_presentation_row_from_dict = PersonPresentationRow.from_dict(person_presentation_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


