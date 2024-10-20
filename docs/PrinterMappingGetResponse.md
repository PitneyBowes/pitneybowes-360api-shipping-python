# PrinterMappingGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The printer connected (directly or via network) to a computer. | [optional] 
**serial_number** | **str** | A Device Serial number. | [optional] 
**printer_name** | **str** | The Printer name which is used for mapping. | [optional] 
**sub_id** | **str** | The subscription ID used for mapping. | [optional] 
**insert_time_stamp** | **datetime** | It records saved Timestamp. | [optional] 
**update_time_stamp** | **datetime** | It records updated Timestamp. | [optional] 

## Example

```python
from shipping.models.printer_mapping_get_response import PrinterMappingGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterMappingGetResponse from a JSON string
printer_mapping_get_response_instance = PrinterMappingGetResponse.from_json(json)
# print the JSON string representation of the object
print(PrinterMappingGetResponse.to_json())

# convert the object into a dict
printer_mapping_get_response_dict = printer_mapping_get_response_instance.to_dict()
# create an instance of PrinterMappingGetResponse from a dict
printer_mapping_get_response_from_dict = PrinterMappingGetResponse.from_dict(printer_mapping_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


