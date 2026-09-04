# ListsPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**lists** | [**List[ListSummary]**](ListSummary.md) | The page of lists accessible to the caller. | 
**total** | **int** | Total number of accessible lists across all pages. | 
**cursor** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.lists_page_response import ListsPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListsPageResponse from a JSON string
lists_page_response_instance = ListsPageResponse.from_json(json)
# print the JSON string representation of the object
print(ListsPageResponse.to_json())

# convert the object into a dict
lists_page_response_dict = lists_page_response_instance.to_dict()
# create an instance of ListsPageResponse from a dict
lists_page_response_from_dict = ListsPageResponse.from_dict(lists_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


