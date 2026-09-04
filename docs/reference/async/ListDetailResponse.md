# ListDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**list_id** | **str** | Stable identifier of the list. | 
**name** | **str** | Display name of the list. | 
**description** | **str** |  | [optional] 
**lead_count** | **int** | Live count of leads in the list (derived from a fresh COUNT). | 
**enriched_count** | **int** | How many of the leads have been enriched (email/phone found). | 
**folder_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**reused** | **bool** | True only when POST /lead-lists returned a pre-existing same-name list (idempotent reuse). Always false on reads and genuine creates. | [optional] [default to False]

## Example

```python
from cleanlist_ai.aio.models.list_detail_response import ListDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetailResponse from a JSON string
list_detail_response_instance = ListDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ListDetailResponse.to_json())

# convert the object into a dict
list_detail_response_dict = list_detail_response_instance.to_dict()
# create an instance of ListDetailResponse from a dict
list_detail_response_from_dict = ListDetailResponse.from_dict(list_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


