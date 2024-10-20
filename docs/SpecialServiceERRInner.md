# SpecialServiceERRInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specialservice_id** | **str** | A unique identifier associated with the Special Service, will be mentioned in this column. If user selects additional service will be entered here. | [optional] 

## Example

```python
from shipping.models.special_service_err_inner import SpecialServiceERRInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceERRInner from a JSON string
special_service_err_inner_instance = SpecialServiceERRInner.from_json(json)
# print the JSON string representation of the object
print(SpecialServiceERRInner.to_json())

# convert the object into a dict
special_service_err_inner_dict = special_service_err_inner_instance.to_dict()
# create an instance of SpecialServiceERRInner from a dict
special_service_err_inner_from_dict = SpecialServiceERRInner.from_dict(special_service_err_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


