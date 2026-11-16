# ConnectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**acting_user_id** | **str** |  | [optional] 
**policy** | **Dict[str, str]** |  | [optional] 
**acts_as** | [**PersonRefDto**](PersonRefDto.md) |  | [optional] 
**acts_as_owner** | **bool** |  | [optional] [default to False]
**connected_by** | [**PersonRefDto**](PersonRefDto.md) |  | [optional] 
**from_play** | **bool** |  | [optional] [default to False]

## Example

```python
from cleanlist_ai.aio.models.connection_dto import ConnectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionDto from a JSON string
connection_dto_instance = ConnectionDto.from_json(json)
# print the JSON string representation of the object
print(ConnectionDto.to_json())

# convert the object into a dict
connection_dto_dict = connection_dto_instance.to_dict()
# create an instance of ConnectionDto from a dict
connection_dto_from_dict = ConnectionDto.from_dict(connection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


