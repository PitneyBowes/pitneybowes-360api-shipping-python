# MultipieceRateShopResponse

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**MultipieceRatesRequestFromAddress**](MultipieceRatesRequestFromAddress.md) |  | [optional] 
**to_address** | [**MultipieceRatesRequestToAddress**](MultipieceRatesRequestToAddress.md) |  | [optional] 
**service_id** | **str** | description | [optional] 
**rates** | [**List[MultipieceRateShopResponseRatesInner]**](MultipieceRateShopResponseRatesInner.md) | description | [optional] 
**errors** | [**List[MultipieceRateShopResponseErrorsInner]**](MultipieceRateShopResponseErrorsInner.md) | It display any error while getting rates | [optional] 

## Example

```python
from shipping.models.multipiece_rate_shop_response import MultipieceRateShopResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRateShopResponse from a JSON string
multipiece_rate_shop_response_instance = MultipieceRateShopResponse.from_json(json)
# print the JSON string representation of the object
print(MultipieceRateShopResponse.to_json())

# convert the object into a dict
multipiece_rate_shop_response_dict = multipiece_rate_shop_response_instance.to_dict()
# create an instance of MultipieceRateShopResponse from a dict
multipiece_rate_shop_response_from_dict = MultipieceRateShopResponse.from_dict(multipiece_rate_shop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


