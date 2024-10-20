# MultipieceRatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**MultipieceRatesRequestFromAddress**](MultipieceRatesRequestFromAddress.md) |  | [optional] 
**multi_piece_parcels** | [**List[MultipieceRatesRequestMultiPieceParcelsInner]**](MultipieceRatesRequestMultiPieceParcelsInner.md) | description | [optional] 
**carrier_accounts** | **List[str]** | description | [optional] 
**to_address** | [**MultipieceRatesRequestToAddress**](MultipieceRatesRequestToAddress.md) |  | [optional] 
**service_id** | **str** | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_request import MultipieceRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesRequest from a JSON string
multipiece_rates_request_instance = MultipieceRatesRequest.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesRequest.to_json())

# convert the object into a dict
multipiece_rates_request_dict = multipiece_rates_request_instance.to_dict()
# create an instance of MultipieceRatesRequest from a dict
multipiece_rates_request_from_dict = MultipieceRatesRequest.from_dict(multipiece_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


