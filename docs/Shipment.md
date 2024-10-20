# Shipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the shipment. User can provide any custom value to it for its own reference | [optional] 
**from_address** | [**MultipieceDomesticShipmentRequestFromAddress**](MultipieceDomesticShipmentRequestFromAddress.md) |  | 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. | 
**parcel_type** | **str** | &gt;-Packaging type specific to the carrier, e.g., FRPKG, LGENV, TUBE,PKG. | 
**service_id** | **str** | &gt;-The abbreviated name of the carrier-specific service. Required for creating a shipment. Optional for rating a parcel. | 
**date_of_shipment** | **str** | Current Shipment date | [optional] 
**special_services** | [**List[SpecialService]**](SpecialService.md) |  | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**metadata** | [**List[ShipmentMetadataInner]**](ShipmentMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**to_address** | [**ShipmentToAddress**](ShipmentToAddress.md) |  | 

## Example

```python
from shipping.models.shipment import Shipment

# TODO update the JSON string below
json = "{}"
# create an instance of Shipment from a JSON string
shipment_instance = Shipment.from_json(json)
# print the JSON string representation of the object
print(Shipment.to_json())

# convert the object into a dict
shipment_dict = shipment_instance.to_dict()
# create an instance of Shipment from a dict
shipment_from_dict = Shipment.from_dict(shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


