# GetAllShipmentsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | This is a GUID (globally unique identifier) that&#39;s automatically generated for every request that the webserver receives. | [optional] 
**from_address** | [**GetAllShipmentsDataInnerFromAddress**](GetAllShipmentsDataInnerFromAddress.md) |  | [optional] 
**parcel** | [**GetAllShipmentsDataInnerParcel**](GetAllShipmentsDataInnerParcel.md) |  | [optional] 
**metadata** | [**List[GetAllShipmentsDataInnerMetadataInner]**](GetAllShipmentsDataInnerMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**parcel_tracking_number** | **str** | The Tracking number given to the Parcel for tracking purpose. | [optional] 
**rate** | [**GetAllShipmentsDataInnerRate**](GetAllShipmentsDataInnerRate.md) |  | [optional] 
**service** | **str** |  | [optional] 
**shipment_id** | **str** | A unique identifier associated with the Shipment. | [optional] 
**status** | **str** |  | [optional] 
**to_address** | [**GetAllShipmentsDataInnerToAddress**](GetAllShipmentsDataInnerToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.get_all_shipments_data_inner import GetAllShipmentsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllShipmentsDataInner from a JSON string
get_all_shipments_data_inner_instance = GetAllShipmentsDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAllShipmentsDataInner.to_json())

# convert the object into a dict
get_all_shipments_data_inner_dict = get_all_shipments_data_inner_instance.to_dict()
# create an instance of GetAllShipmentsDataInner from a dict
get_all_shipments_data_inner_from_dict = GetAllShipmentsDataInner.from_dict(get_all_shipments_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


