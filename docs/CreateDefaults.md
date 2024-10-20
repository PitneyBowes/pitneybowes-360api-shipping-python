# CreateDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Default, e.g., FedEx-SAKS. | [optional] 
**default_id** | **str** | A unique identifier to be assigned to the Default.  | [optional] 
**sending_options** | [**SendingOptions**](SendingOptions.md) |  | [optional] 

## Example

```python
from shipping.models.create_defaults import CreateDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefaults from a JSON string
create_defaults_instance = CreateDefaults.from_json(json)
# print the JSON string representation of the object
print(CreateDefaults.to_json())

# convert the object into a dict
create_defaults_dict = create_defaults_instance.to_dict()
# create an instance of CreateDefaults from a dict
create_defaults_from_dict = CreateDefaults.from_dict(create_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


