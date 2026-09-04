# UsageGroupRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Bucket label for this row, per the requested &#x60;group_by&#x60;: the tool/path, key id, day, or error class. | 
**calls** | **int** | Number of API calls counted in this bucket over the window. | 
**credits_spent** | **float** | Credits spent in this bucket. Float because per-lead agents can cost fractional credits (e.g. 0.5). Currently 0.0 until the request log gains a per-row cost column. | 
**errors** | **int** | Number of error (non-2xx) responses counted in this bucket. | 

## Example

```python
from cleanlist_ai.models.usage_group_row import UsageGroupRow

# TODO update the JSON string below
json = "{}"
# create an instance of UsageGroupRow from a JSON string
usage_group_row_instance = UsageGroupRow.from_json(json)
# print the JSON string representation of the object
print(UsageGroupRow.to_json())

# convert the object into a dict
usage_group_row_dict = usage_group_row_instance.to_dict()
# create an instance of UsageGroupRow from a dict
usage_group_row_from_dict = UsageGroupRow.from_dict(usage_group_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


