# RunRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**entity_type** | **str** |  | 
**lead_id** | **str** |  | [optional] 
**company_id** | **str** |  | [optional] 
**entity** | **object** |  | 
**current_node_id** | **str** |  | 
**status** | **str** |  | 
**source_node_id** | **str** |  | 
**parent_record_id** | **str** |  | [optional] 
**children** | **List[Optional[object]]** |  | [optional] [default to []]
**error** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**deliveries** | **List[Optional[object]]** |  | [optional] [default to []]
**fields** | **object** |  | [optional] 
**approval_reason** | **Dict[str, str]** |  | [optional] 
**path** | **List[Optional[object]]** |  | [optional] 
**outputs** | **object** |  | [optional] 
**crm_links** | **Dict[str, Dict[str, str]]** |  | [optional] 

## Example

```python
from cleanlist_ai.models.run_record_dto import RunRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of RunRecordDto from a JSON string
run_record_dto_instance = RunRecordDto.from_json(json)
# print the JSON string representation of the object
print(RunRecordDto.to_json())

# convert the object into a dict
run_record_dto_dict = run_record_dto_instance.to_dict()
# create an instance of RunRecordDto from a dict
run_record_dto_from_dict = RunRecordDto.from_dict(run_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


