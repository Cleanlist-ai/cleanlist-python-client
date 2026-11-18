# CreateTaskBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_id** | **str** |  | 
**task_type** | **str** |  | [optional] [default to 'Call']
**due_at** | **str** | YYYY-MM-DD | 
**note** | **str** |  | [optional] [default to '']
**commit** | **bool** | Needed when the new task is also created in the CRM; without it that call answers with a preview. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.create_task_body import CreateTaskBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskBody from a JSON string
create_task_body_instance = CreateTaskBody.from_json(json)
# print the JSON string representation of the object
print(CreateTaskBody.to_json())

# convert the object into a dict
create_task_body_dict = create_task_body_instance.to_dict()
# create an instance of CreateTaskBody from a dict
create_task_body_from_dict = CreateTaskBody.from_dict(create_task_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


