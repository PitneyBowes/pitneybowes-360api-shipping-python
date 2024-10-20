# GetDefaultsById


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the created Default. For example: Domestic. | [optional] 
**default_id** | **str** | Unique identifier assigned to the Default while its creation using CreateDefaults API. | [optional] 
**created_date** | **datetime** | The timestamp when the Default is created. | [optional] 
**updated_date** | **datetime** | The timestamp when the Default is updated. | [optional] 
**sending_options** | [**SendingOptions**](SendingOptions.md) |  | [optional] 

## Example

```python
from shipping.models.get_defaults_by_id import GetDefaultsById

# TODO update the JSON string below
json = "{}"
# create an instance of GetDefaultsById from a JSON string
get_defaults_by_id_instance = GetDefaultsById.from_json(json)
# print the JSON string representation of the object
print(GetDefaultsById.to_json())

# convert the object into a dict
get_defaults_by_id_dict = get_defaults_by_id_instance.to_dict()
# create an instance of GetDefaultsById from a dict
get_defaults_by_id_from_dict = GetDefaultsById.from_dict(get_defaults_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


