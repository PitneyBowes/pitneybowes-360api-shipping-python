# ParcelTypesInnerDimensionRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_length_plus_girth** | **float** | This measures the parcel&#39;s maximum length and determine parcel’s girth. | [optional] 
**max_parcel_dimensions** | [**ParcelTypesInnerDimensionRulesInnerMaxParcelDimensions**](ParcelTypesInnerDimensionRulesInnerMaxParcelDimensions.md) |  | [optional] 
**min_length_plus_girth** | **float** | This measures the parcel&#39;s minimum length and determine parcel’s girth. | [optional] 
**min_parcel_dimensions** | [**ParcelTypesInnerDimensionRulesInnerMinParcelDimensions**](ParcelTypesInnerDimensionRulesInnerMinParcelDimensions.md) |  | [optional] 
**required** | **bool** |  | [optional] 
**unit_of_measurement** | **str** | UnitofMesurement is a standard for measuring the physical quantities of specified dimension parameters. | [optional] 

## Example

```python
from shipping.models.parcel_types_inner_dimension_rules_inner import ParcelTypesInnerDimensionRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypesInnerDimensionRulesInner from a JSON string
parcel_types_inner_dimension_rules_inner_instance = ParcelTypesInnerDimensionRulesInner.from_json(json)
# print the JSON string representation of the object
print(ParcelTypesInnerDimensionRulesInner.to_json())

# convert the object into a dict
parcel_types_inner_dimension_rules_inner_dict = parcel_types_inner_dimension_rules_inner_instance.to_dict()
# create an instance of ParcelTypesInnerDimensionRulesInner from a dict
parcel_types_inner_dimension_rules_inner_from_dict = ParcelTypesInnerDimensionRulesInner.from_dict(parcel_types_inner_dimension_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


