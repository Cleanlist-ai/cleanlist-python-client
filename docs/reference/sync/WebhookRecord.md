# WebhookRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from cleanlist_ai.models.webhook_record import WebhookRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRecord from a JSON string
webhook_record_instance = WebhookRecord.from_json(json)
# print the JSON string representation of the object
print(WebhookRecord.to_json())

# convert the object into a dict
webhook_record_dict = webhook_record_instance.to_dict()
# create an instance of WebhookRecord from a dict
webhook_record_from_dict = WebhookRecord.from_dict(webhook_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


