# CreateBulkShipmentsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**size** | **str** | This indicates the label size of the Bulk Shipment, e.g., DocSize can be 8&#39; X 11&#39;. | 
**type** | **str** | This indicates the type of the Batch Shipment, e.g., Shipping Label. | 
**format** | **str** | This defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form. | [optional] 
**name** | **str** |  | 
**carrier_account_id** | **str** | Default &#x60;carrierAccountId&#x60; to be used for this batch. You can override this value by defining it at shipment level. | 
**parcel_type** | **str** | Default &#x60;parcelType&#x60; specific to the carrier, e.g., FRPKG, LGENV, TUBE,PKG to be used for this batch. You can override this value by defining it at shipment level. | 
**service_id** | **str** | Default abbreviated name &#x60;serviceId&#x60; of the carrier-specific service to be used for this batch. You can override this value by defining it at shipment level. | 
**special_services** | [**List[SpecialService]**](SpecialService.md) | Default &#x60;specialServices&#x60; to be used for this batch. You can override this value by defining it at shipment level. | [optional] 
**shipments** | [**List[ShipmentInternational]**](ShipmentInternational.md) |  | 

## Example

```python
from shipping.models.create_bulk_shipments_api_request import CreateBulkShipmentsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkShipmentsAPIRequest from a JSON string
create_bulk_shipments_api_request_instance = CreateBulkShipmentsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBulkShipmentsAPIRequest.to_json())

# convert the object into a dict
create_bulk_shipments_api_request_dict = create_bulk_shipments_api_request_instance.to_dict()
# create an instance of CreateBulkShipmentsAPIRequest from a dict
create_bulk_shipments_api_request_from_dict = CreateBulkShipmentsAPIRequest.from_dict(create_bulk_shipments_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


