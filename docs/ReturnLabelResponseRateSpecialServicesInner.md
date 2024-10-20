# ReturnLabelResponseRateSpecialServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_service_id** | **str** | Description | [optional] 
**input_parameters** | [**List[ReturnLabelResponseRateSpecialServicesInnerInputParametersInner]**](ReturnLabelResponseRateSpecialServicesInnerInputParametersInner.md) |  | [optional] 
**fee** | **float** | Description | [optional] 

## Example

```python
from shipping.models.return_label_response_rate_special_services_inner import ReturnLabelResponseRateSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelResponseRateSpecialServicesInner from a JSON string
return_label_response_rate_special_services_inner_instance = ReturnLabelResponseRateSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelResponseRateSpecialServicesInner.to_json())

# convert the object into a dict
return_label_response_rate_special_services_inner_dict = return_label_response_rate_special_services_inner_instance.to_dict()
# create an instance of ReturnLabelResponseRateSpecialServicesInner from a dict
return_label_response_rate_special_services_inner_from_dict = ReturnLabelResponseRateSpecialServicesInner.from_dict(return_label_response_rate_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


