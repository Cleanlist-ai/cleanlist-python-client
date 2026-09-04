# RemoveLeadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | Identifier of the list leads were removed from. | 
**removed** | **int** | Number of membership rows actually removed. | 

## Example

```python
from cleanlist_ai.models.remove_leads_response import RemoveLeadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLeadsResponse from a JSON string
remove_leads_response_instance = RemoveLeadsResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveLeadsResponse.to_json())

# convert the object into a dict
remove_leads_response_dict = remove_leads_response_instance.to_dict()
# create an instance of RemoveLeadsResponse from a dict
remove_leads_response_from_dict = RemoveLeadsResponse.from_dict(remove_leads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


