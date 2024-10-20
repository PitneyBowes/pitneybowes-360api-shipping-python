# MultipieceDomesticShipmentRequestMultiPieceParcelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | **str** | Description | [optional] 
**parcel** | [**MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel**](MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel.md) |  | [optional] 

## Example

```python
from shipping.models.multipiece_domestic_shipment_request_multi_piece_parcels_inner import MultipieceDomesticShipmentRequestMultiPieceParcelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentRequestMultiPieceParcelsInner from a JSON string
multipiece_domestic_shipment_request_multi_piece_parcels_inner_instance = MultipieceDomesticShipmentRequestMultiPieceParcelsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentRequestMultiPieceParcelsInner.to_json())

# convert the object into a dict
multipiece_domestic_shipment_request_multi_piece_parcels_inner_dict = multipiece_domestic_shipment_request_multi_piece_parcels_inner_instance.to_dict()
# create an instance of MultipieceDomesticShipmentRequestMultiPieceParcelsInner from a dict
multipiece_domestic_shipment_request_multi_piece_parcels_inner_from_dict = MultipieceDomesticShipmentRequestMultiPieceParcelsInner.from_dict(multipiece_domestic_shipment_request_multi_piece_parcels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


