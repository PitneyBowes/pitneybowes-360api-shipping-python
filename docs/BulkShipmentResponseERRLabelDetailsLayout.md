# BulkShipmentResponseERRLabelDetailsLayout

 This indicates the layout of the label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | Defines the label size of the Shipment, that is, the Shipping Label is available in different Doc Size. | [optional] 
**type** | **str** |  This indicates the type of the label. | [optional] 

## Example

```python
from shipping.models.bulk_shipment_response_err_label_details_layout import BulkShipmentResponseERRLabelDetailsLayout

# TODO update the JSON string below
json = "{}"
# create an instance of BulkShipmentResponseERRLabelDetailsLayout from a JSON string
bulk_shipment_response_err_label_details_layout_instance = BulkShipmentResponseERRLabelDetailsLayout.from_json(json)
# print the JSON string representation of the object
print(BulkShipmentResponseERRLabelDetailsLayout.to_json())

# convert the object into a dict
bulk_shipment_response_err_label_details_layout_dict = bulk_shipment_response_err_label_details_layout_instance.to_dict()
# create an instance of BulkShipmentResponseERRLabelDetailsLayout from a dict
bulk_shipment_response_err_label_details_layout_from_dict = BulkShipmentResponseERRLabelDetailsLayout.from_dict(bulk_shipment_response_err_label_details_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


