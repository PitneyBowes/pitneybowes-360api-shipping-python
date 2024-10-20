# MultipieceRatesRequestMultiPieceParcelsInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | description | [optional] 
**parcel_id** | **str** | description | [optional] 
**parcel** | [**MultipieceRatesRequestMultiPieceParcelsInnerParcel**](MultipieceRatesRequestMultiPieceParcelsInnerParcel.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_rates_request_multi_piece_parcels_inner import MultipieceRatesRequestMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesRequestMultiPieceParcelsInner from a JSON string
multipiece_rates_request_multi_piece_parcels_inner_instance = MultipieceRatesRequestMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesRequestMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_rates_request_multi_piece_parcels_inner_dict = multipiece_rates_request_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceRatesRequestMultiPieceParcelsInner from a dict
multipiece_rates_request_multi_piece_parcels_inner_from_dict = MultipieceRatesRequestMultiPieceParcelsInner.from_dict(multipiece_rates_request_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


