# RunDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_preview** | **object** |  | [optional] 
**id** | **str** |  | 
**playbook_id** | **str** |  | 
**status** | **str** |  | 
**outcome** | **Dict[str, str]** |  | [optional] 
**is_dry_run** | **bool** |  | [optional] [default to False]
**sample_size** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] [default to 0]
**test_record** | **object** |  | [optional] 
**projection_result** | **object** |  | [optional] 
**kind** | **str** |  | [optional] [default to 'trigger']
**holds** | **Dict[str, int]** |  | [optional] 
**from_plays** | **List[Dict[str, str]]** |  | [optional] 
**lead_list_id** | **str** |  | [optional] 
**graph_snapshot** | **object** |  | 
**records_total** | **int** |  | 
**records_completed** | **int** |  | 
**records_failed** | **int** |  | 
**credits_used** | **float** |  | 
**errors** | **List[Optional[object]]** |  | 
**node_stats** | [**List[NodeStatsDto]**](NodeStatsDto.md) |  | 
**frontier** | [**List[FrontierEntryDto]**](FrontierEntryDto.md) |  | 
**created_at** | **str** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**period** | **object** |  | [optional] 
**scan** | **object** |  | [optional] 
**meeting** | **object** |  | [optional] 
**sheet** | **object** |  | [optional] 
**cleanup** | **object** |  | [optional] 
**review** | **object** |  | [optional] 
**brief** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 
**waiting** | **Dict[str, Optional[object]]** |  | [optional] 
**projection** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.run_detail_dto import RunDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of RunDetailDto from a JSON string
run_detail_dto_instance = RunDetailDto.from_json(json)
# print the JSON string representation of the object
print(RunDetailDto.to_json())

# convert the object into a dict
run_detail_dto_dict = run_detail_dto_instance.to_dict()
# create an instance of RunDetailDto from a dict
run_detail_dto_from_dict = RunDetailDto.from_dict(run_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


