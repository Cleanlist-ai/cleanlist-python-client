# ConfirmResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** |  | 
**status** | **str** |  | 
**result** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.confirm_result import ConfirmResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmResult from a JSON string
confirm_result_instance = ConfirmResult.from_json(json)
# print the JSON string representation of the object
print(ConfirmResult.to_json())

# convert the object into a dict
confirm_result_dict = confirm_result_instance.to_dict()
# create an instance of ConfirmResult from a dict
confirm_result_from_dict = ConfirmResult.from_dict(confirm_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


