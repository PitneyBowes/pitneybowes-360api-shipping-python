# PrinterMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Name of the printer connected (directly or via network) to a computer. | 
**serial_number** | **str** | A Device Serial number. | 
**printer_name** | **str** | The Printer name which is used for mapping. | 

## Example

```python
from shipping.models.printer_mapping_request import PrinterMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterMappingRequest from a JSON string
printer_mapping_request_instance = PrinterMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PrinterMappingRequest.to_json())

# convert the object into a dict
printer_mapping_request_dict = printer_mapping_request_instance.to_dict()
# create an instance of PrinterMappingRequest from a dict
printer_mapping_request_from_dict = PrinterMappingRequest.from_dict(printer_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


