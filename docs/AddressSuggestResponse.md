# AddressSuggestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressSuggestResponseAddress**](AddressSuggestResponseAddress.md) |  | [optional] 
**suggestions** | [**AddressSuggestResponseSuggestions**](AddressSuggestResponseSuggestions.md) |  | [optional] 

## Example

```python
from shipping.models.address_suggest_response import AddressSuggestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestResponse from a JSON string
address_suggest_response_instance = AddressSuggestResponse.from_json(json)
# print the JSON string representation of the object
print(AddressSuggestResponse.to_json())

# convert the object into a dict
address_suggest_response_dict = address_suggest_response_instance.to_dict()
# create an instance of AddressSuggestResponse from a dict
address_suggest_response_from_dict = AddressSuggestResponse.from_dict(address_suggest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


