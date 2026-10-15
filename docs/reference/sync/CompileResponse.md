# CompileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**route** | **object** |  | 
**person_filter** | **object** |  | 
**company_filter** | **object** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**exclusions_applied** | **Dict[str, int]** |  | [optional] 
**exclusions_complete** | **bool** |  | [optional] [default to True]

## Example

```python
from cleanlist_ai.models.compile_response import CompileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompileResponse from a JSON string
compile_response_instance = CompileResponse.from_json(json)
# print the JSON string representation of the object
print(CompileResponse.to_json())

# convert the object into a dict
compile_response_dict = compile_response_instance.to_dict()
# create an instance of CompileResponse from a dict
compile_response_from_dict = CompileResponse.from_dict(compile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


