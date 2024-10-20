# InternationalShipmentResponseCustoms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customs_info** | [**InternationalShipmentResponseCustomsCustomsInfo**](InternationalShipmentResponseCustomsCustomsInfo.md) |  | [optional] 
**customs_items** | [**List[InternationalShipmentResponseCustomsCustomsItemsInner]**](InternationalShipmentResponseCustomsCustomsItemsInner.md) |  | [optional] 

## Example

```python
from shipping.models.international_shipment_response_customs import InternationalShipmentResponseCustoms

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalShipmentResponseCustoms from a JSON string
international_shipment_response_customs_instance = InternationalShipmentResponseCustoms.from_json(json)
# print the JSON string representation of the object
print(InternationalShipmentResponseCustoms.to_json())

# convert the object into a dict
international_shipment_response_customs_dict = international_shipment_response_customs_instance.to_dict()
# create an instance of InternationalShipmentResponseCustoms from a dict
international_shipment_response_customs_from_dict = InternationalShipmentResponseCustoms.from_dict(international_shipment_response_customs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


