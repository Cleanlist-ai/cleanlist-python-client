# KnowledgeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **bool** |  | [optional] [default to True]
**company_notes** | **bool** |  | [optional] [default to True]

## Example

```python
from cleanlist_ai.aio.models.knowledge_dto import KnowledgeDto

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDto from a JSON string
knowledge_dto_instance = KnowledgeDto.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDto.to_json())

# convert the object into a dict
knowledge_dto_dict = knowledge_dto_instance.to_dict()
# create an instance of KnowledgeDto from a dict
knowledge_dto_from_dict = KnowledgeDto.from_dict(knowledge_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


