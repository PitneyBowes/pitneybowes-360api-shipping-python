# DocTabItem

This field will either be part of the request or response payload or will be marked as a custom field. We need to pass this field only if we need to print it on the label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | This is a mandatory field. It will be displayed on the label | [optional] 
**value** | **str** | If the field is part of a request or response, the value will be picked up from there. In the case of custom fields, the user-provided value will be printed. | [optional] 
**row** | **int** | Row Position of the Item. The min value is 1. | [optional] 
**column** | **int** | Column Position of the Item. The min value is 1. | [optional] 

## Example

```python
from shipping.models.doc_tab_item import DocTabItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocTabItem from a JSON string
doc_tab_item_instance = DocTabItem.from_json(json)
# print the JSON string representation of the object
print(DocTabItem.to_json())

# convert the object into a dict
doc_tab_item_dict = doc_tab_item_instance.to_dict()
# create an instance of DocTabItem from a dict
doc_tab_item_from_dict = DocTabItem.from_dict(doc_tab_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


