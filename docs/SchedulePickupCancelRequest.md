# SchedulePickupCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_ids** | **List[str]** | It specifies the pickup Ids for which you would like to cancel the request. Only pickupIds of the same carrier should be provided in the array. | 
**options** | [**List[SchedulePickupCancelRequestOptionsInner]**](SchedulePickupCancelRequestOptionsInner.md) | It is required to be provided for DHL Express pickup cancellation. Both &#x60;REQUESTOR_NAME&#x60; and &#x60;REASON_FOR_CANCEL&#x60; are required for DHL Express. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_cancel_request import SchedulePickupCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupCancelRequest from a JSON string
schedule_pickup_cancel_request_instance = SchedulePickupCancelRequest.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupCancelRequest.to_json())

# convert the object into a dict
schedule_pickup_cancel_request_dict = schedule_pickup_cancel_request_instance.to_dict()
# create an instance of SchedulePickupCancelRequest from a dict
schedule_pickup_cancel_request_from_dict = SchedulePickupCancelRequest.from_dict(schedule_pickup_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


