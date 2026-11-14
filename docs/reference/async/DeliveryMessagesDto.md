# DeliveryMessagesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slack_channel_id** | **str** |  | [optional] 
**slack_channel_name** | **str** |  | [optional] 
**slack_dm** | **bool** |  | [optional] [default to False]
**email** | **List[str]** |  | [optional] 
**daily_summary** | [**DailySummaryDto**](DailySummaryDto.md) |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.delivery_messages_dto import DeliveryMessagesDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryMessagesDto from a JSON string
delivery_messages_dto_instance = DeliveryMessagesDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryMessagesDto.to_json())

# convert the object into a dict
delivery_messages_dto_dict = delivery_messages_dto_instance.to_dict()
# create an instance of DeliveryMessagesDto from a dict
delivery_messages_dto_from_dict = DeliveryMessagesDto.from_dict(delivery_messages_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


