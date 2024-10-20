# CountriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | This indicates the two-character ISO code of the country from the ISO country list. | [optional] 
**country_name** | **str** | This indicates the name of the country. | [optional] 

## Example

```python
from shipping.models.countries_inner import CountriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CountriesInner from a JSON string
countries_inner_instance = CountriesInner.from_json(json)
# print the JSON string representation of the object
print(CountriesInner.to_json())

# convert the object into a dict
countries_inner_dict = countries_inner_instance.to_dict()
# create an instance of CountriesInner from a dict
countries_inner_from_dict = CountriesInner.from_dict(countries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


