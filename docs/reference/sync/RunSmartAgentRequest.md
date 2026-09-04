# RunSmartAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** | UUID of the lead list the agent runs against. Must be a list this API key can access (owned, org-visible, or shared) — a known id for a private list in the same org is rejected with 404. | 
**agent_type** | **str** | Which agent to run. &#x60;custom_ai&#x60; runs your own &#x60;prompt&#x60;; &#x60;cold_intro_email&#x60; drafts a personalized opener from an email template. The preset research agents (&#x60;title_normalizer&#x60;, &#x60;company_intel&#x60;, &#x60;pain_point_hypothesis&#x60;) run a baked-in instruction and ignore &#x60;prompt&#x60;. All types execute asynchronously as an AI smart column. | [optional] [default to 'custom_ai']
**prompt** | **str** |  | [optional] 
**column_name** | **str** | Display name for the new column that stores each lead&#39;s agent output. Re-using an existing column name appends to it unless &#x60;overwrite&#x3D;true&#x60; is set. | 
**lead_scope** | **str** | &#x60;subset&#x60; runs on up to &#x60;max_rows&#x60; leads (the fast, cheap path). &#x60;all&#x60; runs on the entire list, but any &#x60;all&#x60; run above the configured threshold (default 500 leads) is blocked with a 400 &#x60;approval_required&#x60; until you narrow scope or route a human approval. | [optional] [default to 'subset']
**max_rows** | **int** | Upper bound on how many leads to process when &#x60;lead_scope&#x3D;&#39;subset&#39;&#x60;. Clamped to the list size. Ignored when &#x60;lead_scope&#x3D;&#39;all&#39;&#x60;. | [optional] [default to 100]
**quote_id** | **str** | Single-use spend quote from POST /credits/estimate, signed for this exact request shape (list_id + agent_type + column_name + row count). It is verified and atomically redeemed before the run starts; a stale, mismatched, or already-used quote returns a 400 or 409. Re-quote if you change any field. | 
**overwrite** | **bool** | When true, existing values in a column of the same name are overwritten instead of preserved. Passed through to the workflow via column metadata. | [optional] [default to False]

## Example

```python
from cleanlist_ai.models.run_smart_agent_request import RunSmartAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunSmartAgentRequest from a JSON string
run_smart_agent_request_instance = RunSmartAgentRequest.from_json(json)
# print the JSON string representation of the object
print(RunSmartAgentRequest.to_json())

# convert the object into a dict
run_smart_agent_request_dict = run_smart_agent_request_instance.to_dict()
# create an instance of RunSmartAgentRequest from a dict
run_smart_agent_request_from_dict = RunSmartAgentRequest.from_dict(run_smart_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


