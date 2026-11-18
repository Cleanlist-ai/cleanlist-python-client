# BuyingCommitteeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | The company&#39;s domain, like acme.com | 
**personas** | [**List[Persona]**](Persona.md) |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.buying_committee_body import BuyingCommitteeBody

# TODO update the JSON string below
json = "{}"
# create an instance of BuyingCommitteeBody from a JSON string
buying_committee_body_instance = BuyingCommitteeBody.from_json(json)
# print the JSON string representation of the object
print(BuyingCommitteeBody.to_json())

# convert the object into a dict
buying_committee_body_dict = buying_committee_body_instance.to_dict()
# create an instance of BuyingCommitteeBody from a dict
buying_committee_body_from_dict = BuyingCommitteeBody.from_dict(buying_committee_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


