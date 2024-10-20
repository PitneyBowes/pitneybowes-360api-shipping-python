# ShipmentInternationalCustoms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customs_items** | [**List[ShipmentInternationalCustomsCustomsItemsInner]**](ShipmentInternationalCustomsCustomsItemsInner.md) |  | [optional] 
**customs_info** | [**ShipmentInternationalCustomsCustomsInfo**](ShipmentInternationalCustomsCustomsInfo.md) |  | 

## Example

```python
from shipping.models.shipment_international_customs import ShipmentInternationalCustoms

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentInternationalCustoms from a JSON string
shipment_international_customs_instance = ShipmentInternationalCustoms.from_json(json)
# print the JSON string representation of the object
print(ShipmentInternationalCustoms.to_json())

# convert the object into a dict
shipment_international_customs_dict = shipment_international_customs_instance.to_dict()
# create an instance of ShipmentInternationalCustoms from a dict
shipment_international_customs_from_dict = ShipmentInternationalCustoms.from_dict(shipment_international_customs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


