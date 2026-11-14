# BatchPeopleLookupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[object]** | Up to 1,000 people, each &#x60;{email}&#x60;, &#x60;{linkedin_url}&#x60; or &#x60;{first_name, last_name, domain}&#x60; (extra known keys help the match). | 
**fields** | **List[str]** | What to look up for each row. Every email or phone lookup also resolves the profile; &#x60;profile&#x60; alone looks up the profile only. | 
**quote_id** | **str** |  | [optional] 
**lead_list_id** | **str** |  | [optional] 

## Example

```python
from cleanlist_ai.aio.models.batch_people_lookup_request import BatchPeopleLookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPeopleLookupRequest from a JSON string
batch_people_lookup_request_instance = BatchPeopleLookupRequest.from_json(json)
# print the JSON string representation of the object
print(BatchPeopleLookupRequest.to_json())

# convert the object into a dict
batch_people_lookup_request_dict = batch_people_lookup_request_instance.to_dict()
# create an instance of BatchPeopleLookupRequest from a dict
batch_people_lookup_request_from_dict = BatchPeopleLookupRequest.from_dict(batch_people_lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


