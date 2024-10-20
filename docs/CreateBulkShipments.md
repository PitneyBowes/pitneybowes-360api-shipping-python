# CreateBulkShipments

ShipmentBatch information contains following schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**size** | **str** | This indicates the label size of the Bulk Shipment, e.g., DocSize can be 8&#39; X 11&#39; or 4&#39; X 6&#39;. | 
**type** | **str** | This indicates the type of the Batch Shipment, e.g., Shipping Label. | 
**format** | **str** | This defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form. | [optional] 
**name** | **str** |  | 
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account used by client users during shipment process. Default CarrierAccountID for this batch will be user&#39;s registered carrier account. User can override this value by defining it at shipment level. | 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. Different carriers have different ParcelTypes, e.g., FRPKG, LGENV, TUBE, and PKG. User can override this value by defining it at Shipment level. | 
**service_id** | **str** | A unique identifier given to the carrier-specific service. It varies with carrier selection. This is required for creating a shipment, while it is optional for rating a parcel. User can override this value by defining it at Shipment level. | 
**special_services** | [**List[SpecialService]**](SpecialService.md) | It provides a carrier-service based special or extra service, which also varies based on services and parcel types. User can override this value by defining it at shipment level. | [optional] 
**shipments** | [**List[Shipment]**](Shipment.md) |  | 

## Example

```python
from shipping.models.create_bulk_shipments import CreateBulkShipments

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkShipments from a JSON string
create_bulk_shipments_instance = CreateBulkShipments.from_json(json)
# print the JSON string representation of the object
print(CreateBulkShipments.to_json())

# convert the object into a dict
create_bulk_shipments_dict = create_bulk_shipments_instance.to_dict()
# create an instance of CreateBulkShipments from a dict
create_bulk_shipments_from_dict = CreateBulkShipments.from_dict(create_bulk_shipments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


