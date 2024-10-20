# SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | It indicates the package width | 
**height** | **float** | It indicates the package height | 
**length** | **float** | It indicates the package length | 
**dim_unit** | **str** | It indicates the dimension unit, supported values are &#x60;IN&#x60; and &#x60;CM&#x60; | 
**weight_unit** | **str** | It indicates the weight unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | 
**weight** | **float** | It indicates the package length | 

## Example

```python
from shipping.models.schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner import SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner from a JSON string
schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner_instance = SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner.to_json())

# convert the object into a dict
schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner_dict = schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner_instance.to_dict()
# create an instance of SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner from a dict
schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner_from_dict = SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner.from_dict(schedule_pickup_dhlexp_request_pickup_summary_inner_package_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


