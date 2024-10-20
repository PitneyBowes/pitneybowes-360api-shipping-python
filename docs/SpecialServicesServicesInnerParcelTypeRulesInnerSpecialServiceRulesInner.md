# SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specialservice_id** | **str** | It display the unique id of the special service | [optional] 
**branded_name** | **str** | The brand name of the special service. | [optional] 
**category_id** | **str** | The unique identifier associated with the special service based on the category. | [optional] 
**category_name** | **str** | The special service is categorized with some name and rules, It indicates the category name of the special service. | [optional] 
**incompatible_special_services** | **List[str]** | Indicates non-compatible special services with this special service | [optional] 
**input_parameter_rules** | [**List[SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInnerInputParameterRulesInner]**](SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInnerInputParameterRulesInner.md) | The rules defined for input parameters for this special service | [optional] 
**prerequisite_rules** | [**List[SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInnerPrerequisiteRulesInner]**](SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInnerPrerequisiteRulesInner.md) | It displays other pre-requisite special services for this special service | [optional] 
**trackable** | **bool** | If this special service is trackable or not | [optional] 

## Example

```python
from shipping.models.special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner import SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner from a JSON string
special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner_instance = SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner.from_json(json)
# print the JSON string representation of the object
print(SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner.to_json())

# convert the object into a dict
special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner_dict = special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner_instance.to_dict()
# create an instance of SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner from a dict
special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner_from_dict = SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner.from_dict(special_services_services_inner_parcel_type_rules_inner_special_service_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


