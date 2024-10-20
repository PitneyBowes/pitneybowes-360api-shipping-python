# CreateBatchRequestERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the of ERR Batch which is imported, e.g. ERR-Import-05. | [optional] 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**size** | **str** | This indicates the label size of the Bulk Shipment when it gets printed,i.e., DocSize. | 
**type** | **str** | This indicates the type of the Batch Shipment, e.g., Shipping Label and Coversheet. | 
**format** | **str** | This defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form. | [optional] 
**carrier_account_id** | **str** | A unique identifier associated with the carrier account used by client users during shipment process. Default CarrierAccountID for this batch will be user&#39;s registered USPS account. | 
**service_id** | **str** | A unique identifier given to the carrier-specific service. User can override this value by defining it at Shipment level. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per USPS selected services, e.g. FRPKG, LGENV, TUBE, and PKG. | 
**special_services** | [**List[SpecialServiceBatchERR]**](SpecialServiceBatchERR.md) |  | [optional] 

## Example

```python
from shipping.models.create_batch_request_err import CreateBatchRequestERR

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequestERR from a JSON string
create_batch_request_err_instance = CreateBatchRequestERR.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequestERR.to_json())

# convert the object into a dict
create_batch_request_err_dict = create_batch_request_err_instance.to_dict()
# create an instance of CreateBatchRequestERR from a dict
create_batch_request_err_from_dict = CreateBatchRequestERR.from_dict(create_batch_request_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


