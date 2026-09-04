# Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_ids** | **List[str]** | Lead UUIDs to add (from list_leads_in_list / an owned list). | 
**idempotency_key** | **str** |  | [optional] 
**task_id** | **str** | A cohort handle from a prior search_people / list_leads_in_list response. Materializes that cohort&#39;s entities into this list. | 
**entity_ids** | **List[str]** |  | [optional] 

## Example

```python
from cleanlist_ai.models.body import Body

# TODO update the JSON string below
json = "{}"
# create an instance of Body from a JSON string
body_instance = Body.from_json(json)
# print the JSON string representation of the object
print(Body.to_json())

# convert the object into a dict
body_dict = body_instance.to_dict()
# create an instance of Body from a dict
body_from_dict = Body.from_dict(body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


