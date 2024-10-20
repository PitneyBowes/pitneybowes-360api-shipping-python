# ShipmentInternational


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**ShipmentInternationalFromAddress**](ShipmentInternationalFromAddress.md) |  | 
**parcel** | [**ShipmentInternationalParcel**](ShipmentInternationalParcel.md) |  | 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. | 
**parcel_type** | **str** | &gt;-Packaging type specific to the carrier, e.g., FRPKG, LGENV, TUBE,PKG. | 
**service_id** | **str** | &gt;-The abbreviated name of the carrier-specific service. Required for creating a shipment. Optional for rating a parcel. | 
**date_of_shipment** | **str** | The date of the shipment. The format must be YYY:MM:DD. | [optional] 
**special_services** | [**List[SpecialService]**](SpecialService.md) |  | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**metadata** | [**List[ShipmentInternationalMetadataInner]**](ShipmentInternationalMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**to_address** | [**ShipmentInternationalToAddress**](ShipmentInternationalToAddress.md) |  | 
**customs** | [**ShipmentInternationalCustoms**](ShipmentInternationalCustoms.md) |  | 

## Example

```python
from shipping.models.shipment_international import ShipmentInternational

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentInternational from a JSON string
shipment_international_instance = ShipmentInternational.from_json(json)
# print the JSON string representation of the object
print(ShipmentInternational.to_json())

# convert the object into a dict
shipment_international_dict = shipment_international_instance.to_dict()
# create an instance of ShipmentInternational from a dict
shipment_international_from_dict = ShipmentInternational.from_dict(shipment_international_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


