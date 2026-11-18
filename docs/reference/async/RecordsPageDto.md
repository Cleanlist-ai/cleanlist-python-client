# RecordsPageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[RunRecordDto]**](RunRecordDto.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.records_page_dto import RecordsPageDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecordsPageDto from a JSON string
records_page_dto_instance = RecordsPageDto.from_json(json)
# print the JSON string representation of the object
print(RecordsPageDto.to_json())

# convert the object into a dict
records_page_dto_dict = records_page_dto_instance.to_dict()
# create an instance of RecordsPageDto from a dict
records_page_dto_from_dict = RecordsPageDto.from_dict(records_page_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


