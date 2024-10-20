# MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel

Description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | Description | [optional] 
**weight_unit** | **str** | Description | [optional] 
**width** | **float** | Description | [optional] 
**length** | **float** | Description | [optional] 
**height** | **float** | Description | [optional] 
**dim_unit** | **str** | Description | [optional] 

## Example

```python
from shipping.models.multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel import MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel from a JSON string
multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel_instance = MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel.from_json(json)
# print the JSON string representation of the object
print(MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel.to_json())

# convert the object into a dict
multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel_dict = multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel_instance.to_dict()
# create an instance of MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel from a dict
multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel_from_dict = MultipieceDomesticShipmentRequestMultiPieceParcelsInnerParcel.from_dict(multipiece_domestic_shipment_request_multi_piece_parcels_inner_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


