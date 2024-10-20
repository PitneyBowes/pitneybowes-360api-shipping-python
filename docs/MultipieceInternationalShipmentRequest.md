# MultipieceInternationalShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | description | [optional] 
**type** | **str** | description | [optional] 
**from_address** | [**MultipieceDomesticShipmentRequestFromAddress**](MultipieceDomesticShipmentRequestFromAddress.md) |  | [optional] 
**carrier_account_id** | **str** | description | [optional] 
**service_id** | **str** | description | [optional] 
**shipment_options** | [**MultipieceDomesticShipmentRequestShipmentOptions**](MultipieceDomesticShipmentRequestShipmentOptions.md) |  | [optional] 
**metadata** | [**List[MultipieceDomesticShipmentRequestMetadataInner]**](MultipieceDomesticShipmentRequestMetadataInner.md) | description | [optional] 
**multi_piece_parcels** | [**List[MultipieceInternationalShipmentRequestMultiPieceParcelsInner]**](MultipieceInternationalShipmentRequestMultiPieceParcelsInner.md) | description | [optional] 
**to_address** | [**MultipieceInternationalShipmentRequestToAddress**](MultipieceInternationalShipmentRequestToAddress.md) |  | [optional] 
**customs** | [**MultipieceInternationalShipmentRequestCustoms**](MultipieceInternationalShipmentRequestCustoms.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_international_shipment_request import MultipieceInternationalShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceInternationalShipmentRequest from a JSON string
multipiece_international_shipment_request_instance = MultipieceInternationalShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(MultipieceInternationalShipmentRequest.to_json())

# convert the object into a dict
multipiece_international_shipment_request_dict = multipiece_international_shipment_request_instance.to_dict()
# create an instance of MultipieceInternationalShipmentRequest from a dict
multipiece_international_shipment_request_from_dict = MultipieceInternationalShipmentRequest.from_dict(multipiece_international_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


