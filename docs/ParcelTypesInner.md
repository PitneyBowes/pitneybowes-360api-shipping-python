# ParcelTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branded_name** | **str** | The branded name of parcel type | [optional] 
**carrier** | **str** | A unique identifier associated with the specific carrier. | [optional] 
**dimension_rules** | [**List[ParcelTypesInnerDimensionRulesInner]**](ParcelTypesInnerDimensionRulesInner.md) | This defines the maximum and minimum dimension supported for given parcel type. | [optional] 
**group_name** | **str** |  | [optional] 
**branded_dimensions** | [**ParcelTypesInnerBrandedDimensions**](ParcelTypesInnerBrandedDimensions.md) |  | [optional] 
**parcel_id** | **str** | A unique identifier associated with the Parcel type. | [optional] 
**is_branded** | **bool** | If the Parcel is Branded. If yees, it will take &#x60;true&#x60;, else will take &#x60;false&#x60;. | [optional] 
**parcel_type** | **str** | This defines the type of Parcel. | [optional] 
**service_id** | **str** | A unique identifier associated with the carrier based service. | [optional] 
**service_name** | **str** | Name of the Carrier Service. | [optional] 
**suggested_trackable_specialservice_id** | **str** | This defines the parcel has feature to track special serviceID. | [optional] 
**weight_rules** | [**List[ParcelTypesInnerWeightRulesInner]**](ParcelTypesInnerWeightRulesInner.md) | This defines the maximum and minimum weight supported for given parcel type. | [optional] 

## Example

```python
from shipping.models.parcel_types_inner import ParcelTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypesInner from a JSON string
parcel_types_inner_instance = ParcelTypesInner.from_json(json)
# print the JSON string representation of the object
print(ParcelTypesInner.to_json())

# convert the object into a dict
parcel_types_inner_dict = parcel_types_inner_instance.to_dict()
# create an instance of ParcelTypesInner from a dict
parcel_types_inner_from_dict = ParcelTypesInner.from_dict(parcel_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


