# ShipmentInternationalMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from shipping.models.shipment_international_metadata_inner import ShipmentInternationalMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentInternationalMetadataInner from a JSON string
shipment_international_metadata_inner_instance = ShipmentInternationalMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentInternationalMetadataInner.to_json())

# convert the object into a dict
shipment_international_metadata_inner_dict = shipment_international_metadata_inner_instance.to_dict()
# create an instance of ShipmentInternationalMetadataInner from a dict
shipment_international_metadata_inner_from_dict = ShipmentInternationalMetadataInner.from_dict(shipment_international_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


