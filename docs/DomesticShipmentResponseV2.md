# DomesticShipmentResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Key assigned by the shipping system to the transaction. | [optional] 
**shipment_id** | **str** | The shipmentId, a unique identifier for an individual Shipment. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**label_layout** | [**List[DomesticShipmentResponseV2LabelLayoutInner]**](DomesticShipmentResponseV2LabelLayoutInner.md) | It defines the layout of the shipping label. | [optional] 
**parcel** | [**ParcelV2**](ParcelV2.md) |  | [optional] 
**rate** | [**RateResponseV2**](RateResponseV2.md) |  | [optional] 
**references** | [**ReferenceV2**](ReferenceV2.md) |  | [optional] 
**print_status** | **str** | Status of the Printed Label. | [optional] 
**print_error** | [**DomesticShipmentResponseV2PrintError**](DomesticShipmentResponseV2PrintError.md) |  | [optional] 
**from_address** | [**FromAddressV2Response**](FromAddressV2Response.md) |  | [optional] 
**to_address** | [**ToAddressV2Response**](ToAddressV2Response.md) |  | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 

## Example

```python
from shipping.models.domestic_shipment_response_v2 import DomesticShipmentResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of DomesticShipmentResponseV2 from a JSON string
domestic_shipment_response_v2_instance = DomesticShipmentResponseV2.from_json(json)
# print the JSON string representation of the object
print(DomesticShipmentResponseV2.to_json())

# convert the object into a dict
domestic_shipment_response_v2_dict = domestic_shipment_response_v2_instance.to_dict()
# create an instance of DomesticShipmentResponseV2 from a dict
domestic_shipment_response_v2_from_dict = DomesticShipmentResponseV2.from_dict(domestic_shipment_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


