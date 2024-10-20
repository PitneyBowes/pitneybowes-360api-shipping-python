# MultipieceRatesRequestToAddress

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | description | [optional] 
**name** | **str** | description | [optional] 
**phone** | **str** | description | [optional] 
**email** | **str** | description | [optional] 
**residential** | **bool** | description | [optional] 
**address_line1** | **str** | description | [optional] 
**city_town** | **str** | description | [optional] 
**state_province** | **str** | description | [optional] 
**postal_code** | **str** | description | [optional] 
**country_code** | **str** | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_request_to_address import MultipieceRatesRequestToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesRequestToAddress from a JSON string
multipiece_rates_request_to_address_instance = MultipieceRatesRequestToAddress.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesRequestToAddress.to_json())

# convert the object into a dict
multipiece_rates_request_to_address_dict = multipiece_rates_request_to_address_instance.to_dict()
# create an instance of MultipieceRatesRequestToAddress from a dict
multipiece_rates_request_to_address_from_dict = MultipieceRatesRequestToAddress.from_dict(multipiece_rates_request_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


