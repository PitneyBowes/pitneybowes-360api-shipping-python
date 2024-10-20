# SchedulePickupCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickups** | [**SchedulePickupCancelResponsePickups**](SchedulePickupCancelResponsePickups.md) |  | [optional] 

## Example

```python
from shipping.models.schedule_pickup_cancel_response import SchedulePickupCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupCancelResponse from a JSON string
schedule_pickup_cancel_response_instance = SchedulePickupCancelResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupCancelResponse.to_json())

# convert the object into a dict
schedule_pickup_cancel_response_dict = schedule_pickup_cancel_response_instance.to_dict()
# create an instance of SchedulePickupCancelResponse from a dict
schedule_pickup_cancel_response_from_dict = SchedulePickupCancelResponse.from_dict(schedule_pickup_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


