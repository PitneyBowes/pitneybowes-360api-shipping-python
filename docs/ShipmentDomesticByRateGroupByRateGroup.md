# ShipmentDomesticByRateGroupByRateGroup

Indicates the category to select how cheap the carrier service is, or which carrier has fastest service. <br /> It displays the list of those services. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The Rule Type is a condition applied to RateGroup by Product side as per the customer requirement, which can have following options: Cheapest, Fastest, and deliverBy. &lt;br /&gt; If ruleType is deliverBy, then deliverBy date under deliveryOption will be mandatory to provide. | 
**rate_group_id** | **str** | This is a unique identifier assigned to the created RateGroup, which is used in the shipment creation. | 

## Example

```python
from shipping.models.shipment_domestic_by_rate_group_by_rate_group import ShipmentDomesticByRateGroupByRateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByRateGroupByRateGroup from a JSON string
shipment_domestic_by_rate_group_by_rate_group_instance = ShipmentDomesticByRateGroupByRateGroup.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByRateGroupByRateGroup.to_json())

# convert the object into a dict
shipment_domestic_by_rate_group_by_rate_group_dict = shipment_domestic_by_rate_group_by_rate_group_instance.to_dict()
# create an instance of ShipmentDomesticByRateGroupByRateGroup from a dict
shipment_domestic_by_rate_group_by_rate_group_from_dict = ShipmentDomesticByRateGroupByRateGroup.from_dict(shipment_domestic_by_rate_group_by_rate_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


