# GetSingleShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | This is a GUID (globally unique identifier) that&#39;s automatically generated for every request that the webserver receives. | [optional] 
**from_address** | [**GetSingleShipmentFromAddress**](GetSingleShipmentFromAddress.md) |  | [optional] 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | [optional] 
**metadata** | [**List[GetAllShipmentsDataInnerMetadataInner]**](GetAllShipmentsDataInnerMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**rate** | [**GetSingleShipmentRate**](GetSingleShipmentRate.md) |  | [optional] 
**service** | **str** | This indicates the carrier based service that is used for shipment. | [optional] 
**shipment_id** | **str** | A unique identifier associated with Shipment ID. | [optional] 
**status** | **str** | The status of the Shipment. | [optional] 
**to_address** | [**GetSingleShipmentToAddress**](GetSingleShipmentToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.get_single_shipment import GetSingleShipment

# TODO update the JSON string below
json = "{}"
# create an instance of GetSingleShipment from a JSON string
get_single_shipment_instance = GetSingleShipment.from_json(json)
# print the JSON string representation of the object
print(GetSingleShipment.to_json())

# convert the object into a dict
get_single_shipment_dict = get_single_shipment_instance.to_dict()
# create an instance of GetSingleShipment from a dict
get_single_shipment_from_dict = GetSingleShipment.from_dict(get_single_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


