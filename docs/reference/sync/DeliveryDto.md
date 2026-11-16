# DeliveryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**DeliveryMessagesDto**](DeliveryMessagesDto.md) |  | [optional] 
**data** | [**DeliveryDataDto**](DeliveryDataDto.md) |  | [optional] 

## Example

```python
from cleanlist_ai.models.delivery_dto import DeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryDto from a JSON string
delivery_dto_instance = DeliveryDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryDto.to_json())

# convert the object into a dict
delivery_dto_dict = delivery_dto_instance.to_dict()
# create an instance of DeliveryDto from a dict
delivery_dto_from_dict = DeliveryDto.from_dict(delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


