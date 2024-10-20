# ShipmentDomesticByRulesetMetadataInner

The data that provides information about other interrelated/ required data.<br /> Here, metadata details consists of CostAccount Name and Value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Cost Account which are linked to Shipment. | [optional] 
**value** | **str** | Indicates the value for the CostAccount. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_ruleset_metadata_inner import ShipmentDomesticByRulesetMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByRulesetMetadataInner from a JSON string
shipment_domestic_by_ruleset_metadata_inner_instance = ShipmentDomesticByRulesetMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByRulesetMetadataInner.to_json())

# convert the object into a dict
shipment_domestic_by_ruleset_metadata_inner_dict = shipment_domestic_by_ruleset_metadata_inner_instance.to_dict()
# create an instance of ShipmentDomesticByRulesetMetadataInner from a dict
shipment_domestic_by_ruleset_metadata_inner_from_dict = ShipmentDomesticByRulesetMetadataInner.from_dict(shipment_domestic_by_ruleset_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


