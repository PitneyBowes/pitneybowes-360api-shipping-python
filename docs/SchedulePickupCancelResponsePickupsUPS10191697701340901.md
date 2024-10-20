# SchedulePickupCancelResponsePickupsUPS10191697701340901

It displays the status for this pickup Id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | It displays the status of the Cancellation request- &#x60;cancelled&#x60;. | [optional] 
**cancellation_date** | **str** | It displays the cancellation date. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_cancel_response_pickups_ups10191697701340901 import SchedulePickupCancelResponsePickupsUPS10191697701340901

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupCancelResponsePickupsUPS10191697701340901 from a JSON string
schedule_pickup_cancel_response_pickups_ups10191697701340901_instance = SchedulePickupCancelResponsePickupsUPS10191697701340901.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupCancelResponsePickupsUPS10191697701340901.to_json())

# convert the object into a dict
schedule_pickup_cancel_response_pickups_ups10191697701340901_dict = schedule_pickup_cancel_response_pickups_ups10191697701340901_instance.to_dict()
# create an instance of SchedulePickupCancelResponsePickupsUPS10191697701340901 from a dict
schedule_pickup_cancel_response_pickups_ups10191697701340901_from_dict = SchedulePickupCancelResponsePickupsUPS10191697701340901.from_dict(schedule_pickup_cancel_response_pickups_ups10191697701340901_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


