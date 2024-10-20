# SchedulePickupUPSResponsePickupOptions

It is used to provide any pickup options while scheduling pickups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_start_date_time** | **str** | It specifies the earliest date and time that your parcels will be available for pickup (UTC time) | [optional] 
**pickup_end_date_time** | **str** | It specifies the latest date and time that your parcels will be available for pickup (UTC time) | [optional] 
**overweight** | **float** | It specifies the count of packages which are overwight (weight&gt; 70 lbs) | [optional] 

## Example

```python
from shipping.models.schedule_pickup_ups_response_pickup_options import SchedulePickupUPSResponsePickupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUPSResponsePickupOptions from a JSON string
schedule_pickup_ups_response_pickup_options_instance = SchedulePickupUPSResponsePickupOptions.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUPSResponsePickupOptions.to_json())

# convert the object into a dict
schedule_pickup_ups_response_pickup_options_dict = schedule_pickup_ups_response_pickup_options_instance.to_dict()
# create an instance of SchedulePickupUPSResponsePickupOptions from a dict
schedule_pickup_ups_response_pickup_options_from_dict = SchedulePickupUPSResponsePickupOptions.from_dict(schedule_pickup_ups_response_pickup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


