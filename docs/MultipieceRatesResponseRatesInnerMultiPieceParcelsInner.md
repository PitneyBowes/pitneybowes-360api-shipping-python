# MultipieceRatesResponseRatesInnerMultiPieceParcelsInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | description | [optional] 
**parcel** | [**MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcel**](MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcel.md) |  | [optional] 
**parcel_rate** | [**MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate**](MultipieceRatesResponseRatesInnerMultiPieceParcelsInnerParcelRate.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner import MultipieceRatesResponseRatesInnerMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesResponseRatesInnerMultiPieceParcelsInner from a JSON string
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_instance = MultipieceRatesResponseRatesInnerMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesResponseRatesInnerMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_dict = multipiece_rates_response_rates_inner_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceRatesResponseRatesInnerMultiPieceParcelsInner from a dict
multipiece_rates_response_rates_inner_multi_piece_parcels_inner_from_dict = MultipieceRatesResponseRatesInnerMultiPieceParcelsInner.from_dict(multipiece_rates_response_rates_inner_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


