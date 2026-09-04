# AddByCohort

Mode B: materialize a prior search cohort into the list.  `search_*` rows carry integer search-DB ids (not lead UUIDs), so Mode A's `UUID(lead_id)` rejects them — Mode B resolves the cohort by `task_id` and creates the lead rows from the task's cached `entity_details`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | A cohort handle from a prior search_people / list_leads_in_list response. Materializes that cohort&#39;s entities into this list. | 
**entity_ids** | **List[str]** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.add_by_cohort import AddByCohort

# TODO update the JSON string below
json = "{}"
# create an instance of AddByCohort from a JSON string
add_by_cohort_instance = AddByCohort.from_json(json)
# print the JSON string representation of the object
print(AddByCohort.to_json())

# convert the object into a dict
add_by_cohort_dict = add_by_cohort_instance.to_dict()
# create an instance of AddByCohort from a dict
add_by_cohort_from_dict = AddByCohort.from_dict(add_by_cohort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


