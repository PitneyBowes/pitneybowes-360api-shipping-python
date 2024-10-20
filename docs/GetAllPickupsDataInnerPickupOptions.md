# GetAllPickupsDataInnerPickupOptions

It is used to provide any pickup options while scheduling pickups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_start_date_time** | **str** | It specifies the earliest date and time that your parcels will be available for pickup (UTC time) | [optional] 
**pickup_end_date_time** | **str** | It specifies the latest date and time that your parcels will be available for pickup (UTC time) | [optional] 
**overweight** | **float** | It specifies the count of packages which are overwight (weight&gt; 70 lbs) | [optional] 
**carrier_type** | **str** | It specifies the type of pickup service - &#x60;Ground&#x60; or &#x60;Express&#x60;. Choose &#x60;Ground&#x60; to schedule pickup for next business day or up to two weeks later for Ground packages only (i.e. GRD,HOM,STD,SP_MEDIA,SP_PRCLSEL,SP_PRE_PRINT,SP_PRE_STD,SP_RETURNS). Choose &#x60;Express&#x60; to schedule pickup a same day or a next day pickup for express packages only (i.e. NDA_AM,NDA,NDA_SVR,NDA_AM_EH,NDA_EH,NDA_SVR_EH,2DA_AM,2DA,3DA,XPP,EXP,EXP_X,EXP_CP,XPD). | [optional] 

## Example

```python
from shipping.models.get_all_pickups_data_inner_pickup_options import GetAllPickupsDataInnerPickupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPickupsDataInnerPickupOptions from a JSON string
get_all_pickups_data_inner_pickup_options_instance = GetAllPickupsDataInnerPickupOptions.from_json(json)
# print the JSON string representation of the object
print(GetAllPickupsDataInnerPickupOptions.to_json())

# convert the object into a dict
get_all_pickups_data_inner_pickup_options_dict = get_all_pickups_data_inner_pickup_options_instance.to_dict()
# create an instance of GetAllPickupsDataInnerPickupOptions from a dict
get_all_pickups_data_inner_pickup_options_from_dict = GetAllPickupsDataInnerPickupOptions.from_dict(get_all_pickups_data_inner_pickup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


