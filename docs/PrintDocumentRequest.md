# PrintDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer_alias_name** | **str** | Name of the Printer connected (directly or via network) to a Computer. &#x60;Max length &#x3D; 30&#x60; | 
**data** | **str** | Content/Identifier of document e.g. DOCUMENT_REFERECE_ID. Actual document name e.g. abc.pdf. [IN] i.e base64 string, URL, file path | 
**data_type** | **str** | Data Type of the document e.g. DOCUMENT_REFERENCE. [IN/OUT] | 
**document_type** | **str** | The format of the document file the print takes. | 
**form_name** | **str** | The name of the Document Form. | 
**orientation** | **str** | The orientation of the document layout: Portrait or Landscape. | [optional] 
**reference** | [**PrintDocumentRequestReference**](PrintDocumentRequestReference.md) |  | [optional] 

## Example

```python
from shipping.models.print_document_request import PrintDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintDocumentRequest from a JSON string
print_document_request_instance = PrintDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(PrintDocumentRequest.to_json())

# convert the object into a dict
print_document_request_dict = print_document_request_instance.to_dict()
# create an instance of PrintDocumentRequest from a dict
print_document_request_from_dict = PrintDocumentRequest.from_dict(print_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


