# PrinterMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A Unique ID for the Printer mapper. | [optional] 

## Example

```python
from shipping.models.printer_mapping_response import PrinterMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterMappingResponse from a JSON string
printer_mapping_response_instance = PrinterMappingResponse.from_json(json)
# print the JSON string representation of the object
print(PrinterMappingResponse.to_json())

# convert the object into a dict
printer_mapping_response_dict = printer_mapping_response_instance.to_dict()
# create an instance of PrinterMappingResponse from a dict
printer_mapping_response_from_dict = PrinterMappingResponse.from_dict(printer_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


