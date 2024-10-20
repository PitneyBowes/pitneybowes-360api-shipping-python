# ParcelTypesInnerDimensionRulesInnerMinParcelDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height is a part of Dimension objet where it helps determine a parcel’s girth. | [optional] 
**length** | **float** | Length is a part of Dimension objet having highest numeric value out of three required parameters (length, width, and height) of Dimension. It helps determine a parcel’s girth. | [optional] 
**unit_of_measurement** | **str** | DimUnit is a standard for measuring the physical quantities of specified dimension parameters. | [optional] 
**width** | **float** | Width is a part of Dimension object having lowest numeric value out of three required parameters of dimension (length, width, and height). This helps determine a parcel’s girth. | [optional] 

## Example

```python
from shipping.models.parcel_types_inner_dimension_rules_inner_min_parcel_dimensions import ParcelTypesInnerDimensionRulesInnerMinParcelDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypesInnerDimensionRulesInnerMinParcelDimensions from a JSON string
parcel_types_inner_dimension_rules_inner_min_parcel_dimensions_instance = ParcelTypesInnerDimensionRulesInnerMinParcelDimensions.from_json(json)
# print the JSON string representation of the object
print(ParcelTypesInnerDimensionRulesInnerMinParcelDimensions.to_json())

# convert the object into a dict
parcel_types_inner_dimension_rules_inner_min_parcel_dimensions_dict = parcel_types_inner_dimension_rules_inner_min_parcel_dimensions_instance.to_dict()
# create an instance of ParcelTypesInnerDimensionRulesInnerMinParcelDimensions from a dict
parcel_types_inner_dimension_rules_inner_min_parcel_dimensions_from_dict = ParcelTypesInnerDimensionRulesInnerMinParcelDimensions.from_dict(parcel_types_inner_dimension_rules_inner_min_parcel_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


