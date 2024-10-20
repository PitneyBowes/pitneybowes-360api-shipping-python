# ShipmentERRMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key of metadata is CostAccount. User needs to enter the name of the CostAccount, e.g. PBPUNE_COSTACC. | [optional] 
**value** | **str** | User needs to enter the CostAccount Code, e.g. CAC-00PBPUN. | [optional] 

## Example

```python
from shipping.models.shipment_err_metadata_inner import ShipmentERRMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentERRMetadataInner from a JSON string
shipment_err_metadata_inner_instance = ShipmentERRMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentERRMetadataInner.to_json())

# convert the object into a dict
shipment_err_metadata_inner_dict = shipment_err_metadata_inner_instance.to_dict()
# create an instance of ShipmentERRMetadataInner from a dict
shipment_err_metadata_inner_from_dict = ShipmentERRMetadataInner.from_dict(shipment_err_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


