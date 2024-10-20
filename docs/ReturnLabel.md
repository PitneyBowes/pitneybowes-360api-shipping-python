# ReturnLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | This defines the label size of the Shipment, e.g., Shipping Label having Doc Size (8&#39; X 11&#39;). | [optional] 
**type** | **str** | This defines the type of the Shipment, e.g., Shipping Label. | [optional] 
**from_address** | [**ReturnLabelFromAddress**](ReturnLabelFromAddress.md) |  | [optional] 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | [optional] 
**carrier_account_id** | **str** | The unique identifier associated with the Carrier account used by client users during shipment process. | [optional] 
**parcel_type** | **str** | &gt;-Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. It has categories like Package, Envelopes, Paks, Boxes, Tube, defined per specific carrier and used in abbreviated form, e.g., FRPKG, LGENV, TUBE,PKG. | [optional] 
**parcel_id** | **str** | A unique identifier associated with the Parcel. | [optional] 
**service_id** | **str** | &gt;-A unique identifier given to the carrier-specific service. This is required for creating a shipment, while it is optional for rating a parcel. | [optional] 
**special_services** | [**List[ReturnLabelSpecialServicesInner]**](ReturnLabelSpecialServicesInner.md) |  | [optional] 
**shipment_options** | [**ShipmentOptionsV2**](ShipmentOptionsV2.md) |  | [optional] 
**metadata** | [**List[ShipmentInternationalMetadataInner]**](ShipmentInternationalMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**to_address** | [**ReturnLabelToAddress**](ReturnLabelToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.return_label import ReturnLabel

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabel from a JSON string
return_label_instance = ReturnLabel.from_json(json)
# print the JSON string representation of the object
print(ReturnLabel.to_json())

# convert the object into a dict
return_label_dict = return_label_instance.to_dict()
# create an instance of ReturnLabel from a dict
return_label_from_dict = ReturnLabel.from_dict(return_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


