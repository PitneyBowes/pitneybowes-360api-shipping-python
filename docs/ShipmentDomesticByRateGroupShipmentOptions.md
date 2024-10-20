# ShipmentDomesticByRateGroupShipmentOptions

Shipment Options have an option of Manifest.<br /> With Manifest, the Mail Center agent can print the Manifest (End of day records of all created shipment) of selected carrier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_manifest** | **bool** | This option asks if the shipment is to be added for Manifest, so that the shipment will reflect in the Manifest Form while compilation. &lt;br /&gt; The value can be &#39;true&#39; or &#39;false&#39;. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_rate_group_shipment_options import ShipmentDomesticByRateGroupShipmentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByRateGroupShipmentOptions from a JSON string
shipment_domestic_by_rate_group_shipment_options_instance = ShipmentDomesticByRateGroupShipmentOptions.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByRateGroupShipmentOptions.to_json())

# convert the object into a dict
shipment_domestic_by_rate_group_shipment_options_dict = shipment_domestic_by_rate_group_shipment_options_instance.to_dict()
# create an instance of ShipmentDomesticByRateGroupShipmentOptions from a dict
shipment_domestic_by_rate_group_shipment_options_from_dict = ShipmentDomesticByRateGroupShipmentOptions.from_dict(shipment_domestic_by_rate_group_shipment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


