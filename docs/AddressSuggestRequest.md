# AddressSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressSuggestRequestAddress**](AddressSuggestRequestAddress.md) |  | 

## Example

```python
from shipping.models.address_suggest_request import AddressSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestRequest from a JSON string
address_suggest_request_instance = AddressSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(AddressSuggestRequest.to_json())

# convert the object into a dict
address_suggest_request_dict = address_suggest_request_instance.to_dict()
# create an instance of AddressSuggestRequest from a dict
address_suggest_request_from_dict = AddressSuggestRequest.from_dict(address_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


