# DomesticShipmentResponseV2PrintError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | indicates error code of print | [optional] 
**message** | **str** | Error message if print failed  | [optional] 

## Example

```python
from shipping.models.domestic_shipment_response_v2_print_error import DomesticShipmentResponseV2PrintError

# TODO update the JSON string below
json = "{}"
# create an instance of DomesticShipmentResponseV2PrintError from a JSON string
domestic_shipment_response_v2_print_error_instance = DomesticShipmentResponseV2PrintError.from_json(json)
# print the JSON string representation of the object
print(DomesticShipmentResponseV2PrintError.to_json())

# convert the object into a dict
domestic_shipment_response_v2_print_error_dict = domestic_shipment_response_v2_print_error_instance.to_dict()
# create an instance of DomesticShipmentResponseV2PrintError from a dict
domestic_shipment_response_v2_print_error_from_dict = DomesticShipmentResponseV2PrintError.from_dict(domestic_shipment_response_v2_print_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


