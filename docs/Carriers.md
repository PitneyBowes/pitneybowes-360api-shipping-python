# Carriers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carriers** | [**List[CarriersCarriersInner]**](CarriersCarriersInner.md) |  | [optional] 

## Example

```python
from shipping.models.carriers import Carriers

# TODO update the JSON string below
json = "{}"
# create an instance of Carriers from a JSON string
carriers_instance = Carriers.from_json(json)
# print the JSON string representation of the object
print(Carriers.to_json())

# convert the object into a dict
carriers_dict = carriers_instance.to_dict()
# create an instance of Carriers from a dict
carriers_from_dict = Carriers.from_dict(carriers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


