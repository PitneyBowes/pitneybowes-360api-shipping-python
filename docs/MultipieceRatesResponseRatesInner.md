# MultipieceRatesResponseRatesInner

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_carrier_charge** | **float** | description | [optional] 
**carrier** | **str** | description | [optional] 
**currency_code** | **str** | description | [optional] 
**rate_type_id** | **str** | description | [optional] 
**service_id** | **str** | description | [optional] 
**multi_piece_parcels** | [**List[MultipieceRatesResponseRatesInnerMultiPieceParcelsInner]**](MultipieceRatesResponseRatesInnerMultiPieceParcelsInner.md) | description | [optional] 
**surcharges** | [**List[MultipieceRatesResponseRatesInnerSurchargesInner]**](MultipieceRatesResponseRatesInnerSurchargesInner.md) | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_response_rates_inner import MultipieceRatesResponseRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesResponseRatesInner from a JSON string
multipiece_rates_response_rates_inner_instance = MultipieceRatesResponseRatesInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesResponseRatesInner.to_json())

# convert the object into a dict
multipiece_rates_response_rates_inner_dict = multipiece_rates_response_rates_inner_instance.to_dict()
# create an instance of MultipieceRatesResponseRatesInner from a dict
multipiece_rates_response_rates_inner_from_dict = MultipieceRatesResponseRatesInner.from_dict(multipiece_rates_response_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


