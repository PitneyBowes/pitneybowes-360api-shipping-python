# ShipmentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_manifest** | **bool** | This option asks if the shipment is to be added for Manifest, so that the shipment will reflect in the Manifest Form while compilation. The value can be &#39;true&#39; or &#39;false&#39;. Applicable for USPS | [optional] 
**print_custom_message** | **str** | This prints a custom message on shipping label | [optional] 
**receipt_option** | **str** | It provides options to print receipt with shipping label. Only applicable for USPS, can take values- RECEIPT_ONLY or RECEIPT_WITH_INSTRUCTIONS or NO_OPTIONS | [optional] 
**print_department** | **str** | This prints department on shipping label, applicable for FedEx | [optional] 
**print_invoice_number** | **str** | This prints invoice number on shipping label, applicable for FedEx | [optional] 
**print_po_number** | **str** | This prints po number on shipping label, applicable for FedEx | [optional] 
**package_description** | **str** | This is required for DHL Express shipment. It is used to provide description of package | [optional] 

## Example

```python
from shipping.models.shipment_options import ShipmentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentOptions from a JSON string
shipment_options_instance = ShipmentOptions.from_json(json)
# print the JSON string representation of the object
print(ShipmentOptions.to_json())

# convert the object into a dict
shipment_options_dict = shipment_options_instance.to_dict()
# create an instance of ShipmentOptions from a dict
shipment_options_from_dict = ShipmentOptions.from_dict(shipment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


