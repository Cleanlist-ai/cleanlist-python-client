# DeliveryDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_list_id** | **str** |  | [optional] 
**configured_lead_list_id** | **str** |  | [optional] 
**crm_sync** | **bool** |  | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.delivery_data_dto import DeliveryDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryDataDto from a JSON string
delivery_data_dto_instance = DeliveryDataDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryDataDto.to_json())

# convert the object into a dict
delivery_data_dto_dict = delivery_data_dto_instance.to_dict()
# create an instance of DeliveryDataDto from a dict
delivery_data_dto_from_dict = DeliveryDataDto.from_dict(delivery_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


