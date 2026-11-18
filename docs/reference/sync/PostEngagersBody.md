# PostEngagersBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | **object** | People filters engagers must match, as in people search. | 
**author_urls** | **List[str]** |  | [optional] 
**text_phrases** | **List[str]** |  | [optional] 
**posted_within_days** | **int** |  | [optional] [default to 14]
**limit** | **int** |  | [optional] [default to 25]
**quote_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.post_engagers_body import PostEngagersBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostEngagersBody from a JSON string
post_engagers_body_instance = PostEngagersBody.from_json(json)
# print the JSON string representation of the object
print(PostEngagersBody.to_json())

# convert the object into a dict
post_engagers_body_dict = post_engagers_body_instance.to_dict()
# create an instance of PostEngagersBody from a dict
post_engagers_body_from_dict = PostEngagersBody.from_dict(post_engagers_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


