# NodeStatsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 
**node_type** | **str** |  | 
**status** | **str** |  | 
**skip_reason** | **str** |  | [optional] 
**entered** | **int** |  | 
**succeeded** | **int** |  | 
**failed** | **int** |  | 
**filtered** | **int** |  | 
**credits_used** | **float** |  | 
**detail** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.node_stats_dto import NodeStatsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStatsDto from a JSON string
node_stats_dto_instance = NodeStatsDto.from_json(json)
# print the JSON string representation of the object
print(NodeStatsDto.to_json())

# convert the object into a dict
node_stats_dto_dict = node_stats_dto_instance.to_dict()
# create an instance of NodeStatsDto from a dict
node_stats_dto_from_dict = NodeStatsDto.from_dict(node_stats_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


