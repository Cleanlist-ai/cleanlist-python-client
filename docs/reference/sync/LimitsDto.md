# LimitsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits_per_run** | **float** |  | [optional] 
**records_per_run** | **float** |  | [optional] 
**model_credits_per_run** | **float** |  | [optional] [default to 100]

## Example

```python
from cleanlist_ai.models.limits_dto import LimitsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LimitsDto from a JSON string
limits_dto_instance = LimitsDto.from_json(json)
# print the JSON string representation of the object
print(LimitsDto.to_json())

# convert the object into a dict
limits_dto_dict = limits_dto_instance.to_dict()
# create an instance of LimitsDto from a dict
limits_dto_from_dict = LimitsDto.from_dict(limits_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


