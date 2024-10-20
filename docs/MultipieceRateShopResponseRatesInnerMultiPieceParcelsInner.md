# MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | description | [optional] 
**parcel** | [**MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcel**](MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcel.md) |  | [optional] 
**parcel_rate** | [**MultipieceRateShopResponseRatesInnerMultiPieceParcelsInnerParcelRate**](MultipieceRateShopResponseRatesInnerMultiPieceParcelsInnerParcelRate.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner import MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner from a JSON string
multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner_instance = MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner_dict = multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner from a dict
multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner_from_dict = MultipieceRateShopResponseRatesInnerMultiPieceParcelsInner.from_dict(multipiece_rate_shop_response_rates_inner_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


