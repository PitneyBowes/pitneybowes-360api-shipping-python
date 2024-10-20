# ReprintShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | This is a GUID (globally unique identifier) that&#39;s automatically generated for every request that the webserver receives. | [optional] 
**size** | **str** | This defines the label size of the Shipment, e.g., Shipping Label having Doc Size (8&#39; X 11&#39;). | [optional] 
**type** | **str** | This defines the type of the Shipment, e.g., Shipping Label. | [optional] 
**format** | **str** | This defines the type of the shipment which is printed. For example Shipping label prints in PDF form. | [optional] 
**from_address** | [**ReprintShipmentFromAddress**](ReprintShipmentFromAddress.md) |  | [optional] 
**parcel** | [**ReprintShipmentParcel**](ReprintShipmentParcel.md) |  | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**rate** | [**ReprintShipmentRate**](ReprintShipmentRate.md) |  | [optional] 
**shipment_id** | **str** | A unique identifier associated with Shipment ID. | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**to_address** | [**ReprintShipmentToAddress**](ReprintShipmentToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.reprint_shipment import ReprintShipment

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintShipment from a JSON string
reprint_shipment_instance = ReprintShipment.from_json(json)
# print the JSON string representation of the object
print(ReprintShipment.to_json())

# convert the object into a dict
reprint_shipment_dict = reprint_shipment_instance.to_dict()
# create an instance of ReprintShipment from a dict
reprint_shipment_from_dict = ReprintShipment.from_dict(reprint_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


