# GeoRadius

``SearchFilters.geoRadius``: a free-text center plus a distance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | **str** | Free-text location the radius is measured from. | [optional] [default to '']
**radius** | **float** | Distance from the center; must be greater than 0 to apply. | [optional] [default to 0]
**unit** | **str** | Distance unit: km or mi. | [optional] [default to 'km']

## Example

```python
from cleanlist_ai.models.geo_radius import GeoRadius

# TODO update the JSON string below
json = "{}"
# create an instance of GeoRadius from a JSON string
geo_radius_instance = GeoRadius.from_json(json)
# print the JSON string representation of the object
print(GeoRadius.to_json())

# convert the object into a dict
geo_radius_dict = geo_radius_instance.to_dict()
# create an instance of GeoRadius from a dict
geo_radius_from_dict = GeoRadius.from_dict(geo_radius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


