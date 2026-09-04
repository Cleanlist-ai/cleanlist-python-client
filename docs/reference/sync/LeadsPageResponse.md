# LeadsPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**list_id** | **str** | Identifier of the list these leads belong to. | 
**leads** | [**List[LeadRow]**](LeadRow.md) | The page of leads in the list. | 
**total** | **int** | Total number of leads in the list across all pages. | 
**cursor** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.models.leads_page_response import LeadsPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeadsPageResponse from a JSON string
leads_page_response_instance = LeadsPageResponse.from_json(json)
# print the JSON string representation of the object
print(LeadsPageResponse.to_json())

# convert the object into a dict
leads_page_response_dict = leads_page_response_instance.to_dict()
# create an instance of LeadsPageResponse from a dict
leads_page_response_from_dict = LeadsPageResponse.from_dict(leads_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


