# ParcelTypesInnerWeightRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_weight** | **float** | This defines maximum weight, which can be considered. | [optional] 
**min_weight** | **float** | This defines minimum weight, which can be considered. | [optional] 
**required** | **bool** |  | [optional] 
**unit_of_measurement** | **str** | UnitOfMeasurement is a standard for measuring the physical quantities of specified dimension parameters. | [optional] 

## Example

```python
from shipping.models.parcel_types_inner_weight_rules_inner import ParcelTypesInnerWeightRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypesInnerWeightRulesInner from a JSON string
parcel_types_inner_weight_rules_inner_instance = ParcelTypesInnerWeightRulesInner.from_json(json)
# print the JSON string representation of the object
print(ParcelTypesInnerWeightRulesInner.to_json())

# convert the object into a dict
parcel_types_inner_weight_rules_inner_dict = parcel_types_inner_weight_rules_inner_instance.to_dict()
# create an instance of ParcelTypesInnerWeightRulesInner from a dict
parcel_types_inner_weight_rules_inner_from_dict = ParcelTypesInnerWeightRulesInner.from_dict(parcel_types_inner_weight_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


