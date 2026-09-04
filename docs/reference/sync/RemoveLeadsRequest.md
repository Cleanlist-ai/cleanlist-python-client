# RemoveLeadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_ids** | **List[str]** | Lead UUIDs to remove from the list (max 100 per call). Unknown ids are silently no-op — no 404. | 

## Example

```python
from cleanlist_ai.models.remove_leads_request import RemoveLeadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLeadsRequest from a JSON string
remove_leads_request_instance = RemoveLeadsRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveLeadsRequest.to_json())

# convert the object into a dict
remove_leads_request_dict = remove_leads_request_instance.to_dict()
# create an instance of RemoveLeadsRequest from a dict
remove_leads_request_from_dict = RemoveLeadsRequest.from_dict(remove_leads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


