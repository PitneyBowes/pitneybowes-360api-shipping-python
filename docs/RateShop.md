# RateShop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_shipment** | **str** | This defines the date of the Shipment in the format YYYY:MM:DD.,required for future shipment rating | [optional] 
**from_address** | [**RateShopFromAddress**](RateShopFromAddress.md) |  | 
**parcel** | [**RateShopParcel**](RateShopParcel.md) |  | 
**carrier_accounts** | **List[str]** | This provide one or more carrier accounts Ids for rate shop. It can be referred from &#x60;Get Carrier Accounts&#x60; API | [optional] 
**parcel_type** | **str** | Parcel Type required for rating, it&#39;s value can be referred from response of &#x60;Get Parcel Types&#x60; API | [optional] 
**parcel_id** | **str** | &gt;-Parcel Id is optional and required to be given in case of branded parcels which have brandedDimension and/or brandedWeight. If parcel has brandedDimension, in that case user need not to pass dimensionUnit and dimension details(length, width and height) in the parcel object. And if brandedWeight is also available for the parcel then in that case weightUnit and weight need not to be passed  in parcel object | [optional] 
**to_address** | [**SingleRateToAddress**](SingleRateToAddress.md) |  | 
**is_hazmat** | **bool** | isHazmat if set to true,only services which support Hazardous material shipment would be visible in the response | [optional] 

## Example

```python
from shipping.models.rate_shop import RateShop

# TODO update the JSON string below
json = "{}"
# create an instance of RateShop from a JSON string
rate_shop_instance = RateShop.from_json(json)
# print the JSON string representation of the object
print(RateShop.to_json())

# convert the object into a dict
rate_shop_dict = rate_shop_instance.to_dict()
# create an instance of RateShop from a dict
rate_shop_from_dict = RateShop.from_dict(rate_shop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


