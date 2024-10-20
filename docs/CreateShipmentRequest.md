# CreateShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | This defines the label size of the Shipment, e.g., Shipping Label having Doc Size (8&#39; X 11&#39;). | 
**type** | **str** | This defines the type of the Shipment, e.g., Shipping Label. | 
**format** | **str** | This defines the type of the shipment which is printed. For example Shipping label prints in PDF form. | [optional] 
**date_of_shipment** | **str** | This defines the date of the Shipment in the format YYYY:MM:DD. | [optional] 
**from_address** | [**ShipmentInternationalFromAddress**](ShipmentInternationalFromAddress.md) |  | 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | 
**carrier_account_id** | **str** | The unique identifier associated with the Carrier account used by client users during shipment process. | 
**parcel_type** | **str** | &gt;-Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. It has categories like Package, Envelopes, Paks, Boxes, Tube, defined per specific carrier and used in abbreviated form, e.g., FRPKG, LGENV, TUBE,PKG. | 
**parcel_id** | **str** | &gt;-Parcel Id is optional and required to be given in case of branded parcels which have brandedDimension and/or brandedWeight. If parcel has brandedDimension, in that case user need not to pass dimensionUnit and dimension details(length, width and height) in the parcel object. And if brandedWeight is also available for the parcel then in that case weightUnit and weight need not to be passed  in parcel object | [optional] 
**service_id** | **str** | &gt;-A unique identifier given to the carrier-specific service. This is required for creating a shipment, while it is optional for rating a parcel. | 
**special_services** | [**List[SpecialService]**](SpecialService.md) | This provides a carrier-service based special or extra sevice. | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**metadata** | [**List[ShipmentInternationalMetadataInner]**](ShipmentInternationalMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**to_address** | [**ShipmentInternationalToAddress**](ShipmentInternationalToAddress.md) |  | 
**customs** | [**ShipmentInternationalCustoms**](ShipmentInternationalCustoms.md) |  | 

## Example

```python
from shipping.models.create_shipment_request import CreateShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipmentRequest from a JSON string
create_shipment_request_instance = CreateShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShipmentRequest.to_json())

# convert the object into a dict
create_shipment_request_dict = create_shipment_request_instance.to_dict()
# create an instance of CreateShipmentRequest from a dict
create_shipment_request_from_dict = CreateShipmentRequest.from_dict(create_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


