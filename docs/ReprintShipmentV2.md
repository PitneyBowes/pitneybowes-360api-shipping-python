# ReprintShipmentV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | The shipmentId, a unique identifier for an individual Shipment, which is used for Reprint or Cancel. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**label_layout** | [**List[ReprintShipmentV2LabelLayoutInner]**](ReprintShipmentV2LabelLayoutInner.md) | It defines the layout of the shipping label. | [optional] 
**parcel** | [**ParcelV2**](ParcelV2.md) |  | [optional] 
**rate** | [**RateResponseV2**](RateResponseV2.md) |  | [optional] 
**references** | [**CancelShipmentV2References**](CancelShipmentV2References.md) |  | [optional] 
**print_status** | **str** | Status of the Printed Label. | [optional] 

## Example

```python
from shipping.models.reprint_shipment_v2 import ReprintShipmentV2

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintShipmentV2 from a JSON string
reprint_shipment_v2_instance = ReprintShipmentV2.from_json(json)
# print the JSON string representation of the object
print(ReprintShipmentV2.to_json())

# convert the object into a dict
reprint_shipment_v2_dict = reprint_shipment_v2_instance.to_dict()
# create an instance of ReprintShipmentV2 from a dict
reprint_shipment_v2_from_dict = ReprintShipmentV2.from_dict(reprint_shipment_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


