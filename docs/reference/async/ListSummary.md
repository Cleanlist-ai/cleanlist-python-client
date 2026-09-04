# ListSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | Stable identifier of the list. | 
**name** | **str** | Display name of the list. | 
**lead_count** | **int** | Live count of leads currently in the list. | 
**folder_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.list_summary import ListSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ListSummary from a JSON string
list_summary_instance = ListSummary.from_json(json)
# print the JSON string representation of the object
print(ListSummary.to_json())

# convert the object into a dict
list_summary_dict = list_summary_instance.to_dict()
# create an instance of ListSummary from a dict
list_summary_from_dict = ListSummary.from_dict(list_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


