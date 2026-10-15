# PublicApiError

Canonical Cleanlist public API error envelope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**PublicApiErrorPayload**](PublicApiErrorPayload.md) |  | 

## Example

```python
from cleanlist_ai.aio.models.public_api_error import PublicApiError

# TODO update the JSON string below
json = "{}"
# create an instance of PublicApiError from a JSON string
public_api_error_instance = PublicApiError.from_json(json)
# print the JSON string representation of the object
print(PublicApiError.to_json())

# convert the object into a dict
public_api_error_dict = public_api_error_instance.to_dict()
# create an instance of PublicApiError from a dict
public_api_error_from_dict = PublicApiError.from_dict(public_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


