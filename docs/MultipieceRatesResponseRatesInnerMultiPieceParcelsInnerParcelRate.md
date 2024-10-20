# MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | description | [optional] 
**delivery_commitment** | [**RateShopResponseRatesInnerDeliveryCommitment**](RateShopResponseRatesInnerDeliveryCommitment.md) |  | [optional] 
**surcharges** | [**List[MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRateSurchargesInner]**](MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRateSurchargesInner.md) | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate import MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate from a JSON string
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_instance = MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate.to_json())

# convert the object into a dict
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_dict = multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_instance.to_dict()
# create an instance of MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate from a dict
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_from_dict = MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate.from_dict(multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


