# MultipieceDomesticShipmentResponseMultiPieceRatesInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_carrier_charge** | **float** | description | [optional] 
**carrier** | **str** | description | [optional] 
**currency_code** | **str** | description | [optional] 
**rate_type_id** | **str** | description | [optional] 
**service_id** | **str** | description | [optional] 
**service_name** | **str** | description | [optional] 
**multi_piece_parcels** | [**List[MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner]**](MultipieceDomesticShipmentResponseMultiPieceRatesInnerMultiPieceParcelsInner.md) | description | [optional] 
**surcharges** | [**List[MultipieceDomesticShipmentResponseMultiPieceRatesInnerSurchargesInner]**](MultipieceDomesticShipmentResponseMultiPieceRatesInnerSurchargesInner.md) | description | [optional] 

## Example

```python
from shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner import MultipieceDomesticShipmentResponseMultiPieceRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentResponseMultiPieceRatesInner from a JSON string
multipiece_domestic_shipment_response_multi_piece_rates_inner_instance = MultipieceDomesticShipmentResponseMultiPieceRatesInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentResponseMultiPieceRatesInner.to_json())

# convert the object into a dict
multipiece_domestic_shipment_response_multi_piece_rates_inner_dict = multipiece_domestic_shipment_response_multi_piece_rates_inner_instance.to_dict()
# create an instance of MultipieceDomesticShipmentResponseMultiPieceRatesInner from a dict
multipiece_domestic_shipment_response_multi_piece_rates_inner_from_dict = MultipieceDomesticShipmentResponseMultiPieceRatesInner.from_dict(multipiece_domestic_shipment_response_multi_piece_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


