# ShipmentOptionsERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_manifest** | **bool** | This option asks if the shipment is to be added for Manifest, so that the shipment can be reflected in the Manifest Form while compilation. The value can be &#39;true&#39; or &#39;false&#39;. Applicable for USPS. | [optional] 
**print_custom_message** | **str** | This prints a custom message on the Shipping Label. | [optional] 
**receipt_option** | **str** | It provides options to print receipt with Shipping Label. This is only applicable for USPS, and takes values: &#x60;RECEIPT_ONLY&#x60;, &#x60;RECEIPT_WITH_INSTRUCTIONS&#x60;, or &#x60;NO_OPTIONS&#x60;. | [optional] 
**print_department** | **str** | It displays/prints the Department on the Shipping Label. | [optional] 
**print_invoice_number** | **str** | It displays/prints Invoice Number on the Shipping Label. | [optional] 
**print_po_number** | **str** | It displays/prints PO Number on the Shipping Label. | [optional] 

## Example

```python
from shipping.models.shipment_options_err import ShipmentOptionsERR

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentOptionsERR from a JSON string
shipment_options_err_instance = ShipmentOptionsERR.from_json(json)
# print the JSON string representation of the object
print(ShipmentOptionsERR.to_json())

# convert the object into a dict
shipment_options_err_dict = shipment_options_err_instance.to_dict()
# create an instance of ShipmentOptionsERR from a dict
shipment_options_err_from_dict = ShipmentOptionsERR.from_dict(shipment_options_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


