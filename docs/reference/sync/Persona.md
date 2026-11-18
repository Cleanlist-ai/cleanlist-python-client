# Persona


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**titles** | **List[str]** |  | 
**exclude_titles** | **List[str]** |  | [optional] 
**count** | **int** |  | [optional] [default to 1]

## Example

```python
from cleanlist_ai.models.persona import Persona

# TODO update the JSON string below
json = "{}"
# create an instance of Persona from a JSON string
persona_instance = Persona.from_json(json)
# print the JSON string representation of the object
print(Persona.to_json())

# convert the object into a dict
persona_dict = persona_instance.to_dict()
# create an instance of Persona from a dict
persona_from_dict = Persona.from_dict(persona_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


