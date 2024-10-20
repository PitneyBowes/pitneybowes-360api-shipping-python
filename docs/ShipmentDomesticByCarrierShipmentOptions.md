# ShipmentDomesticByCarrierShipmentOptions

Shipment Options have an added feature that is Manifest.<br /> With Manifest, the Mail Center agent can print the Manifest (End of day records of all created shipment) of selected carrier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_manifest** | **bool** | This option asks if the shipment is to be added for Manifest, so that the shipment will reflect in the Manifest Form while compilation. &lt;br /&gt; The value can be &#39;true&#39; or &#39;false&#39;. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_carrier_shipment_options import ShipmentDomesticByCarrierShipmentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByCarrierShipmentOptions from a JSON string
shipment_domestic_by_carrier_shipment_options_instance = ShipmentDomesticByCarrierShipmentOptions.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByCarrierShipmentOptions.to_json())

# convert the object into a dict
shipment_domestic_by_carrier_shipment_options_dict = shipment_domestic_by_carrier_shipment_options_instance.to_dict()
# create an instance of ShipmentDomesticByCarrierShipmentOptions from a dict
shipment_domestic_by_carrier_shipment_options_from_dict = ShipmentDomesticByCarrierShipmentOptions.from_dict(shipment_domestic_by_carrier_shipment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


