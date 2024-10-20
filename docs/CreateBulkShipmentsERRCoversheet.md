# CreateBulkShipmentsERRCoversheet

This ShipmentBatch contains the schema information for ERR Coversheet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the of ERR Batch which consists of multiple shipments (shipments in bulk) for Coversheet printing., e.g. ERR-Coversheet07. | 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**size** | **str** | This indicates the envelope size of the ERR Bulk Shipment, i.e., DocSize. We have indicated the example values in enum. | 
**type** | **str** | This indicates the type of the ERR Batch Shipment, e.g., Coversheet. | 
**format** | **str** | This defines the format type of the shipment which is printed. For example Coversheet prints in PDF form. | [optional] 
**carrier_account_id** | **str** | The unique identifier associated with the user&#39;s registered USPS Account which will be required for this batch. User can override this value by defining it at Shipment level. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel. And it varies as per USPS selected services, e.g. LTR, LGENV. User can override this value by defining it at shipment level. | 
**service_id** | **str** | A unique identifier given  to the carrier-specific service which is used for this BulkShipment. User can override this value by defining it at shipment level. | 
**special_services** | [**List[SpecialServiceERRInner]**](SpecialServiceERRInner.md) |  | [optional] 
**shipments** | [**List[ShipmentERRCoversheet]**](ShipmentERRCoversheet.md) |  | 

## Example

```python
from shipping.models.create_bulk_shipments_err_coversheet import CreateBulkShipmentsERRCoversheet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkShipmentsERRCoversheet from a JSON string
create_bulk_shipments_err_coversheet_instance = CreateBulkShipmentsERRCoversheet.from_json(json)
# print the JSON string representation of the object
print(CreateBulkShipmentsERRCoversheet.to_json())

# convert the object into a dict
create_bulk_shipments_err_coversheet_dict = create_bulk_shipments_err_coversheet_instance.to_dict()
# create an instance of CreateBulkShipmentsERRCoversheet from a dict
create_bulk_shipments_err_coversheet_from_dict = CreateBulkShipmentsERRCoversheet.from_dict(create_bulk_shipments_err_coversheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


