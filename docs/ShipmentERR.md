# ShipmentERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | This is a user-defined value provided by users just for their reference. This is for mapping purpose against each shipment. | [optional] 
**from_address** | [**FromAddress**](FromAddress.md) |  | 
**to_address** | [**ToAddress**](ToAddress.md) |  | 
**parcel** | [**Parcel**](Parcel.md) |  | 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. | [optional] 
**parcel_type** | **str** | &gt;-Packaging type varies as per selected carrier and its services, e.g., PKG, LGENV. | [optional] 
**service_id** | **str** | &gt;-The unique identifier given to the carrier-specific service. ERR supports two services: First Class Mail (FCM) and Priority Mail (PM). | [optional] 
**date_of_shipment** | **str** | Indicates the date when shipment is created. | [optional] 
**special_services** | [**List[SpecialServiceERRInner]**](SpecialServiceERRInner.md) |  | [optional] 
**shipment_options** | [**ShipmentOptionsERR**](ShipmentOptionsERR.md) |  | [optional] 
**metadata** | [**List[ShipmentERRMetadataInner]**](ShipmentERRMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 

## Example

```python
from shipping.models.shipment_err import ShipmentERR

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentERR from a JSON string
shipment_err_instance = ShipmentERR.from_json(json)
# print the JSON string representation of the object
print(ShipmentERR.to_json())

# convert the object into a dict
shipment_err_dict = shipment_err_instance.to_dict()
# create an instance of ShipmentERR from a dict
shipment_err_from_dict = ShipmentERR.from_dict(shipment_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


