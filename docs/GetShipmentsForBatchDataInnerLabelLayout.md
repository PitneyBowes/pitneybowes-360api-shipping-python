# GetShipmentsForBatchDataInnerLabelLayout

Label layout details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_format** | **str** | Defines the format of the document file the print takes. | [optional] 
**print_receipt** | **bool** | This option asks if the receipt is to be printed. | [optional] 
**size** | **str** | Defines the label size of the Shipment, that is, the Shipping Label is available in different Doc Size. | [optional] 
**type** | **str** | This indicates the type of the label | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_data_inner_label_layout import GetShipmentsForBatchDataInnerLabelLayout

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchDataInnerLabelLayout from a JSON string
get_shipments_for_batch_data_inner_label_layout_instance = GetShipmentsForBatchDataInnerLabelLayout.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchDataInnerLabelLayout.to_json())

# convert the object into a dict
get_shipments_for_batch_data_inner_label_layout_dict = get_shipments_for_batch_data_inner_label_layout_instance.to_dict()
# create an instance of GetShipmentsForBatchDataInnerLabelLayout from a dict
get_shipments_for_batch_data_inner_label_layout_from_dict = GetShipmentsForBatchDataInnerLabelLayout.from_dict(get_shipments_for_batch_data_inner_label_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


