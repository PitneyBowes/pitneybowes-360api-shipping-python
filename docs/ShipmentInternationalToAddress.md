# ShipmentInternationalToAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**city_town** | **str** |  | [optional] 
**country_code** | **str** |  | 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**postal_code** | **str** |  | 
**state_province** | **str** |  | 

## Example

```python
from shipping.models.shipment_international_to_address import ShipmentInternationalToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentInternationalToAddress from a JSON string
shipment_international_to_address_instance = ShipmentInternationalToAddress.from_json(json)
# print the JSON string representation of the object
print(ShipmentInternationalToAddress.to_json())

# convert the object into a dict
shipment_international_to_address_dict = shipment_international_to_address_instance.to_dict()
# create an instance of ShipmentInternationalToAddress from a dict
shipment_international_to_address_from_dict = ShipmentInternationalToAddress.from_dict(shipment_international_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


