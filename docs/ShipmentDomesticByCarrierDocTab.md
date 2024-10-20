# ShipmentDomesticByCarrierDocTab

This option is used to provide additional information into the label's additional space

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | This is an optional field and will be used when the client has multiple doctab options. | [optional] 
**to_address_name** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**parcel_tracking_number** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**carrier** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**service_id** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**date_of_shipment** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**piece_number** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**package_total_carrier_charge** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**total_carrier_charge** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**package_weight** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**total_weight** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**custom_field1** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**custom_field2** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**custom_field3** | [**DocTabItem**](DocTabItem.md) |  | [optional] 
**custom_field4** | [**DocTabItem**](DocTabItem.md) |  | [optional] 

## Example

```python
from shipping.models.shipment_domestic_by_carrier_doc_tab import ShipmentDomesticByCarrierDocTab

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticByCarrierDocTab from a JSON string
shipment_domestic_by_carrier_doc_tab_instance = ShipmentDomesticByCarrierDocTab.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticByCarrierDocTab.to_json())

# convert the object into a dict
shipment_domestic_by_carrier_doc_tab_dict = shipment_domestic_by_carrier_doc_tab_instance.to_dict()
# create an instance of ShipmentDomesticByCarrierDocTab from a dict
shipment_domestic_by_carrier_doc_tab_from_dict = ShipmentDomesticByCarrierDocTab.from_dict(shipment_domestic_by_carrier_doc_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


