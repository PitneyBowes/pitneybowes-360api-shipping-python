# MultipieceRatesResponse

description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**MultipieceRatesRequestFromAddress**](MultipieceRatesRequestFromAddress.md) |  | [optional] 
**to_address** | [**MultipieceRatesRequestToAddress**](MultipieceRatesRequestToAddress.md) |  | [optional] 
**service_id** | **str** | description | [optional] 
**rates** | [**List[MultipieceRatesResponseRatesInner]**](MultipieceRatesResponseRatesInner.md) | description | [optional] 

## Example

```python
from shipping.models.multipiece_rates_response import MultipieceRatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRatesResponse from a JSON string
multipiece_rates_response_instance = MultipieceRatesResponse.from_json(json)
# print the JSON string representation of the object
print(MultipieceRatesResponse.to_json())

# convert the object into a dict
multipiece_rates_response_dict = multipiece_rates_response_instance.to_dict()
# create an instance of MultipieceRatesResponse from a dict
multipiece_rates_response_from_dict = MultipieceRatesResponse.from_dict(multipiece_rates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


