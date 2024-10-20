# ShipmentMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is a key of metadata | [optional] 
**value** | **str** | This is a value of metadata | [optional] 

## Example

```python
from shipping.models.shipment_metadata_inner import ShipmentMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMetadataInner from a JSON string
shipment_metadata_inner_instance = ShipmentMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentMetadataInner.to_json())

# convert the object into a dict
shipment_metadata_inner_dict = shipment_metadata_inner_instance.to_dict()
# create an instance of ShipmentMetadataInner from a dict
shipment_metadata_inner_from_dict = ShipmentMetadataInner.from_dict(shipment_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


