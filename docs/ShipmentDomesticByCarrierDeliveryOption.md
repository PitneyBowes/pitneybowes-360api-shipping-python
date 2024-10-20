# ShipmentDomesticByCarrierDeliveryOption

There are two options of delivery: deliverBy and useBestNextDate, where customer can schedule the delivery date in deliverBy. <br /> In case if the customer's scheduled `deliverBy` date falls under Holiday, then `useBestNextDate` will be used by our system. Then, we will mark the second option and deliver the same.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliver_by** | **date** | Delivery date is the data when shipment is to be delivered, which is scheduled by sender. The format of the Date is YYYY-MM-DD. &lt;br /&gt; This field will be mandatory to provide, if the customer chooses ruleType is deliverBy. | [optional] 
**use_best_next_date** | **bool** | When this is set to true, if the scheduled delivery date falls on a Holiday, then the next business day will be considered to deliver the shipment. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_carrier_delivery_option import ShipmentDomesticByCarrierDeliveryOption

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByCarrierDeliveryOption from a JSON string
shipment_domestic_by_carrier_delivery_option_instance = ShipmentDomesticByCarrierDeliveryOption.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByCarrierDeliveryOption.to_json())

# convert the object into a dict
shipment_domestic_by_carrier_delivery_option_dict = shipment_domestic_by_carrier_delivery_option_instance.to_dict()
# create an instance of ShipmentDomesticByCarrierDeliveryOption from a dict
shipment_domestic_by_carrier_delivery_option_from_dict = ShipmentDomesticByCarrierDeliveryOption.from_dict(shipment_domestic_by_carrier_delivery_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


