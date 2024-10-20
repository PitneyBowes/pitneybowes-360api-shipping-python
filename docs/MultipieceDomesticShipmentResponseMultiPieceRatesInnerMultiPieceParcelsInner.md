# MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | description | [optional] 
**parcel** | [**MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInnerParcel**](MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInnerParcel.md) |  | [optional] 
**parcel_rate** | [**MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInnerParcelRate**](MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInnerParcelRate.md) |  | [optional] 
**parcel_tracking_number** | **str** | description | [optional] 

## Example

```python
from shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner import MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner from a JSON string
multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_instance = MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_dict = multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner from a dict
multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_from_dict = MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner.from_dict(multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


