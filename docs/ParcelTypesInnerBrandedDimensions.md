# ParcelTypesInnerBrandedDimensions

This will be available for parcels with Parcel Type as branded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**girth** | **float** | This is the measure around parcel by area or circumference. | [optional] 
**height** | **float** | Height is a part of Dimension objet where it helps determine a parcel’s girth. | [optional] 
**length** | **float** | Length is a part of Dimension objet having highest numeric value out of three required parameters (length, width, and height) of Dimension. It helps determine a parcel’s girth. | [optional] 
**unit_of_measurement** | **str** | UnitofMesurements is a standard for measuring the physical quantities of specified dimension parameters. | [optional] 
**width** | **float** | Width is a part of Dimension object having lowest numeric value out of three required parameters of dimension (length, width, and height). This helps determine a parcel’s girth. | [optional] 

## Example

```python
from shipping.models.parcel_types_inner_branded_dimensions import ParcelTypesInnerBrandedDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypesInnerBrandedDimensions from a JSON string
parcel_types_inner_branded_dimensions_instance = ParcelTypesInnerBrandedDimensions.from_json(json)
# print the JSON string representation of the object
print(ParcelTypesInnerBrandedDimensions.to_json())

# convert the object into a dict
parcel_types_inner_branded_dimensions_dict = parcel_types_inner_branded_dimensions_instance.to_dict()
# create an instance of ParcelTypesInnerBrandedDimensions from a dict
parcel_types_inner_branded_dimensions_from_dict = ParcelTypesInnerBrandedDimensions.from_dict(parcel_types_inner_branded_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


