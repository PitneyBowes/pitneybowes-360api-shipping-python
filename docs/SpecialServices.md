# SpecialServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[SpecialServicesServicesInner]**](SpecialServicesServicesInner.md) |  | [optional] 

## Example

```python
from shipping.models.special_services import SpecialServices

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServices from a JSON string
special_services_instance = SpecialServices.from_json(json)
# print the JSON string representation of the object
print(SpecialServices.to_json())

# convert the object into a dict
special_services_dict = special_services_instance.to_dict()
# create an instance of SpecialServices from a dict
special_services_from_dict = SpecialServices.from_dict(special_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


