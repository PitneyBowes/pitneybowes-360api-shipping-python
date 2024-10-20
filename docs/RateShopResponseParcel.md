# RateShopResponseParcel

Parcel dimension, weight and unit of measurement details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height is a part of Dimension objet where it helps determine a parcel’s girth. | 
**length** | **float** | Length is a part of Dimension objet having highest numeric value out of three required parameters (length, width, and height) of Dimension. It helps determine a parcel’s girth. | 
**width** | **float** | Width is a part of Dimension object having lowest numeric value out of three required parameters of dimension (length, width, and height). This helps determine a parcel’s girth. | 
**dim_unit** | **str** | DimUnit is a standard for measuring the physical quantities of specified dimension parameters. | 
**weight_unit** | **str** | WeightUnit is a standard for measuring the physical quantities of specified weight. | 
**weight** | **float** | Weight is the measure of how heavy an object is. | 

## Example

```python
from shipping.models.rate_shop_response_parcel import RateShopResponseParcel

# TODO update the JSON string below
json = "{}"
# create an instance of RateShopResponseParcel from a JSON string
rate_shop_response_parcel_instance = RateShopResponseParcel.from_json(json)
# print the JSON string representation of the object
print(RateShopResponseParcel.to_json())

# convert the object into a dict
rate_shop_response_parcel_dict = rate_shop_response_parcel_instance.to_dict()
# create an instance of RateShopResponseParcel from a dict
rate_shop_response_parcel_from_dict = RateShopResponseParcel.from_dict(rate_shop_response_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


