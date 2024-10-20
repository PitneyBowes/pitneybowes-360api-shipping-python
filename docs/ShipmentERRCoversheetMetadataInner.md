# ShipmentERRCoversheetMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key of metadata is CostAccount. User needs to enter the name of the CostAccount, e.g. PBNOIDA-COSTACC. | [optional] 
**value** | **str** | User needs to enter the Cost Account Code, CostAccount-00PBNOD. | [optional] 

## Example

```python
from shipping.models.shipment_err_coversheet_metadata_inner import ShipmentERRCoversheetMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentERRCoversheetMetadataInner from a JSON string
shipment_err_coversheet_metadata_inner_instance = ShipmentERRCoversheetMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentERRCoversheetMetadataInner.to_json())

# convert the object into a dict
shipment_err_coversheet_metadata_inner_dict = shipment_err_coversheet_metadata_inner_instance.to_dict()
# create an instance of ShipmentERRCoversheetMetadataInner from a dict
shipment_err_coversheet_metadata_inner_from_dict = ShipmentERRCoversheetMetadataInner.from_dict(shipment_err_coversheet_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


