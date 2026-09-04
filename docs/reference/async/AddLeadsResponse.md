# AddLeadsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | Identifier of the list leads were added to. | 
**added** | **int** | Number of leads newly inserted into the list (billed rows). | 
**skipped_duplicates** | **int** | Leads already in the list that were skipped (not re-billed). | 
**created** | **int** |  | [optional] 
**credits_charged** | **float** | Import credits charged. Import is free, so this is 0; only enrichment is billed (separately). | [optional] [default to 0]

## Example

```python
from cleanlist_ai.aio.models.add_leads_response import AddLeadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddLeadsResponse from a JSON string
add_leads_response_instance = AddLeadsResponse.from_json(json)
# print the JSON string representation of the object
print(AddLeadsResponse.to_json())

# convert the object into a dict
add_leads_response_dict = add_leads_response_instance.to_dict()
# create an instance of AddLeadsResponse from a dict
add_leads_response_from_dict = AddLeadsResponse.from_dict(add_leads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


