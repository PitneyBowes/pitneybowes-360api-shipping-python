# CreateShipment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | This is a GUID (globally unique identifier) that&#39;s automatically generated for every request that the webserver receives. | [optional] 
**label_layout** | [**List[DomesticShipmentResponseLabelLayoutInner]**](DomesticShipmentResponseLabelLayoutInner.md) | This indicates the label layout and generated label details | [optional] 
**from_address** | [**ReprintShipmentFromAddress**](ReprintShipmentFromAddress.md) |  | [optional] 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | [optional] 
**parcel_id** | **str** | &gt;-Parcel Id is optional and would be visible in case when is present in the request. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**rate** | [**InternationalShipmentResponseRate**](InternationalShipmentResponseRate.md) |  | [optional] 
**shipment_id** | **str** | A unique identifier associated with the Shipment. | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**to_address** | [**ReprintShipmentToAddress**](ReprintShipmentToAddress.md) |  | [optional] 
**customs** | [**InternationalShipmentResponseCustoms**](InternationalShipmentResponseCustoms.md) |  | [optional] 

## Example

```python
from shipping.models.create_shipment200_response import CreateShipment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipment200Response from a JSON string
create_shipment200_response_instance = CreateShipment200Response.from_json(json)
# print the JSON string representation of the object
print(CreateShipment200Response.to_json())

# convert the object into a dict
create_shipment200_response_dict = create_shipment200_response_instance.to_dict()
# create an instance of CreateShipment200Response from a dict
create_shipment200_response_from_dict = CreateShipment200Response.from_dict(create_shipment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


