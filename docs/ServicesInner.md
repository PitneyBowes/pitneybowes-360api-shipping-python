# ServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branded_name** | **str** | The branded name of service. | [optional] 
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 

## Example

```python
from shipping.models.services_inner import ServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesInner from a JSON string
services_inner_instance = ServicesInner.from_json(json)
# print the JSON string representation of the object
print(ServicesInner.to_json())

# convert the object into a dict
services_inner_dict = services_inner_instance.to_dict()
# create an instance of ServicesInner from a dict
services_inner_from_dict = ServicesInner.from_dict(services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


