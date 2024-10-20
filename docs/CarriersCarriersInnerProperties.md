# CarriersCarriersInnerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_not_supported** | **bool** | This defines if the carrier is domestic supported or not. For Not Supported, will take &#x60;true&#x60; as a boolean value, else it will take &#x60;false&#x60;. | [optional] 
**future_shipment_supported** | **bool** | This defines if the carrier supports future shipment. If yes, it will take the value &#x60;true&#x60;, else it will be &#x60;false&#x60;. | [optional] 
**international_supported** | **bool** | This defines if the carrier is internatioanl supported or not. If Yes, it will take &#x60;true&#x60; as boolean value, else it will take &#x60;false&#x60;. | [optional] 

## Example

```python
from shipping.models.carriers_carriers_inner_properties import CarriersCarriersInnerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersCarriersInnerProperties from a JSON string
carriers_carriers_inner_properties_instance = CarriersCarriersInnerProperties.from_json(json)
# print the JSON string representation of the object
print(CarriersCarriersInnerProperties.to_json())

# convert the object into a dict
carriers_carriers_inner_properties_dict = carriers_carriers_inner_properties_instance.to_dict()
# create an instance of CarriersCarriersInnerProperties from a dict
carriers_carriers_inner_properties_from_dict = CarriersCarriersInnerProperties.from_dict(carriers_carriers_inner_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


