# DeletedWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** |  | 
**deleted** | **bool** |  | [optional] [default to True]

## Example

```python
from cleanlist_ai.aio.models.deleted_webhook import DeletedWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedWebhook from a JSON string
deleted_webhook_instance = DeletedWebhook.from_json(json)
# print the JSON string representation of the object
print(DeletedWebhook.to_json())

# convert the object into a dict
deleted_webhook_dict = deleted_webhook_instance.to_dict()
# create an instance of DeletedWebhook from a dict
deleted_webhook_from_dict = DeletedWebhook.from_dict(deleted_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


