# CreateBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Batch which consists of multiple shipments (shipments in bulk). | [optional] 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**size** | **str** | This indicates the label size of the Bulk Shipment, e.g., DocSize can be 8&#39; X 11&#39; or 4&#39; X 6&#39;. | 
**type** | **str** | This indicates the type of the Batch Shipment, e.g., Shipping Label. | 
**format** | **str** | This defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form. | [optional] 
**carrier_account_id** | **str** | A unique identifier associated with the carrier account used by client users during shipment process. | 
**service_id** | **str** | A unique identifier given to the carrier-specific service. This varies as per carrier selection. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per USPS selected services, e.g. FRPKG, LGENV, TUBE, and PKG. | 
**special_services** | [**List[SpecialServiceBatch]**](SpecialServiceBatch.md) |  | [optional] 

## Example

```python
from shipping.models.create_batch_request import CreateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequest from a JSON string
create_batch_request_instance = CreateBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequest.to_json())

# convert the object into a dict
create_batch_request_dict = create_batch_request_instance.to_dict()
# create an instance of CreateBatchRequest from a dict
create_batch_request_from_dict = CreateBatchRequest.from_dict(create_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


