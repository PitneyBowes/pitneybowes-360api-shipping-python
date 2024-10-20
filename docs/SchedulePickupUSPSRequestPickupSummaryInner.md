# SchedulePickupUSPSRequestPickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The service id | 
**package_count** | **float** | The total number of packages | 
**total_weight** | **float** | The total weight of the packages | 
**weight_unit** | **str** | Weight Unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | 

## Example

```python
from shipping.models.schedule_pickup_usps_request_pickup_summary_inner import SchedulePickupUSPSRequestPickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUSPSRequestPickupSummaryInner from a JSON string
schedule_pickup_usps_request_pickup_summary_inner_instance = SchedulePickupUSPSRequestPickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUSPSRequestPickupSummaryInner.to_json())

# convert the object into a dict
schedule_pickup_usps_request_pickup_summary_inner_dict = schedule_pickup_usps_request_pickup_summary_inner_instance.to_dict()
# create an instance of SchedulePickupUSPSRequestPickupSummaryInner from a dict
schedule_pickup_usps_request_pickup_summary_inner_from_dict = SchedulePickupUSPSRequestPickupSummaryInner.from_dict(schedule_pickup_usps_request_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


