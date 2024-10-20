# GetAllShipmentsDataInnerRateSpecialServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The amount of the specialSevice. | [optional] 
**input_parameters** | [**List[GetAllShipmentsDataInnerRateSpecialServicesInnerInputParametersInner]**](GetAllShipmentsDataInnerRateSpecialServicesInnerInputParametersInner.md) | &gt;-The parameters to set for the special service, such as an insurance value or a receipt-number format. This is required if the specialservice requires input parameters. If a special service does not require input parameters, you can either leave out the array or pass an empty array. | [optional] 
**special_service_id** | **str** | A unique identifier associated to the Special Service , which depends on the carrier based service. | [optional] 

## Example

```python
from shipping.models.get_all_shipments_data_inner_rate_special_services_inner import GetAllShipmentsDataInnerRateSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllShipmentsDataInnerRateSpecialServicesInner from a JSON string
get_all_shipments_data_inner_rate_special_services_inner_instance = GetAllShipmentsDataInnerRateSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(GetAllShipmentsDataInnerRateSpecialServicesInner.to_json())

# convert the object into a dict
get_all_shipments_data_inner_rate_special_services_inner_dict = get_all_shipments_data_inner_rate_special_services_inner_instance.to_dict()
# create an instance of GetAllShipmentsDataInnerRateSpecialServicesInner from a dict
get_all_shipments_data_inner_rate_special_services_inner_from_dict = GetAllShipmentsDataInnerRateSpecialServicesInner.from_dict(get_all_shipments_data_inner_rate_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


