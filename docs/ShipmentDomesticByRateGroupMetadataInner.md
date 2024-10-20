# ShipmentDomesticByRateGroupMetadataInner

The data that provides information about other interrelated/ required sub-data.<br /> Here, metadata details consists of CostAccount Name and Value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Cost Account which are linked to Shipment. | [optional] 
**value** | **str** | Indicates the value for the CostAccount. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_rate_group_metadata_inner import ShipmentDomesticByRateGroupMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByRateGroupMetadataInner from a JSON string
shipment_domestic_by_rate_group_metadata_inner_instance = ShipmentDomesticByRateGroupMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByRateGroupMetadataInner.to_json())

# convert the object into a dict
shipment_domestic_by_rate_group_metadata_inner_dict = shipment_domestic_by_rate_group_metadata_inner_instance.to_dict()
# create an instance of ShipmentDomesticByRateGroupMetadataInner from a dict
shipment_domestic_by_rate_group_metadata_inner_from_dict = ShipmentDomesticByRateGroupMetadataInner.from_dict(shipment_domestic_by_rate_group_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


