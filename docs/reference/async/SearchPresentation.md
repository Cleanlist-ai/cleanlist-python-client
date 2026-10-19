# SearchPresentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_kind** | **str** |  | [optional] [default to 'person']
**columns** | **List[str]** | Columns to lay out, in order. Name, Title, Company, Location, Headcount, Industry, Email and Phone read the row&#39;s own cells; any other column reads the row&#39;s extra cells. Renderers show exactly these. | [optional] 
**rows** | [**List[PersonPresentationRow]**](PersonPresentationRow.md) |  | [optional] 
**shown** | **int** | Rows in this block. | 
**returned** | **int** | Rows in the producing response. | 
**provider_total** | **int** |  | [optional] 
**evidence_checked** | **int** |  | [optional] 
**headcount_discrepancy_rows** | **List[int]** |  | [optional] 
**industry_truncated_rows** | **List[int]** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.search_presentation import SearchPresentation

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPresentation from a JSON string
search_presentation_instance = SearchPresentation.from_json(json)
# print the JSON string representation of the object
print(SearchPresentation.to_json())

# convert the object into a dict
search_presentation_dict = search_presentation_instance.to_dict()
# create an instance of SearchPresentation from a dict
search_presentation_from_dict = SearchPresentation.from_dict(search_presentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


