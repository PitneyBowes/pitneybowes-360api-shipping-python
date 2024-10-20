# ReturnLabelSpecialServicesInner

This object is required to pass when to create UPS return label and is optional for FedEx

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_service_id** | **str** | PRL is the return label special service | [optional] 
**input_parameters** | [**List[ReturnLabelSpecialServicesInnerInputParametersInner]**](ReturnLabelSpecialServicesInnerInputParametersInner.md) |  | [optional] 

## Example

```python
from shipping.models.return_label_special_services_inner import ReturnLabelSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelSpecialServicesInner from a JSON string
return_label_special_services_inner_instance = ReturnLabelSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelSpecialServicesInner.to_json())

# convert the object into a dict
return_label_special_services_inner_dict = return_label_special_services_inner_instance.to_dict()
# create an instance of ReturnLabelSpecialServicesInner from a dict
return_label_special_services_inner_from_dict = ReturnLabelSpecialServicesInner.from_dict(return_label_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


