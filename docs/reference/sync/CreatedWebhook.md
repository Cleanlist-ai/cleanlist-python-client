# CreatedWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**secret** | **str** | Signing secret for the Cleanlist-Signature header. Shown only in this response; store it now. | 

## Example

```python
from cleanlist_ai.models.created_webhook import CreatedWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedWebhook from a JSON string
created_webhook_instance = CreatedWebhook.from_json(json)
# print the JSON string representation of the object
print(CreatedWebhook.to_json())

# convert the object into a dict
created_webhook_dict = created_webhook_instance.to_dict()
# create an instance of CreatedWebhook from a dict
created_webhook_from_dict = CreatedWebhook.from_dict(created_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


