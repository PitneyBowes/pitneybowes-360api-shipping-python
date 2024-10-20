# MultipieceInternationalShipmentResponseCustoms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customs_items** | [**List[ShipmentInternationalCustomsCustomsItemsInner]**](ShipmentInternationalCustomsCustomsItemsInner.md) |  | 
**customs_info** | [**MultipieceInternationalShipmentResponseCustomsCustomsInfo**](MultipieceInternationalShipmentResponseCustomsCustomsInfo.md) |  | 

## Example

```python
from shipping.models.multipiece_international_shipment_response_customs import MultipieceInternationalShipmentResponseCustoms

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceInternationalShipmentResponseCustoms from a JSON string
multipiece_international_shipment_response_customs_instance = MultipieceInternationalShipmentResponseCustoms.from_json(json)
# print the JSON string representation of the object
print(MultipieceInternationalShipmentResponseCustoms.to_json())

# convert the object into a dict
multipiece_international_shipment_response_customs_dict = multipiece_international_shipment_response_customs_instance.to_dict()
# create an instance of MultipieceInternationalShipmentResponseCustoms from a dict
multipiece_international_shipment_response_customs_from_dict = MultipieceInternationalShipmentResponseCustoms.from_dict(multipiece_international_shipment_response_customs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


