# FilterOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.filter_option import FilterOption

# TODO update the JSON string below
json = "{}"
# create an instance of FilterOption from a JSON string
filter_option_instance = FilterOption.from_json(json)
# print the JSON string representation of the object
print(FilterOption.to_json())

# convert the object into a dict
filter_option_dict = filter_option_instance.to_dict()
# create an instance of FilterOption from a dict
filter_option_from_dict = FilterOption.from_dict(filter_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


