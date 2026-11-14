# UpdateThreadBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**commit** | **bool** | Needed when archiving closes a task in the CRM; without it that call answers with a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.update_thread_body import UpdateThreadBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThreadBody from a JSON string
update_thread_body_instance = UpdateThreadBody.from_json(json)
# print the JSON string representation of the object
print(UpdateThreadBody.to_json())

# convert the object into a dict
update_thread_body_dict = update_thread_body_instance.to_dict()
# create an instance of UpdateThreadBody from a dict
update_thread_body_from_dict = UpdateThreadBody.from_dict(update_thread_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


