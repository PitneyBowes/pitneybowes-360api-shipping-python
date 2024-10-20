# PrintDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job ID of the printed document. | [optional] 

## Example

```python
from shipping.models.print_document_response import PrintDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrintDocumentResponse from a JSON string
print_document_response_instance = PrintDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(PrintDocumentResponse.to_json())

# convert the object into a dict
print_document_response_dict = print_document_response_instance.to_dict()
# create an instance of PrintDocumentResponse from a dict
print_document_response_from_dict = PrintDocumentResponse.from_dict(print_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


