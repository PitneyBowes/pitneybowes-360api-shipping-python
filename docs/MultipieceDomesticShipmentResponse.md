# MultipieceDomesticShipmentResponse


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

## Example

```python
from shipping.models.multipiece_domestic_shipment_response import MultipieceDomesticShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentResponse from a JSON string
multipiece_domestic_shipment_response_instance = MultipieceDomesticShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentResponse.to_json())

# convert the object into a dict
multipiece_domestic_shipment_response_dict = multipiece_domestic_shipment_response_instance.to_dict()
# create an instance of MultipieceDomesticShipmentResponse from a dict
multipiece_domestic_shipment_response_from_dict = MultipieceDomesticShipmentResponse.from_dict(multipiece_domestic_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


