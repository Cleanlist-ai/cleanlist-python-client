# RunSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**playbook_id** | **str** |  | 
**status** | **str** |  | 
**is_dry_run** | **bool** |  | [optional] [default to False]
**sample_size** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] [default to 0]
**kind** | **str** |  | [optional] [default to 'trigger']
**holds** | **Dict[str, int]** |  | [optional] 
**from_plays** | **List[Dict[str, str]]** |  | [optional] 
**records_total** | **int** |  | 
**records_completed** | **int** |  | 
**records_failed** | **int** |  | 
**credits_used** | **float** |  | 
**workflow_id** | **str** |  | [optional] 
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
**test_record** | **object** |  | [optional] 
**waiting_holds** | **Dict[str, int]** |  | [optional] 
**error** | **Dict[str, str]** |  | [optional] 
**outcome** | **Dict[str, str]** |  | [optional] 

## Example

```python
from cleanlist_ai.models.run_summary_dto import RunSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of RunSummaryDto from a JSON string
run_summary_dto_instance = RunSummaryDto.from_json(json)
# print the JSON string representation of the object
print(RunSummaryDto.to_json())

# convert the object into a dict
run_summary_dto_dict = run_summary_dto_instance.to_dict()
# create an instance of RunSummaryDto from a dict
run_summary_dto_from_dict = RunSummaryDto.from_dict(run_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


