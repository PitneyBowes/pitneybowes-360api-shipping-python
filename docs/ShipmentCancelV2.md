# ShipmentCancelV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | The shipmentId is a unique identifier for an individual Shipment. | 
**parcel_tracking_number** | **str** | The tracking number associated with one parcel in a shipment. The parcel tracking number can be used to track one specific parcel. | [optional] 
**references** | [**ShipmentReprintV2References**](ShipmentReprintV2References.md) |  | [optional] 

## Example

```python
from shipping.models.shipment_cancel_v2 import ShipmentCancelV2

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentCancelV2 from a JSON string
shipment_cancel_v2_instance = ShipmentCancelV2.from_json(json)
# print the JSON string representation of the object
print(ShipmentCancelV2.to_json())

# convert the object into a dict
shipment_cancel_v2_dict = shipment_cancel_v2_instance.to_dict()
# create an instance of ShipmentCancelV2 from a dict
shipment_cancel_v2_from_dict = ShipmentCancelV2.from_dict(shipment_cancel_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


