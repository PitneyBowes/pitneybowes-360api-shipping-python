# SchedulePickupUPSResponsePickupRateSurchargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | It displays the surcharge which is applied | [optional] 
**fee** | **float** | It displays the surcharge fee which is applied | [optional] 

## Example

```python
from shipping.models.schedule_pickup_ups_response_pickup_rate_surcharges_inner import SchedulePickupUPSResponsePickupRateSurchargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUPSResponsePickupRateSurchargesInner from a JSON string
schedule_pickup_ups_response_pickup_rate_surcharges_inner_instance = SchedulePickupUPSResponsePickupRateSurchargesInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUPSResponsePickupRateSurchargesInner.to_json())

# convert the object into a dict
schedule_pickup_ups_response_pickup_rate_surcharges_inner_dict = schedule_pickup_ups_response_pickup_rate_surcharges_inner_instance.to_dict()
# create an instance of SchedulePickupUPSResponsePickupRateSurchargesInner from a dict
schedule_pickup_ups_response_pickup_rate_surcharges_inner_from_dict = SchedulePickupUPSResponsePickupRateSurchargesInner.from_dict(schedule_pickup_ups_response_pickup_rate_surcharges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


