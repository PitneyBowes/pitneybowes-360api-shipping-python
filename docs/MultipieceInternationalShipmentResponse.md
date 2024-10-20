# MultipieceInternationalShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | description | [optional] 
**label_layout** | [**List[MultipieceDomesticShipmentResponseLabelLayoutInner]**](MultipieceDomesticShipmentResponseLabelLayoutInner.md) | description | [optional] 
**from_address** | [**MultipieceDomesticShipmentRequestFromAddress**](MultipieceDomesticShipmentRequestFromAddress.md) |  | [optional] 
**multi_piece_rates** | [**List[MultipieceDomesticShipmentResponseMultiPieceRatesInner]**](MultipieceDomesticShipmentResponseMultiPieceRatesInner.md) | description | [optional] 
**parcel_tracking_number** | **str** | description | [optional] 
**shipment_id** | **str** | description | [optional] 
**shipment_options** | [**MultipieceDomesticShipmentRequestShipmentOptions**](MultipieceDomesticShipmentRequestShipmentOptions.md) |  | [optional] 
**to_address** | [**MultipieceDomesticShipmentRequestToAddress**](MultipieceDomesticShipmentRequestToAddress.md) |  | [optional] 
**customs** | [**MultipieceInternationalShipmentResponseCustoms**](MultipieceInternationalShipmentResponseCustoms.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_international_shipment_response import MultipieceInternationalShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceInternationalShipmentResponse from a JSON string
multipiece_international_shipment_response_instance = MultipieceInternationalShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(MultipieceInternationalShipmentResponse.to_json())

# convert the object into a dict
multipiece_international_shipment_response_dict = multipiece_international_shipment_response_instance.to_dict()
# create an instance of MultipieceInternationalShipmentResponse from a dict
multipiece_international_shipment_response_from_dict = MultipieceInternationalShipmentResponse.from_dict(multipiece_international_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


