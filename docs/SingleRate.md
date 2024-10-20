# SingleRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_shipment** | **str** | This defines the date of the Shipment in the format YYYY:MM:DD, required for future shipment rating | [optional] 
**from_address** | [**SingleRateFromAddress**](SingleRateFromAddress.md) |  | 
**parcel** | [**SingleRateParcel**](SingleRateParcel.md) |  | 
**carrier_accounts** | **List[str]** |  This provides a single carrier account Id in case of single rate request. It can be referred from response of &#x60;Get Carrier Accounts&#x60; API. | 
**parcel_type** | **str** | Parcel Type its value can be referred from response of &#x60;Get Parcel Types&#x60; API. | 
**parcel_id** | **str** | &gt;-Parcel Id is optional and required to be given in case of branded parcels which have brandedDimension and/or brandedWeight. If parcel has brandedDimension, in that case user need not to pass dimensionUnit and dimension details(length, width and height) in the parcel object. And if brandedWeight is also available for the parcel then in that case weightUnit and weight need not to be passed  in parcel object   | [optional] 
**service_id** | **str** | Service to be used for rating, it can be referred from response of &#x60;Get Services&#x60; API | 
**special_services** | [**List[SpecialService]**](SpecialService.md) | Special services to be used for rating, it can be referred from response of &#x60;Get Special Services&#x60; API | [optional] 
**to_address** | [**SingleRateToAddress**](SingleRateToAddress.md) |  | 

## Example

```python
from shipping.models.single_rate import SingleRate

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRate from a JSON string
single_rate_instance = SingleRate.from_json(json)
# print the JSON string representation of the object
print(SingleRate.to_json())

# convert the object into a dict
single_rate_dict = single_rate_instance.to_dict()
# create an instance of SingleRate from a dict
single_rate_from_dict = SingleRate.from_dict(single_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


