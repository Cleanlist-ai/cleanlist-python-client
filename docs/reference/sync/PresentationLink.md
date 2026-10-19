# PresentationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.presentation_link import PresentationLink

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationLink from a JSON string
presentation_link_instance = PresentationLink.from_json(json)
# print the JSON string representation of the object
print(PresentationLink.to_json())

# convert the object into a dict
presentation_link_dict = presentation_link_instance.to_dict()
# create an instance of PresentationLink from a dict
presentation_link_from_dict = PresentationLink.from_dict(presentation_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


