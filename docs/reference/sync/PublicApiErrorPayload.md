# PublicApiErrorPayload

The `error` field of every public-API error response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**problem** | **str** |  | 
**cause** | **str** |  | [optional] 
**fix** | **str** |  | [optional] 
**retryable** | **bool** |  | [optional] [default to False]
**retry_after_ms** | **int** |  | [optional] 
**docs_url** | **str** |  | 
**request_id** | **str** |  | 
**estimated_cost_credits** | **int** |  | [optional] 
**available_credits** | **int** |  | [optional] 
**shortfall_credits** | **int** |  | [optional] 
**suggested_actions** | [**List[SuggestedAction]**](SuggestedAction.md) |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from cleanlist_ai.models.public_api_error_payload import PublicApiErrorPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PublicApiErrorPayload from a JSON string
public_api_error_payload_instance = PublicApiErrorPayload.from_json(json)
# print the JSON string representation of the object
print(PublicApiErrorPayload.to_json())

# convert the object into a dict
public_api_error_payload_dict = public_api_error_payload_instance.to_dict()
# create an instance of PublicApiErrorPayload from a dict
public_api_error_payload_from_dict = PublicApiErrorPayload.from_dict(public_api_error_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


