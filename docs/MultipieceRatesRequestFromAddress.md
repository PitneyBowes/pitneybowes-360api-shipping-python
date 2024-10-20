# MultipieceRatesRequestFromAddress

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | description | [optional] 
**city_town** | **str** | description | [optional] 
**state_province** | **str** | description | [optional] 
**postal_code** | **str** | description | [optional] 
**country_code** | **str** | description | [optional] 
**company** | **str** | description | [optional] 
**name** | **str** | description | [optional] 
**phone** | **str** | description | [optional] 
**email** | **str** | description | [optional] 
**residential** | **bool** | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_request_from_address import MultipieceRatesRequestFromAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesRequestFromAddress from a JSON string
multipiece_rates_request_from_address_instance = MultipieceRatesRequestFromAddress.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesRequestFromAddress.to_json())

# convert the object into a dict
multipiece_rates_request_from_address_dict = multipiece_rates_request_from_address_instance.to_dict()
# create an instance of MultipieceRatesRequestFromAddress from a dict
multipiece_rates_request_from_address_from_dict = MultipieceRatesRequestFromAddress.from_dict(multipiece_rates_request_from_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


