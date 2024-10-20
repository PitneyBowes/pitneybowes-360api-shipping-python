# CreateBulkShipmentsAPIERRRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the of ERR Batch which consists of multiple shipments (shipments in bulk) for Coversheet printing., e.g. ERR-Coversheet07. | 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**size** | **str** | This indicates the envelope size of the ERR Bulk Shipment, i.e., DocSize. We have indicated the example values in enum. | 
**type** | **str** | Indicates the type of the Batch Shipment, e.g., Shipping Label. | 
**format** | **str** | This defines the format type of the shipment which is printed. For example Coversheet prints in PDF form. | [optional] 
**carrier_account_id** | **str** | The unique identifier associated with the user&#39;s registered USPS Account which will be required for this batch. User can override this value by defining it at Shipment level. | 
**service_id** | **str** | A unique identifier given  to the carrier-specific service which is used for this BulkShipment. User can override this value by defining it at shipment level. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per USPS selected services, e.g. LTR, LGENV. User can override this value by defining it at shipment level. | 
**parcel_id** | **str** | A unique identifier given to the parcel or package corresponding to the selected service. This is optional field, but is used in few cases. Examples include BLM10, B1095, MT1098, etc. User can override this value by defining it at Shipment level. | [optional] 
**special_services** | [**List[SpecialServiceERRInner]**](SpecialServiceERRInner.md) |  | [optional] 
**shipments** | [**List[ShipmentERRCoversheet]**](ShipmentERRCoversheet.md) |  | 

## Example

```python
from shipping.models.create_bulk_shipments_apierr_request import CreateBulkShipmentsAPIERRRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkShipmentsAPIERRRequest from a JSON string
create_bulk_shipments_apierr_request_instance = CreateBulkShipmentsAPIERRRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBulkShipmentsAPIERRRequest.to_json())

# convert the object into a dict
create_bulk_shipments_apierr_request_dict = create_bulk_shipments_apierr_request_instance.to_dict()
# create an instance of CreateBulkShipmentsAPIERRRequest from a dict
create_bulk_shipments_apierr_request_from_dict = CreateBulkShipmentsAPIERRRequest.from_dict(create_bulk_shipments_apierr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


