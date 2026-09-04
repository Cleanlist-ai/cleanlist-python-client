# WhoamiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**user_email** | **str** |  | 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**organization_id** | **str** | Cleanlist organization id that owns this session&#39;s credits and lists. | 
**organization_name** | **str** |  | [optional] 
**auth_type** | **str** | How the caller authenticated: &#x60;clerk_jwt&#x60; (portal session token), &#x60;api_key&#x60; (a &#x60;clapi_&#x60; bearer key), or &#x60;oauth&#x60; (third-party grant). | 
**scopes** | **List[Optional[str]]** | Granted permission scopes for this credential (per-user Clerk &#x60;publicMetadata.cleanlist_scopes&#x60;). Endpoints gate on these — e.g. &#x60;credits:read&#x60;, &#x60;search:read&#x60;, &#x60;lists:write&#x60;, &#x60;enrichment:write&#x60;, &#x60;admin:api_keys&#x60;. | 
**tier** | **str** | Resolved plan tier from the org&#39;s Stripe &#x60;credits_product_id&#x60; (V2 &#39;Scale&#39; buyers map to &#x60;enterprise&#x60;). The MCP reads this once per session to tier-filter its advertised tool list. Unknown / unmapped products fall through to &#x60;free&#x60; (the safe default). | 
**appsumo_tier** | **int** |  | [optional] 
**features** | **List[Optional[str]]** | EFFECTIVE feature grants the gates actually enforce: base Stripe tier ∪ AppSumo carve-outs − AppSumo blocks (via &#x60;has_feature_effective&#x60;). Sourced from the same function the server-side gate uses so the advertised list and the gate can&#39;t drift. Sorted alphabetically for stable diffs. | 

## Example

```python
from cleanlist_ai.aio.models.whoami_response import WhoamiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhoamiResponse from a JSON string
whoami_response_instance = WhoamiResponse.from_json(json)
# print the JSON string representation of the object
print(WhoamiResponse.to_json())

# convert the object into a dict
whoami_response_dict = whoami_response_instance.to_dict()
# create an instance of WhoamiResponse from a dict
whoami_response_from_dict = WhoamiResponse.from_dict(whoami_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


