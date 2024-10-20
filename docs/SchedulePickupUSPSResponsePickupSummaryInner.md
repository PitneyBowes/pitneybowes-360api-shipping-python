# SchedulePickupUSPSResponsePickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The service id | [optional] 
**package_count** | **float** | The total number of packages | [optional] 
**total_weight** | **float** | The total weight of the packages | [optional] 
**weight_unit** | **str** | Weight Unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | [optional] 

## Example

```python
from shipping.models.schedule_pickup_usps_response_pickup_summary_inner import SchedulePickupUSPSResponsePickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUSPSResponsePickupSummaryInner from a JSON string
schedule_pickup_usps_response_pickup_summary_inner_instance = SchedulePickupUSPSResponsePickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUSPSResponsePickupSummaryInner.to_json())

# convert the object into a dict
schedule_pickup_usps_response_pickup_summary_inner_dict = schedule_pickup_usps_response_pickup_summary_inner_instance.to_dict()
# create an instance of SchedulePickupUSPSResponsePickupSummaryInner from a dict
schedule_pickup_usps_response_pickup_summary_inner_from_dict = SchedulePickupUSPSResponsePickupSummaryInner.from_dict(schedule_pickup_usps_response_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


