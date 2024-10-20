# CarriersCarriersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_id** | **str** | A unique identifier associated with the specific carrier. | [optional] 
**name** | **str** | This is the name of the Carrier, a shipping service which is used to carry shipment (e.g., parcels/packages/envelopes) from one place to other. | [optional] 
**origin_country** | **str** | This indicates the two-character ISO code of the source country from the ISO country list. | [optional] 
**properties** | [**CarriersCarriersInnerProperties**](CarriersCarriersInnerProperties.md) |  | [optional] 

## Example

```python
from shipping.models.carriers_carriers_inner import CarriersCarriersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersCarriersInner from a JSON string
carriers_carriers_inner_instance = CarriersCarriersInner.from_json(json)
# print the JSON string representation of the object
print(CarriersCarriersInner.to_json())

# convert the object into a dict
carriers_carriers_inner_dict = carriers_carriers_inner_instance.to_dict()
# create an instance of CarriersCarriersInner from a dict
carriers_carriers_inner_from_dict = CarriersCarriersInner.from_dict(carriers_carriers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


