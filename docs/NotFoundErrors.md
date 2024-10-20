# NotFoundErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[NotFoundErrorsErrorsInner]**](NotFoundErrorsErrorsInner.md) |  | [optional] 

## Example

```python
from shipping.models.not_found_errors import NotFoundErrors

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundErrors from a JSON string
not_found_errors_instance = NotFoundErrors.from_json(json)
# print the JSON string representation of the object
print(NotFoundErrors.to_json())

# convert the object into a dict
not_found_errors_dict = not_found_errors_instance.to_dict()
# create an instance of NotFoundErrors from a dict
not_found_errors_from_dict = NotFoundErrors.from_dict(not_found_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


