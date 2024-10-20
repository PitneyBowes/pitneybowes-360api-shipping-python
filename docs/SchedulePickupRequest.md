# SchedulePickupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_location** | **str** | It specifies the location from where packages would be collected. Applicable values are &#x60;FRONT&#x60;,&#x60;NONE&#x60;,&#x60;SIDE&#x60;,&#x60;REAR&#x60; | 
**carrier_account_id** | **str** | It specifies the carrier account id, its value can be referenced from the &#x60;Get Carrier Accounts&#x60; API. | 
**pickup_address** | [**SchedulePickupDHLEXPRequestPickupAddress**](SchedulePickupDHLEXPRequestPickupAddress.md) |  | 
**shipment_ids** | **List[str]** | It indicates the shipmentIds for which pickup to be scheduled. | [optional] 
**pickup_summary** | [**List[SchedulePickupFedexRequestPickupSummaryInner]**](SchedulePickupFedexRequestPickupSummaryInner.md) | This can be used to add package details for which labels are not created yet but would want to schedule pickup in advance. | [optional] 
**additionalnotes** | **str** | It can be used to provide any additional comments or remarks, it would be printed on the scheduled pickup document. | [optional] 
**reference** | **str** | It is used for any reference purpose | [optional] 
**pickup_options** | [**SchedulePickupFedexRequestPickupOptions**](SchedulePickupFedexRequestPickupOptions.md) |  | 

## Example

```python
from shipping.models.schedule_pickup_request import SchedulePickupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupRequest from a JSON string
schedule_pickup_request_instance = SchedulePickupRequest.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupRequest.to_json())

# convert the object into a dict
schedule_pickup_request_dict = schedule_pickup_request_instance.to_dict()
# create an instance of SchedulePickupRequest from a dict
schedule_pickup_request_from_dict = SchedulePickupRequest.from_dict(schedule_pickup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


