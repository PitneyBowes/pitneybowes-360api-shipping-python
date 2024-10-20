# SpecialServicesServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 
**branded_name** | **str** | The branded name of the service | [optional] 
**parcel_type_rules** | [**List[SpecialServicesServicesInnerParcelTypeRulesInner]**](SpecialServicesServicesInnerParcelTypeRulesInner.md) | It displays special services for specific parcel type | [optional] 

## Example

```python
from shipping.models.special_services_services_inner import SpecialServicesServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServicesServicesInner from a JSON string
special_services_services_inner_instance = SpecialServicesServicesInner.from_json(json)
# print the JSON string representation of the object
print(SpecialServicesServicesInner.to_json())

# convert the object into a dict
special_services_services_inner_dict = special_services_services_inner_instance.to_dict()
# create an instance of SpecialServicesServicesInner from a dict
special_services_services_inner_from_dict = SpecialServicesServicesInner.from_dict(special_services_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


