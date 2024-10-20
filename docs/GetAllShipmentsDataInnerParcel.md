# GetAllShipmentsDataInnerParcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height is a part of Dimension objet where it helps determine a parcel’s girth. | 
**length** | **float** | Length is a part of Dimension objet having highest numeric value out of three required parameters (length, width, and height) of Dimension. It helps determine a parcel’s girth. | 
**width** | **float** | Width is a part of Dimension object having lowest numeric value out of three required parameters of dimension (length, width, and height). This helps determine a parcel’s girth. | 
**dim_unit** | **str** | DimUnit is a standard for measuring the physical quantities of specified dimension parameters. | 
**weight_unit** | **str** | WeightUnit is a standard for measuring the physical quantities of specified weight. | 
**weight** | **float** |  | 

## Example

```python
from shipping.models.get_all_shipments_data_inner_parcel import GetAllShipmentsDataInnerParcel

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllShipmentsDataInnerParcel from a JSON string
get_all_shipments_data_inner_parcel_instance = GetAllShipmentsDataInnerParcel.from_json(json)
# print the JSON string representation of the object
print(GetAllShipmentsDataInnerParcel.to_json())

# convert the object into a dict
get_all_shipments_data_inner_parcel_dict = get_all_shipments_data_inner_parcel_instance.to_dict()
# create an instance of GetAllShipmentsDataInnerParcel from a dict
get_all_shipments_data_inner_parcel_from_dict = GetAllShipmentsDataInnerParcel.from_dict(get_all_shipments_data_inner_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


