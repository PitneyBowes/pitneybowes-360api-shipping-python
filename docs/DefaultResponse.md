# DefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the created Default. For example: Domestic. | [optional] 
**default_id** | **str** | Unique identifier assigned to the Default while its creation using CreateDefaults API. | [optional] 
**created_date** | **str** | The timestamp when the Default is created. | [optional] 
**updated_date** | **str** | The timestamp when the Default is updated. | [optional] 
**sending_options** | [**SendingOptionsResponse**](SendingOptionsResponse.md) |  | [optional] 

## Example

```python
from shipping.models.default_response import DefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultResponse from a JSON string
default_response_instance = DefaultResponse.from_json(json)
# print the JSON string representation of the object
print(DefaultResponse.to_json())

# convert the object into a dict
default_response_dict = default_response_instance.to_dict()
# create an instance of DefaultResponse from a dict
default_response_from_dict = DefaultResponse.from_dict(default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


