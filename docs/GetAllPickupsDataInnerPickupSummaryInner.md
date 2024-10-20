# GetAllPickupsDataInnerPickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The service id | [optional] 
**package_count** | **float** | The total number of packages | [optional] 
**total_weight** | **float** | The total weight of the packages | [optional] 
**weight_unit** | **str** | Weight Unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | [optional] 
**parcel_type** | **str** | It indicates the parcel type, applicable values are- &#x60;PKG&#x60;,&#x60;LTR&#x60;,&#x60;TUBE&#x60;,&#x60;PACK&#x60;,&#x60;BOX&#x60;,&#x60;25KG&#x60;,&#x60;10KG&#x60;,&#x60;SMALL_EXP_BOX&#x60;,&#x60;MED_EXP_BOX&#x60;,&#x60;LG_EXP_BOX&#x60; | [optional] 
**to_address_country_code** | **str** | It indicates the 2 characters- ISO country code of recipient of the shipment. | [optional] 
**currency_code** | **str** | Currency code | [optional] 

## Example

```python
from shipping.models.get_all_pickups_data_inner_pickup_summary_inner import GetAllPickupsDataInnerPickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPickupsDataInnerPickupSummaryInner from a JSON string
get_all_pickups_data_inner_pickup_summary_inner_instance = GetAllPickupsDataInnerPickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(GetAllPickupsDataInnerPickupSummaryInner.to_json())

# convert the object into a dict
get_all_pickups_data_inner_pickup_summary_inner_dict = get_all_pickups_data_inner_pickup_summary_inner_instance.to_dict()
# create an instance of GetAllPickupsDataInnerPickupSummaryInner from a dict
get_all_pickups_data_inner_pickup_summary_inner_from_dict = GetAllPickupsDataInnerPickupSummaryInner.from_dict(get_all_pickups_data_inner_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


