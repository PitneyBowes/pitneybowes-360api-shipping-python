# ReprintShipmentV2LabelLayoutInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | This is used to encode binary data as printable text.&lt;br /&gt; ContentType of the document is URL if the fileformat is PDF, while it will be BASE64 if the fileFormat is ZPL2. | [optional] 
**contents** | **str** | Content/Identifier of document e.g. DOCUMENT_REFERECE_ID.&lt;br /&gt; Actual document name e.g. abc.pdf. [IN]. | [optional] 
**file_format** | **str** | Defines the format of the document file the print takes. | [optional] 
**size** | **str** | Defines the label size of the Shipment, that is, the Shipping Label is available in different Doc Size. | [optional] 
**type** | **str** | Defines the type of the Shipment. | [optional] 

## Example

```python
from shipping.models.reprint_shipment_v2_label_layout_inner import ReprintShipmentV2LabelLayoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintShipmentV2LabelLayoutInner from a JSON string
reprint_shipment_v2_label_layout_inner_instance = ReprintShipmentV2LabelLayoutInner.from_json(json)
# print the JSON string representation of the object
print(ReprintShipmentV2LabelLayoutInner.to_json())

# convert the object into a dict
reprint_shipment_v2_label_layout_inner_dict = reprint_shipment_v2_label_layout_inner_instance.to_dict()
# create an instance of ReprintShipmentV2LabelLayoutInner from a dict
reprint_shipment_v2_label_layout_inner_from_dict = ReprintShipmentV2LabelLayoutInner.from_dict(reprint_shipment_v2_label_layout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


