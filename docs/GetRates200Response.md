# GetRates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**RateShopResponseFromAddress**](RateShopResponseFromAddress.md) |  | [optional] 
**parcel** | [**RateShopResponseParcel**](RateShopResponseParcel.md) |  | [optional] 
**rates** | [**List[RateShopResponseRatesInner]**](RateShopResponseRatesInner.md) | It displays all available rates for each services | [optional] 
**to_address** | [**RateShopResponseToAddress**](RateShopResponseToAddress.md) |  | [optional] 
**is_hazmat** | **bool** | isHazmat if set to true,only services which support Hazardous material shipment would be visible in the response | [optional] 
**errors** | [**List[RateShopResponseErrorsInner]**](RateShopResponseErrorsInner.md) | It display any error while getting rates | [optional] 

## Example

```python
from shipping.models.get_rates200_response import GetRates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRates200Response from a JSON string
get_rates200_response_instance = GetRates200Response.from_json(json)
# print the JSON string representation of the object
print(GetRates200Response.to_json())

# convert the object into a dict
get_rates200_response_dict = get_rates200_response_instance.to_dict()
# create an instance of GetRates200Response from a dict
get_rates200_response_from_dict = GetRates200Response.from_dict(get_rates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


