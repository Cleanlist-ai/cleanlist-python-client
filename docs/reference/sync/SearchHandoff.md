# SearchHandoff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**unavailable_reason** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.search_handoff import SearchHandoff

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHandoff from a JSON string
search_handoff_instance = SearchHandoff.from_json(json)
# print the JSON string representation of the object
print(SearchHandoff.to_json())

# convert the object into a dict
search_handoff_dict = search_handoff_instance.to_dict()
# create an instance of SearchHandoff from a dict
search_handoff_from_dict = SearchHandoff.from_dict(search_handoff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


