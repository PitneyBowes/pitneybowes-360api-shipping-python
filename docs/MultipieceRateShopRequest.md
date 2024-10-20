# MultipieceRateShopRequest

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**MultipieceRatesRequestFromAddress**](MultipieceRatesRequestFromAddress.md) |  | [optional] 
**multi_piece_parcels** | [**List[MultipieceRateShopRequestMultiPieceParcelsInner]**](MultipieceRateShopRequestMultiPieceParcelsInner.md) | description | [optional] 
**carrier_accounts** | **List[str]** | description | [optional] 
**to_address** | [**MultipieceRatesRequestToAddress**](MultipieceRatesRequestToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_rate_shop_request import MultipieceRateShopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRateShopRequest from a JSON string
multipiece_rate_shop_request_instance = MultipieceRateShopRequest.from_json(json)
# print the JSON string representation of the object
print(MultipieceRateShopRequest.to_json())

# convert the object into a dict
multipiece_rate_shop_request_dict = multipiece_rate_shop_request_instance.to_dict()
# create an instance of MultipieceRateShopRequest from a dict
multipiece_rate_shop_request_from_dict = MultipieceRateShopRequest.from_dict(multipiece_rate_shop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


