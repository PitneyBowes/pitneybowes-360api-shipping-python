# InternationalShipmentResponseRateSpecialServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The amount of the special service. | [optional] 
**input_parameters** | [**List[InternationalShipmentResponseRateSpecialServicesInnerInputParametersInner]**](InternationalShipmentResponseRateSpecialServicesInnerInputParametersInner.md) | &gt;-The parameters to set for the special service, such as an insurance value or a receipt-number format. This is required if the specialservice requires input parameters. If a special service does not require input parameters, you can either leave out the array or pass an empty array. | [optional] 
**special_service_id** | **str** | This is the unique identifier given to various specialservice, which is used while Rating. | [optional] 

## Example

```python
from shipping.models.international_shipment_response_rate_special_services_inner import InternationalShipmentResponseRateSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalShipmentResponseRateSpecialServicesInner from a JSON string
international_shipment_response_rate_special_services_inner_instance = InternationalShipmentResponseRateSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(InternationalShipmentResponseRateSpecialServicesInner.to_json())

# convert the object into a dict
international_shipment_response_rate_special_services_inner_dict = international_shipment_response_rate_special_services_inner_instance.to_dict()
# create an instance of InternationalShipmentResponseRateSpecialServicesInner from a dict
international_shipment_response_rate_special_services_inner_from_dict = InternationalShipmentResponseRateSpecialServicesInner.from_dict(international_shipment_response_rate_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


