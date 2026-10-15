# CreditsCharged

Actual credits billed after settle. Null while running or for non-prepaid legacy runs; 0 for a sweep-refunded run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from cleanlist_ai.models.credits_charged import CreditsCharged

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsCharged from a JSON string
credits_charged_instance = CreditsCharged.from_json(json)
# print the JSON string representation of the object
print(CreditsCharged.to_json())

# convert the object into a dict
credits_charged_dict = credits_charged_instance.to_dict()
# create an instance of CreditsCharged from a dict
credits_charged_from_dict = CreditsCharged.from_dict(credits_charged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


