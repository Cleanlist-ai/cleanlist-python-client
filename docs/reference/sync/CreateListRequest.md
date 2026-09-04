# CreateListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the list (1–200 chars). Create is idempotent on this name — if you already own an exact same-name list (case-insensitive) it is reused and returned with &#x60;reused: true&#x60; instead of a duplicate being inserted. | 
**description** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.create_list_request import CreateListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListRequest from a JSON string
create_list_request_instance = CreateListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateListRequest.to_json())

# convert the object into a dict
create_list_request_dict = create_list_request_instance.to_dict()
# create an instance of CreateListRequest from a dict
create_list_request_from_dict = CreateListRequest.from_dict(create_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


