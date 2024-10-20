# CancelShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** | The name of the Carrier. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties, except as noted below: | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**status** | **str** | Status of the Shipment. | [optional] 

## Example

```python
from shipping.models.cancel_shipment import CancelShipment

# TODO update the JSON string below
json = "{}"
# create an instance of CancelShipment from a JSON string
cancel_shipment_instance = CancelShipment.from_json(json)
# print the JSON string representation of the object
print(CancelShipment.to_json())

# convert the object into a dict
cancel_shipment_dict = cancel_shipment_instance.to_dict()
# create an instance of CancelShipment from a dict
cancel_shipment_from_dict = CancelShipment.from_dict(cancel_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


