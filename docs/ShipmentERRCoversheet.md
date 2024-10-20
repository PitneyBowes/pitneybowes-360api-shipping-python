# ShipmentERRCoversheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | This is a user-defined value provided by users just for their reference. This is for mapping purpose against each shipment. | [optional] 
**from_address** | [**FromAddress**](FromAddress.md) |  | 
**to_address** | [**ToAddress**](ToAddress.md) |  | 
**parcel** | [**Parcel**](Parcel.md) |  | 
**carrier_account_id** | **str** | A unique identifier associated with the user&#39;s registered USPS account which is used by client users while shipment process. | [optional] 
**parcel_type** | **str** | &gt;-Packaging type varies as per USPS selected services, e.g., LTR, LGENV. | [optional] 
**service_id** | **str** | &gt;-A unique identifier given to the carrier-specific service. ERR supports two services: First Class Mail (FCM) and Priority Mail (PM). | [optional] 
**date_of_shipment** | **str** | The date when shipment gets created. | [optional] 
**special_services** | [**List[SpecialServiceERRInner]**](SpecialServiceERRInner.md) |  | [optional] 
**shipment_options** | [**ShipmentOptionsERR**](ShipmentOptionsERR.md) |  | [optional] 
**metadata** | [**List[ShipmentERRCoversheetMetadataInner]**](ShipmentERRCoversheetMetadataInner.md) | Additional metadata that needs to be stored for this shipment, can be added here. For now, &#x60;costAccountName&#x60; is supported. | [optional] 

## Example

```python
from shipping.models.shipment_err_coversheet import ShipmentERRCoversheet

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentERRCoversheet from a JSON string
shipment_err_coversheet_instance = ShipmentERRCoversheet.from_json(json)
# print the JSON string representation of the object
print(ShipmentERRCoversheet.to_json())

# convert the object into a dict
shipment_err_coversheet_dict = shipment_err_coversheet_instance.to_dict()
# create an instance of ShipmentERRCoversheet from a dict
shipment_err_coversheet_from_dict = ShipmentERRCoversheet.from_dict(shipment_err_coversheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


