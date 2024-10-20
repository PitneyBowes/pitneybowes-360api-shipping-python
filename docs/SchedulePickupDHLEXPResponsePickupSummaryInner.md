# SchedulePickupDHLEXPResponsePickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | The service id | [optional] 
**package_count** | **float** | The total number of packages | [optional] 
**total_weight** | **float** | The total weight of the packages | [optional] 
**weight_unit** | **str** | Weight Unit, supported values are &#x60;OZ&#x60; and &#x60;GM&#x60; | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**total_customs_declared_value** | **str** | It indicates the custom declared value. It is required in case of international shipment. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_dhlexp_response_pickup_summary_inner import SchedulePickupDHLEXPResponsePickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupDHLEXPResponsePickupSummaryInner from a JSON string
schedule_pickup_dhlexp_response_pickup_summary_inner_instance = SchedulePickupDHLEXPResponsePickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupDHLEXPResponsePickupSummaryInner.to_json())

# convert the object into a dict
schedule_pickup_dhlexp_response_pickup_summary_inner_dict = schedule_pickup_dhlexp_response_pickup_summary_inner_instance.to_dict()
# create an instance of SchedulePickupDHLEXPResponsePickupSummaryInner from a dict
schedule_pickup_dhlexp_response_pickup_summary_inner_from_dict = SchedulePickupDHLEXPResponsePickupSummaryInner.from_dict(schedule_pickup_dhlexp_response_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


