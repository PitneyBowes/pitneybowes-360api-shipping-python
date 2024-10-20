# CreateDefaultsResponse

This is the response for created Default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier used in Database for Default, for mapping purpose. | [optional] 
**default_id** | **str** | Assigned unique identifier for the created Default. | [optional] 

## Example

```python
from shipping.models.create_defaults_response import CreateDefaultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefaultsResponse from a JSON string
create_defaults_response_instance = CreateDefaultsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDefaultsResponse.to_json())

# convert the object into a dict
create_defaults_response_dict = create_defaults_response_instance.to_dict()
# create an instance of CreateDefaultsResponse from a dict
create_defaults_response_from_dict = CreateDefaultsResponse.from_dict(create_defaults_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


