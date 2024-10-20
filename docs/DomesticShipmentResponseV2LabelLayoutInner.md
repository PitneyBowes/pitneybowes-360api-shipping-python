# DomesticShipmentResponseV2LabelLayoutInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **str** | Content/Identifier of document e.g. DOCUMENT_REFERECE_ID.&lt;br /&gt; Actual document name e.g. abc.pdf. [IN]. | [optional] 
**file_format** | **str** | Defines the format of the document file the print takes. | [optional] 
**size** | **str** | Defines the label size of the Shipment, that is, the Shipping Label is available in different Doc Size. | [optional] 
**type** | **str** | Defines the type of the Shipment. | [optional] 

## Example

```python
from shipping.models.domestic_shipment_response_v2_label_layout_inner import DomesticShipmentResponseV2LabelLayoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of DomesticShipmentResponseV2LabelLayoutInner from a JSON string
domestic_shipment_response_v2_label_layout_inner_instance = DomesticShipmentResponseV2LabelLayoutInner.from_json(json)
# print the JSON string representation of the object
print(DomesticShipmentResponseV2LabelLayoutInner.to_json())

# convert the object into a dict
domestic_shipment_response_v2_label_layout_inner_dict = domestic_shipment_response_v2_label_layout_inner_instance.to_dict()
# create an instance of DomesticShipmentResponseV2LabelLayoutInner from a dict
domestic_shipment_response_v2_label_layout_inner_from_dict = DomesticShipmentResponseV2LabelLayoutInner.from_dict(domestic_shipment_response_v2_label_layout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


