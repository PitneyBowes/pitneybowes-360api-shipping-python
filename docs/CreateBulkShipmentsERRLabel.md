# CreateBulkShipmentsERRLabel

This ShipmentBatch contains the schema information for ERR Label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the of ERR Batch which consists of multiple shipments (shipments in bulk) for Label printing, e.g. ERR-Bulk05. | 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**size** | **str** | This indicates the label size of the Bulk Shipment when it gets printed,i.e., DocSize. This has two options 8&#39; X 11&#39; or 4&#39; X 6&#39;. | 
**type** | **str** | Indicates the type of the Batch Shipment, e.g., Shipping Label. | 
**format** | **str** | Defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form. | [optional] 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. Default CarrierAccountID for this batch will be user&#39;s registered USPS account. User can override this value by defining it at Shipment level. | 
**service_id** | **str** | A unique identifier given to the carrier-specific service. User can override this value by defining it at Shipment level. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per USPS selected services, e.g. FRPKG, LGENV, TUBE, and PKG. User can override this value by defining it at Shipment level. | 
**parcel_id** | **str** | A unique identifier given to the parcel or package corresponding to the selected service. This is optional field, but is used in few cases. Examples include BLM10, B1095, MT1098, etc. User can override this value by defining it at Shipment level. | [optional] 
**special_services** | [**List[SpecialServiceERRInner]**](SpecialServiceERRInner.md) |  | [optional] 
**shipments** | [**List[ShipmentERR]**](ShipmentERR.md) |  | 

## Example

```python
from shipping.models.create_bulk_shipments_err_label import CreateBulkShipmentsERRLabel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkShipmentsERRLabel from a JSON string
create_bulk_shipments_err_label_instance = CreateBulkShipmentsERRLabel.from_json(json)
# print the JSON string representation of the object
print(CreateBulkShipmentsERRLabel.to_json())

# convert the object into a dict
create_bulk_shipments_err_label_dict = create_bulk_shipments_err_label_instance.to_dict()
# create an instance of CreateBulkShipmentsERRLabel from a dict
create_bulk_shipments_err_label_from_dict = CreateBulkShipmentsERRLabel.from_dict(create_bulk_shipments_err_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


