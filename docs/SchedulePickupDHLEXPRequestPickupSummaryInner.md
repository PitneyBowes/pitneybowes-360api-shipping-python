# SchedulePickupDHLEXPRequestPickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The service id | 
**package_count** | **float** | The total number of packages | 
**total_weight** | **float** | The total weight of the packages | 
**weight_unit** | **str** | Weight Unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | 
**currency_code** | **str** | Currency code | 
**total_customs_declared_value** | **float** | It indicates the custom declared value. It is required in case of international shipment. | [optional] 
**package_details** | [**List[SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner]**](SchedulePickupDHLEXPRequestPickupSummaryInnerPackageDetailsInner.md) | It descibes the individual package details | 

## Example

```python
from shipping.models.schedule_pickup_dhlexp_request_pickup_summary_inner import SchedulePickupDHLEXPRequestPickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupDHLEXPRequestPickupSummaryInner from a JSON string
schedule_pickup_dhlexp_request_pickup_summary_inner_instance = SchedulePickupDHLEXPRequestPickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupDHLEXPRequestPickupSummaryInner.to_json())

# convert the object into a dict
schedule_pickup_dhlexp_request_pickup_summary_inner_dict = schedule_pickup_dhlexp_request_pickup_summary_inner_instance.to_dict()
# create an instance of SchedulePickupDHLEXPRequestPickupSummaryInner from a dict
schedule_pickup_dhlexp_request_pickup_summary_inner_from_dict = SchedulePickupDHLEXPRequestPickupSummaryInner.from_dict(schedule_pickup_dhlexp_request_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


