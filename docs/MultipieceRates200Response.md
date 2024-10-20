# MultipieceRates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**MultipieceRatesRequestFromAddress**](MultipieceRatesRequestFromAddress.md) |  | [optional] 
**to_address** | [**MultipieceRatesRequestToAddress**](MultipieceRatesRequestToAddress.md) |  | [optional] 
**service_id** | **str** | description | [optional] 
**rates** | [**List[MultipieceRatesResponseRatesInner]**](MultipieceRatesResponseRatesInner.md) | description | [optional] 
**errors** | [**List[MultipieceRateShopResponseErrorsInner]**](MultipieceRateShopResponseErrorsInner.md) | It display any error while getting rates | [optional] 

## Example

```python
from shipping.models.multipiece_rates200_response import MultipieceRates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRates200Response from a JSON string
multipiece_rates200_response_instance = MultipieceRates200Response.from_json(json)
# print the JSON string representation of the object
print(MultipieceRates200Response.to_json())

# convert the object into a dict
multipiece_rates200_response_dict = multipiece_rates200_response_instance.to_dict()
# create an instance of MultipieceRates200Response from a dict
multipiece_rates200_response_from_dict = MultipieceRates200Response.from_dict(multipiece_rates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


