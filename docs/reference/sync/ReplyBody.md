# ReplyBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**commit** | **bool** | Send it. Without it the answer is who would get it. | [optional] [default to False]
**request_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.reply_body import ReplyBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyBody from a JSON string
reply_body_instance = ReplyBody.from_json(json)
# print the JSON string representation of the object
print(ReplyBody.to_json())

# convert the object into a dict
reply_body_dict = reply_body_instance.to_dict()
# create an instance of ReplyBody from a dict
reply_body_from_dict = ReplyBody.from_dict(reply_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


