# SchedulePickupFedexRequestPickupOptions

It is used to provide any pickup options while scheduling pickups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_start_date_time** | **str** | It specifies the earliest date and time that your parcels will be available for pickup (UTC time) | 
**pickup_end_date_time** | **str** | It specifies the latest date and time that your parcels will be available for pickup (UTC time) | 
**overweight** | **float** | It specifies the count of packages which are overwight (weight&gt; 70 lbs) | [optional] 
**carrier_type** | **str** | It specifies the type of pickup service - &#x60;Ground&#x60; or &#x60;Express&#x60;. &lt;br&gt; &lt;br&gt; Choose &#x60;Ground&#x60; to schedule pickup for next business day or up to two weeks later for Ground packages only (i.e. GRD,HOM,STD,SP_MEDIA,SP_PRCLSEL,SP_PRE_PRINT,SP_PRE_STD,SP_RETURNS). &lt;br&gt; &lt;br&gt; Choose &#x60;Express&#x60; to schedule pickup a same day or a next day pickup for express packages only (i.e. NDA_AM,NDA,NDA_SVR,NDA_AM_EH,NDA_EH,NDA_SVR_EH,2DA_AM,2DA,3DA,XPP,EXP,EXP_X,EXP_CP,XPD). | 

## Example

```python
from shipping.models.schedule_pickup_fedex_request_pickup_options import SchedulePickupFedexRequestPickupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupFedexRequestPickupOptions from a JSON string
schedule_pickup_fedex_request_pickup_options_instance = SchedulePickupFedexRequestPickupOptions.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupFedexRequestPickupOptions.to_json())

# convert the object into a dict
schedule_pickup_fedex_request_pickup_options_dict = schedule_pickup_fedex_request_pickup_options_instance.to_dict()
# create an instance of SchedulePickupFedexRequestPickupOptions from a dict
schedule_pickup_fedex_request_pickup_options_from_dict = SchedulePickupFedexRequestPickupOptions.from_dict(schedule_pickup_fedex_request_pickup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


