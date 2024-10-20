# ShipmentDomesticMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | It is used to provide metadata name, possible values are &#x60;costAccountName&#x60;, For NORATE carrier- &#x60;customCharge&#x60; and &#x60;customTrackingNumber&#x60; can be used to provide custom rate and tracking number respectively. | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from shipping.models.shipment_domestic_metadata_inner import ShipmentDomesticMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticMetadataInner from a JSON string
shipment_domestic_metadata_inner_instance = ShipmentDomesticMetadataInner.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticMetadataInner.to_json())

# convert the object into a dict
shipment_domestic_metadata_inner_dict = shipment_domestic_metadata_inner_instance.to_dict()
# create an instance of ShipmentDomesticMetadataInner from a dict
shipment_domestic_metadata_inner_from_dict = ShipmentDomesticMetadataInner.from_dict(shipment_domestic_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


