# SchedulePickupDHLEXPRequestPickupOptions

It is used to provide any pickup options while scheduling pickups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_start_date_time** | **str** | It specifies the earliest date and time that your parcels will be available for pickup (UTC time) | 
**pickup_end_date_time** | **str** | It specifies the latest date and time that your parcels will be available for pickup (UTC time) | 

## Example

```python
from shipping.models.schedule_pickup_dhlexp_request_pickup_options import SchedulePickupDHLEXPRequestPickupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupDHLEXPRequestPickupOptions from a JSON string
schedule_pickup_dhlexp_request_pickup_options_instance = SchedulePickupDHLEXPRequestPickupOptions.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupDHLEXPRequestPickupOptions.to_json())

# convert the object into a dict
schedule_pickup_dhlexp_request_pickup_options_dict = schedule_pickup_dhlexp_request_pickup_options_instance.to_dict()
# create an instance of SchedulePickupDHLEXPRequestPickupOptions from a dict
schedule_pickup_dhlexp_request_pickup_options_from_dict = SchedulePickupDHLEXPRequestPickupOptions.from_dict(schedule_pickup_dhlexp_request_pickup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


