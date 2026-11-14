# UpdateTaskBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**outcome** | **str** |  | [optional] [default to '']
**note** | **str** |  | [optional] [default to '']
**commit** | **bool** | Needed when the change writes to the CRM; without it that call answers with a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.update_task_body import UpdateTaskBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskBody from a JSON string
update_task_body_instance = UpdateTaskBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskBody.to_json())

# convert the object into a dict
update_task_body_dict = update_task_body_instance.to_dict()
# create an instance of UpdateTaskBody from a dict
update_task_body_from_dict = UpdateTaskBody.from_dict(update_task_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


