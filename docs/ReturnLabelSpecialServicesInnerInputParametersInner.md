# ReturnLabelSpecialServicesInnerInputParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | It takes the input parameters. &#x60;RETURN_PKG_DESCRIPTION&#x60; is required for UPS and &#x60;RMA_NUMBER&#x60; for FedEx | [optional] 
**value** | **str** | It specifies the input value | [optional] 

## Example

```python
from shipping.models.return_label_special_services_inner_input_parameters_inner import ReturnLabelSpecialServicesInnerInputParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelSpecialServicesInnerInputParametersInner from a JSON string
return_label_special_services_inner_input_parameters_inner_instance = ReturnLabelSpecialServicesInnerInputParametersInner.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelSpecialServicesInnerInputParametersInner.to_json())

# convert the object into a dict
return_label_special_services_inner_input_parameters_inner_dict = return_label_special_services_inner_input_parameters_inner_instance.to_dict()
# create an instance of ReturnLabelSpecialServicesInnerInputParametersInner from a dict
return_label_special_services_inner_input_parameters_inner_from_dict = ReturnLabelSpecialServicesInnerInputParametersInner.from_dict(return_label_special_services_inner_input_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


