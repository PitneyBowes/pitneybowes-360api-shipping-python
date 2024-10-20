# SchedulePickupCancelRequestOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | It specifies name of the requestor and reson for the cancellation. | [optional] 
**value** | **str** | It specifies the value for the given name input. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_cancel_request_options_inner import SchedulePickupCancelRequestOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupCancelRequestOptionsInner from a JSON string
schedule_pickup_cancel_request_options_inner_instance = SchedulePickupCancelRequestOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupCancelRequestOptionsInner.to_json())

# convert the object into a dict
schedule_pickup_cancel_request_options_inner_dict = schedule_pickup_cancel_request_options_inner_instance.to_dict()
# create an instance of SchedulePickupCancelRequestOptionsInner from a dict
schedule_pickup_cancel_request_options_inner_from_dict = SchedulePickupCancelRequestOptionsInner.from_dict(schedule_pickup_cancel_request_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


