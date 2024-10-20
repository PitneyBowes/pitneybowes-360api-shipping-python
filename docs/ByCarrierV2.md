# ByCarrierV2

The shipment is grouped by Carrier and their Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | This is a unique identifier associated with the specific sub-carrier account, which must be valid.&lt;br /&gt; This is used in the shipment creation (if this value is defined, Carrier properties will be skipped). | 
**carrier** | **str** | A unique identifier associated with the specific carrier, i.e. CarrierID, which must be valid. | 
**service** | **str** | Indicates a unique identifier associated with the carrier specific service, which is ServiceID, which must be valid. | 

## Example

```python
from shipping.models.by_carrier_v2 import ByCarrierV2

# TODO update the JSON string below
json = "{}"
# create an instance of ByCarrierV2 from a JSON string
by_carrier_v2_instance = ByCarrierV2.from_json(json)
# print the JSON string representation of the object
print(ByCarrierV2.to_json())

# convert the object into a dict
by_carrier_v2_dict = by_carrier_v2_instance.to_dict()
# create an instance of ByCarrierV2 from a dict
by_carrier_v2_from_dict = ByCarrierV2.from_dict(by_carrier_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


