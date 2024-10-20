# SchedulePickupUPSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_location** | **str** | It specifies the location from where packages would be collected. | [optional] 
**pickup_confirmation_number** | **str** | It displays the unique confirmation number of the pickup | [optional] 
**pickup_id** | **str** | It displays the unique pickup Id which can be further used to get scheduled PDF and cancel pdf if required. | [optional] 
**carrier** | **str** | It dispays the carrier | [optional] 
**carrier_account_id** | **str** | It displays the carrier acount id which is used to create the shipment | [optional] 
**pickup_address** | [**SchedulePickupDHLEXPResponsePickupAddress**](SchedulePickupDHLEXPResponsePickupAddress.md) |  | [optional] 
**shipment_ids** | **List[str]** | It indicates the shipmentIds for which pickup is scheduled. | [optional] 
**pickup_summary** | [**List[SchedulePickupUPSResponsePickupSummaryInner]**](SchedulePickupUPSResponsePickupSummaryInner.md) | It displays the package details provided in the request. | [optional] 
**additionalnotes** | **str** | It displays additional comments or remarks provided in the request, it would be printed on the scheduled pickup document | [optional] 
**reference** | **str** | It displays any reference information provided in the request. | [optional] 
**pickup_date_time** | **str** | It displays the scheduled pickup date and time (in UTC) | [optional] 
**pickup_total_weight** | **float** | It displays the total package weight. | [optional] 
**pickup_total_weight_unit** | **str** | It displays the weight unit. | [optional] 
**pickup_options** | [**SchedulePickupUPSResponsePickupOptions**](SchedulePickupUPSResponsePickupOptions.md) |  | [optional] 
**pickup_rate** | [**SchedulePickupUPSResponsePickupRate**](SchedulePickupUPSResponsePickupRate.md) |  | [optional] 

## Example

```python
from shipping.models.schedule_pickup_ups_response import SchedulePickupUPSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupUPSResponse from a JSON string
schedule_pickup_ups_response_instance = SchedulePickupUPSResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupUPSResponse.to_json())

# convert the object into a dict
schedule_pickup_ups_response_dict = schedule_pickup_ups_response_instance.to_dict()
# create an instance of SchedulePickupUPSResponse from a dict
schedule_pickup_ups_response_from_dict = SchedulePickupUPSResponse.from_dict(schedule_pickup_ups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


