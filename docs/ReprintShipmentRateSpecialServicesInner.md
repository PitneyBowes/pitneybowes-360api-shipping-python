# ReprintShipmentRateSpecialServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The amount of the specialSevice. | [optional] 
**input_parameters** | [**List[GetSingleShipmentRateSpecialServicesInnerInputParametersInner]**](GetSingleShipmentRateSpecialServicesInnerInputParametersInner.md) | &gt;-The parameters to set for the special service, such as an insurance value or a receipt-number format. This is required if the specialservice requires input parameters. If a special service does not require input parameters, you can either leave out the array or pass an empty array. | [optional] 
**special_service_id** | **str** | A unique identifier associated to the Special Service , which depends on the carrier based service. | [optional] 

## Example

```python
from shipping.models.reprint_shipment_rate_special_services_inner import ReprintShipmentRateSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintShipmentRateSpecialServicesInner from a JSON string
reprint_shipment_rate_special_services_inner_instance = ReprintShipmentRateSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(ReprintShipmentRateSpecialServicesInner.to_json())

# convert the object into a dict
reprint_shipment_rate_special_services_inner_dict = reprint_shipment_rate_special_services_inner_instance.to_dict()
# create an instance of ReprintShipmentRateSpecialServicesInner from a dict
reprint_shipment_rate_special_services_inner_from_dict = ReprintShipmentRateSpecialServicesInner.from_dict(reprint_shipment_rate_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


