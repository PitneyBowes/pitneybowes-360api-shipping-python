# MultipieceInternationalShipmentRequestMultiPieceParcelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | Description | [optional] 
**parcel_id** | **str** | Description | [optional] 
**parcel** | [**MultipieceInternationalShipmentRequestMultiPieceParcelsInnerParcel**](MultipieceInternationalShipmentRequestMultiPieceParcelsInnerParcel.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_international_shipment_request_multi_piece_parcels_inner import MultipieceInternationalShipmentRequestMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceInternationalShipmentRequestMultiPieceParcelsInner from a JSON string
multipiece_international_shipment_request_multi_piece_parcels_inner_instance = MultipieceInternationalShipmentRequestMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceInternationalShipmentRequestMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_international_shipment_request_multi_piece_parcels_inner_dict = multipiece_international_shipment_request_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceInternationalShipmentRequestMultiPieceParcelsInner from a dict
multipiece_international_shipment_request_multi_piece_parcels_inner_from_dict = MultipieceInternationalShipmentRequestMultiPieceParcelsInner.from_dict(multipiece_international_shipment_request_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


