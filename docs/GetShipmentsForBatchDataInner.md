# GetShipmentsForBatchDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | This is a system-generated unique identifier assigned to the Batch while it is processed. | [optional] 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. | [optional] 
**external_id** | **str** | This is a user-defined value provided by users just for their reference. This is for mapping purpose against each shipment. | [optional] 
**from_address** | [**FromAddress**](FromAddress.md) |  | [optional] 
**label_layout** | [**GetShipmentsForBatchDataInnerLabelLayout**](GetShipmentsForBatchDataInnerLabelLayout.md) |  | [optional] 
**metadata** | [**List[GetShipmentsForBatchDataInnerMetadataInner]**](GetShipmentsForBatchDataInnerMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 
**parcel** | [**Parcel**](Parcel.md) |  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per carrier selection and corresponding services. | [optional] 
**service_id** | **str** | A unique identifier given to the carrier-specific service. User can override this value by defining it at Shipment level. | [optional] 
**shipment_id** | **str** | Shipment ID is a unique identifier for an individual shipment | [optional] 
**shipment_identifier** | **str** | Unique identifier generated for each shipment, it can be either success or failed. | [optional] 
**shipment_options** | [**ShipmentOptions**](ShipmentOptions.md) |  | [optional] 
**special_services** | [**List[GetShipmentsForBatchDataInnerSpecialServicesInner]**](GetShipmentsForBatchDataInnerSpecialServicesInner.md) | Special services used to create shipment | [optional] 
**step_status** | [**GetShipmentsForBatchDataInnerStepStatus**](GetShipmentsForBatchDataInnerStepStatus.md) |  | [optional] 
**to_address** | [**ToAddress**](ToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_data_inner import GetShipmentsForBatchDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchDataInner from a JSON string
get_shipments_for_batch_data_inner_instance = GetShipmentsForBatchDataInner.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchDataInner.to_json())

# convert the object into a dict
get_shipments_for_batch_data_inner_dict = get_shipments_for_batch_data_inner_instance.to_dict()
# create an instance of GetShipmentsForBatchDataInner from a dict
get_shipments_for_batch_data_inner_from_dict = GetShipmentsForBatchDataInner.from_dict(get_shipments_for_batch_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


