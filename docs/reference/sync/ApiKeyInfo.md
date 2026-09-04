# ApiKeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Opaque id of the API key row (safe to display and reference). | 
**key_prefix** | **str** | Non-secret leading segment of the key, used for at-a-glance identification. Cleanlist keys are &#x60;clapi_&#x60;. | 
**key_last4** | **str** | Last 4 characters of the key for disambiguation. The full secret is never returned by this endpoint. | 
**name** | **str** |  | [optional] 
**scopes** | **List[Optional[str]]** | Permission scopes carried by this key. Scopes are granted per-USER today, so every key the caller owns shares the caller&#39;s scopes. | 
**created_at** | **str** |  | [optional] 
**last_used_at** | **str** |  | [optional] 
**is_active** | **bool** | Whether the key is currently active. Revoked keys report false. | 

## Example

```python
from cleanlist_ai.models.api_key_info import ApiKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyInfo from a JSON string
api_key_info_instance = ApiKeyInfo.from_json(json)
# print the JSON string representation of the object
print(ApiKeyInfo.to_json())

# convert the object into a dict
api_key_info_dict = api_key_info_instance.to_dict()
# create an instance of ApiKeyInfo from a dict
api_key_info_from_dict = ApiKeyInfo.from_dict(api_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


