# MultipieceDomesticShipmentRequest


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
**multi_piece_parcels** | [**List[MultipieceDomesticShipmentRequestMultiPieceParcelsInner]**](MultipieceDomesticShipmentRequestMultiPieceParcelsInner.md) | description | [optional] 
**to_address** | [**MultipieceDomesticShipmentRequestToAddress**](MultipieceDomesticShipmentRequestToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_domestic_shipment_request import MultipieceDomesticShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentRequest from a JSON string
multipiece_domestic_shipment_request_instance = MultipieceDomesticShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentRequest.to_json())

# convert the object into a dict
multipiece_domestic_shipment_request_dict = multipiece_domestic_shipment_request_instance.to_dict()
# create an instance of MultipieceDomesticShipmentRequest from a dict
multipiece_domestic_shipment_request_from_dict = MultipieceDomesticShipmentRequest.from_dict(multipiece_domestic_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


