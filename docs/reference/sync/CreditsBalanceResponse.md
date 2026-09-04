# CreditsBalanceResponse

Minimal balance shape. The MCP `check_credits` description tells the agent to direct the user to billing for plan/renewal info, so we deliberately don't ship plan_slug / renew_at here even though callers might want them — keep the contract tight.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**timestamp_ms** | **int** |  | [optional] 
**agent_instructions** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**organization_id** | **str** | Organization whose credit wallet this balance belongs to. | 
**credits** | **int** | Current spendable credit balance for the organization (&#x60;organizations.credits_count&#x60;). Whole credits; never negative. | 

## Example

```python
from cleanlist_ai.models.credits_balance_response import CreditsBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsBalanceResponse from a JSON string
credits_balance_response_instance = CreditsBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(CreditsBalanceResponse.to_json())

# convert the object into a dict
credits_balance_response_dict = credits_balance_response_instance.to_dict()
# create an instance of CreditsBalanceResponse from a dict
credits_balance_response_from_dict = CreditsBalanceResponse.from_dict(credits_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


