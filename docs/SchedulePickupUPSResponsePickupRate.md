# SchedulePickupUPSResponsePickupRate

It displays the pickup rate information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | It displays the base charge for this pickup | [optional] 
**surcharges** | [**List[SchedulePickupUPSResponsePickupRateSurchargesInner]**](SchedulePickupUPSResponsePickupRateSurchargesInner.md) | It displays the surcharges if any for the pickup | [optional] 
**total_carrier_charge** | **float** | It displays the total charge for the pickup including surcharges. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_ups_response_pickup_rate import SchedulePickupUPSResponsePickupRate

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUPSResponsePickupRate from a JSON string
schedule_pickup_ups_response_pickup_rate_instance = SchedulePickupUPSResponsePickupRate.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUPSResponsePickupRate.to_json())

# convert the object into a dict
schedule_pickup_ups_response_pickup_rate_dict = schedule_pickup_ups_response_pickup_rate_instance.to_dict()
# create an instance of SchedulePickupUPSResponsePickupRate from a dict
schedule_pickup_ups_response_pickup_rate_from_dict = SchedulePickupUPSResponsePickupRate.from_dict(schedule_pickup_ups_response_pickup_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


