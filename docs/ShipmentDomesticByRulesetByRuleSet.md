# ShipmentDomesticByRulesetByRuleSet

User can create the Shipment using Rule Set.<br /> By Rule Set means a rule that is defined as one or more conditions resulting in an action (or more than one action). <br /> The conditions and actions can vary widely.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The Rule Type is a condition applied to RateGroup by Product side, which can be applicable for a client or set of client users. | [optional] 
**hazmat** | **str** | This is for Hazardous material. | [optional] 
**ship_option** | **str** | The options for shipment usually created based on priority or Zone. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_ruleset_by_rule_set import ShipmentDomesticByRulesetByRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByRulesetByRuleSet from a JSON string
shipment_domestic_by_ruleset_by_rule_set_instance = ShipmentDomesticByRulesetByRuleSet.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByRulesetByRuleSet.to_json())

# convert the object into a dict
shipment_domestic_by_ruleset_by_rule_set_dict = shipment_domestic_by_ruleset_by_rule_set_instance.to_dict()
# create an instance of ShipmentDomesticByRulesetByRuleSet from a dict
shipment_domestic_by_ruleset_by_rule_set_from_dict = ShipmentDomesticByRulesetByRuleSet.from_dict(shipment_domestic_by_ruleset_by_rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


