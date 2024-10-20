# ShipmentDomesticByCarrierMetadataInner

The data that provides information about other inter-related/ required data.<br /> Here, metadata details consists of CostAccount Name and Value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Cost Account which are linked to Shipment. | [optional] 
**value** | **str** | Indicates the value for the CostAccount. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_carrier_metadata_inner import ShipmentDomesticByCarrierMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByCarrierMetadataInner from a JSON string
shipment_domestic_by_carrier_metadata_inner_instance = ShipmentDomesticByCarrierMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByCarrierMetadataInner.to_json())

# convert the object into a dict
shipment_domestic_by_carrier_metadata_inner_dict = shipment_domestic_by_carrier_metadata_inner_instance.to_dict()
# create an instance of ShipmentDomesticByCarrierMetadataInner from a dict
shipment_domestic_by_carrier_metadata_inner_from_dict = ShipmentDomesticByCarrierMetadataInner.from_dict(shipment_domestic_by_carrier_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


