# MultipieceRateShopRequestMultiPieceParcelsInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | description | [optional] 
**parcel** | [**MultipieceRateShopRequestMultiPieceParcelsInnerParcel**](MultipieceRateShopRequestMultiPieceParcelsInnerParcel.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_rate_shop_request_multi_piece_parcels_inner import MultipieceRateShopRequestMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRateShopRequestMultiPieceParcelsInner from a JSON string
multipiece_rate_shop_request_multi_piece_parcels_inner_instance = MultipieceRateShopRequestMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRateShopRequestMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_rate_shop_request_multi_piece_parcels_inner_dict = multipiece_rate_shop_request_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceRateShopRequestMultiPieceParcelsInner from a dict
multipiece_rate_shop_request_multi_piece_parcels_inner_from_dict = MultipieceRateShopRequestMultiPieceParcelsInner.from_dict(multipiece_rate_shop_request_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


