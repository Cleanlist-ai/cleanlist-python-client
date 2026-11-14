# Card


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** |  | 
**title** | **str** |  | 
**summary** | **str** |  | 
**credits_required** | **float** |  | [optional] 
**expires_at** | **str** |  | 

## Example

```python
from cleanlist_ai.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print(Card.to_json())

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_from_dict = Card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


