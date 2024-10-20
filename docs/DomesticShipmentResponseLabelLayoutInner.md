# DomesticShipmentResponseLabelLayoutInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | it shows the type of label generated | [optional] 
**contents** | **str** | it shows the label URL of the shipment | [optional] 
**size** | **str** | This defines the label size of the Shipment, e.g., Shipping Label having Doc Size (4&#39; X 6&#39; or 8.5&#39; X 11&#39;). | [optional] 
**type** | **str** | This defines the type of the Shipment, e.g., Shipping Label. | [optional] 
**file_format** | **str** | This defines the type of the shipment which is printed. For example Shipping label prints in PDF form. | [optional] 

## Example

```python
from shipping.models.domestic_shipment_response_label_layout_inner import DomesticShipmentResponseLabelLayoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of DomesticShipmentResponseLabelLayoutInner from a JSON string
domestic_shipment_response_label_layout_inner_instance = DomesticShipmentResponseLabelLayoutInner.from_json(json)
# print the JSON string representation of the object
print(DomesticShipmentResponseLabelLayoutInner.to_json())

# convert the object into a dict
domestic_shipment_response_label_layout_inner_dict = domestic_shipment_response_label_layout_inner_instance.to_dict()
# create an instance of DomesticShipmentResponseLabelLayoutInner from a dict
domestic_shipment_response_label_layout_inner_from_dict = DomesticShipmentResponseLabelLayoutInner.from_dict(domestic_shipment_response_label_layout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


