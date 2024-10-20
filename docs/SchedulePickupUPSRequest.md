# SchedulePickupUPSRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_location** | **str** | It specifies the location from where packages would be collected. Applicable values are &#x60;Front Door&#x60;,&#x60;Back Door&#x60;,&#x60;Side Door&#x60;,&#x60;Shipping&#x60;,&#x60;Receiving&#x60;,&#x60;Knock on Door/Ring Bell&#x60;,&#x60;Mail Room&#x60;,&#x60;Garage&#x60;,&#x60;Office&#x60;,&#x60;Downstairs&#x60;,&#x60;Reception&#x60;,&#x60;In/At Mailbox&#x60;,&#x60;Third Party&#x60;,&#x60;Warehouse&#x60;,&#x60;Other&#x60; | 
**carrier_account_id** | **str** | It specifies the carrier account id, its value can be referenced from the &#x60;Get Carrier Accounts&#x60; API. | 
**pickup_address** | [**SchedulePickupDHLEXPRequestPickupAddress**](SchedulePickupDHLEXPRequestPickupAddress.md) |  | 
**shipment_ids** | **List[str]** | It indicates the shipmentIds for which pickup to be scheduled. | [optional] 
**pickup_summary** | [**List[SchedulePickupUPSRequestPickupSummaryInner]**](SchedulePickupUPSRequestPickupSummaryInner.md) | This can be used to add package details for which labels are not created yet but would want to schedule pickup in advance. | [optional] 
**additionalnotes** | **str** | It can be used to provide any additional comments or remarks, it would be printed on the scheduled pickup document. It is required when packageLocation is set to &#x60;Other&#x60;. | [optional] 
**reference** | **str** | It is used for any reference purpose | [optional] 
**pickup_options** | [**SchedulePickupUPSRequestPickupOptions**](SchedulePickupUPSRequestPickupOptions.md) |  | 

## Example

```python
from shipping.models.schedule_pickup_ups_request import SchedulePickupUPSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUPSRequest from a JSON string
schedule_pickup_ups_request_instance = SchedulePickupUPSRequest.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUPSRequest.to_json())

# convert the object into a dict
schedule_pickup_ups_request_dict = schedule_pickup_ups_request_instance.to_dict()
# create an instance of SchedulePickupUPSRequest from a dict
schedule_pickup_ups_request_from_dict = SchedulePickupUPSRequest.from_dict(schedule_pickup_ups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


