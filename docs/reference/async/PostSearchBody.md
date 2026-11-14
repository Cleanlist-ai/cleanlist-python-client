# PostSearchBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Your LinkedIn account&#39;s id. | 
**keywords** | **str** | The topic, as search words. | 
**days** | **int** | How recent: 1, 7 or 30. | [optional] [default to 7]
**limit** | **int** |  | [optional] [default to 10]

## Example

```python
from cleanlist_ai.aio.models.post_search_body import PostSearchBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchBody from a JSON string
post_search_body_instance = PostSearchBody.from_json(json)
# print the JSON string representation of the object
print(PostSearchBody.to_json())

# convert the object into a dict
post_search_body_dict = post_search_body_instance.to_dict()
# create an instance of PostSearchBody from a dict
post_search_body_from_dict = PostSearchBody.from_dict(post_search_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


