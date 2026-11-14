# DailySummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** |  | 
**timezone** | **str** |  | 

## Example

```python
from cleanlist_ai.aio.models.daily_summary_dto import DailySummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DailySummaryDto from a JSON string
daily_summary_dto_instance = DailySummaryDto.from_json(json)
# print the JSON string representation of the object
print(DailySummaryDto.to_json())

# convert the object into a dict
daily_summary_dto_dict = daily_summary_dto_instance.to_dict()
# create an instance of DailySummaryDto from a dict
daily_summary_dto_from_dict = DailySummaryDto.from_dict(daily_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


