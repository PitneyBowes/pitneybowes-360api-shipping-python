# ParcelV2

The details of the Parcel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Length is always the greatest of the three dimensions. The other two dimensions are used in the calculation of the girth. | [optional] 
**width** | **float** | There is no strict rule as to which element is the width or the height, but the width is the second greatest dimension of a parcel by convention. | [optional] 
**height** | **float** | By convention the height is the smallest dimension of the parcel. | [optional] 
**dim_unit** | **str** | DimUnit is a standard for measuring the physical quantities of specified dimension parameters.&lt;br /&gt; The valid values are: Inch and Centimeter. | [optional] 
**weight_unit** | **str** | WeightUnit is a standard for measuring the physical quantities of specified weight.&lt;br /&gt; The valid values are: Ounces and Grams.&lt;br /&gt; For USPS shipments, set this to OZ. | 
**weight** | **float** | Weight measures the heaviness of an object (how heavy an object is) . | [optional] 
**package_value** | **float** | Indicates value of the package. | [optional] 

## Example

```python
from shipping.models.parcel_v2 import ParcelV2

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelV2 from a JSON string
parcel_v2_instance = ParcelV2.from_json(json)
# print the JSON string representation of the object
print(ParcelV2.to_json())

# convert the object into a dict
parcel_v2_dict = parcel_v2_instance.to_dict()
# create an instance of ParcelV2 from a dict
parcel_v2_from_dict = ParcelV2.from_dict(parcel_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


