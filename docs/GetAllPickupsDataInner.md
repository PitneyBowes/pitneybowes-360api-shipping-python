# GetAllPickupsDataInner


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
**pickup_summary** | [**List[GetAllPickupsDataInnerPickupSummaryInner]**](GetAllPickupsDataInnerPickupSummaryInner.md) | It displays the package details provided in the request. | [optional] 
**special_instructions** | **str** | It displays additional comments or remarks provided in the request, it would be printed on the scheduled pickup document | [optional] 
**reference** | **str** | It displays any reference information provided in the request. | [optional] 
**pickup_date_time** | **str** | It displays the scheduled pickup date and time (in UTC) | [optional] 
**pickup_total_weight** | **float** | It displays the total package weight. | [optional] 
**pickup_total_weight_unit** | **str** | It displays the weight unit. | [optional] 
**pickup_options** | [**GetAllPickupsDataInnerPickupOptions**](GetAllPickupsDataInnerPickupOptions.md) |  | [optional] 
**pickup_rate** | [**SchedulePickupUPSResponsePickupRate**](SchedulePickupUPSResponsePickupRate.md) |  | [optional] 

## Example

```python
from shipping.models.get_all_pickups_data_inner import GetAllPickupsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPickupsDataInner from a JSON string
get_all_pickups_data_inner_instance = GetAllPickupsDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAllPickupsDataInner.to_json())

# convert the object into a dict
get_all_pickups_data_inner_dict = get_all_pickups_data_inner_instance.to_dict()
# create an instance of GetAllPickupsDataInner from a dict
get_all_pickups_data_inner_from_dict = GetAllPickupsDataInner.from_dict(get_all_pickups_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


