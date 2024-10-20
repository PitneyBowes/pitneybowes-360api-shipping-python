# ShipmentReprintV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | The shipmentId is a unique identifier for an individual Shipment. | 
**printer_alias_name** | **str** | Refers to a printer connected (directly or via network) to a computer. &#x60;Max length &#x3D; 60&#x60; | [optional] 
**references** | [**ShipmentReprintV2References**](ShipmentReprintV2References.md) |  | [optional] 

## Example

```python
from shipping.models.shipment_reprint_v2 import ShipmentReprintV2

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentReprintV2 from a JSON string
shipment_reprint_v2_instance = ShipmentReprintV2.from_json(json)
# print the JSON string representation of the object
print(ShipmentReprintV2.to_json())

# convert the object into a dict
shipment_reprint_v2_dict = shipment_reprint_v2_instance.to_dict()
# create an instance of ShipmentReprintV2 from a dict
shipment_reprint_v2_from_dict = ShipmentReprintV2.from_dict(shipment_reprint_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


