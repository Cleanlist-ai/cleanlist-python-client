# FrontierEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 
**status** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from cleanlist_ai.aio.models.frontier_entry_dto import FrontierEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of FrontierEntryDto from a JSON string
frontier_entry_dto_instance = FrontierEntryDto.from_json(json)
# print the JSON string representation of the object
print(FrontierEntryDto.to_json())

# convert the object into a dict
frontier_entry_dto_dict = frontier_entry_dto_instance.to_dict()
# create an instance of FrontierEntryDto from a dict
frontier_entry_dto_from_dict = FrontierEntryDto.from_dict(frontier_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


