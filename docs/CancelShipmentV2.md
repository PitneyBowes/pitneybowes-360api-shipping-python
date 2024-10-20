# CancelShipmentV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** | The name of the Carrier. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**status** | **str** | Status of the Shipment. | [optional] 
**references** | [**CancelShipmentV2References**](CancelShipmentV2References.md) |  | [optional] 

## Example

```python
from shipping.models.cancel_shipment_v2 import CancelShipmentV2

# TODO update the JSON string below
json = "{}"
# create an instance of CancelShipmentV2 from a JSON string
cancel_shipment_v2_instance = CancelShipmentV2.from_json(json)
# print the JSON string representation of the object
print(CancelShipmentV2.to_json())

# convert the object into a dict
cancel_shipment_v2_dict = cancel_shipment_v2_instance.to_dict()
# create an instance of CancelShipmentV2 from a dict
cancel_shipment_v2_from_dict = CancelShipmentV2.from_dict(cancel_shipment_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


