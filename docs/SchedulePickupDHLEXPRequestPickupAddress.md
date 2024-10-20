# SchedulePickupDHLEXPRequestPickupAddress

It specifies the address from where your parcels will be available for pickup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the person, It should not contain special character or numeric value | 
**address_line1** | **str** | Address line1 of the pickup address | 
**city_town** | **str** | City of the pickup address | 
**state_province** | **str** | State province of the pickup address | 
**postal_code** | **str** | Postal Code of the pickup address | 
**country_code** | **str** | ISO-2 characters country code | 
**phone** | **str** | Phone number | 
**company** | **str** | Company name of pickup address | [optional] 
**email** | **str** | Email. A Confirmation email will be send to this email id when pickup gets scheduled successfully. | [optional] 

## Example

```python
from shipping.models.schedule_pickup_dhlexp_request_pickup_address import SchedulePickupDHLEXPRequestPickupAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupDHLEXPRequestPickupAddress from a JSON string
schedule_pickup_dhlexp_request_pickup_address_instance = SchedulePickupDHLEXPRequestPickupAddress.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupDHLEXPRequestPickupAddress.to_json())

# convert the object into a dict
schedule_pickup_dhlexp_request_pickup_address_dict = schedule_pickup_dhlexp_request_pickup_address_instance.to_dict()
# create an instance of SchedulePickupDHLEXPRequestPickupAddress from a dict
schedule_pickup_dhlexp_request_pickup_address_from_dict = SchedulePickupDHLEXPRequestPickupAddress.from_dict(schedule_pickup_dhlexp_request_pickup_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


