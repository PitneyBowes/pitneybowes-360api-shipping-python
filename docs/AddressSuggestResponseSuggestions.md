# AddressSuggestResponseSuggestions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestion_type** | **str** | The part of the address that is changed in the accompanying suggestions. Possible values are: - street - streetPrimaryRange (e.g., street number, PO Box number) - secondaryRange (e.g., suite number, apartment number) - PO BoxPrimaryRange - ruralRouteUnitRange - highwayContractUnitRange - city - company - puertoricanUrbanization | [optional] 
**addresses** | [**List[AddressSuggestResponseSuggestionsAddressesInner]**](AddressSuggestResponseSuggestionsAddressesInner.md) |  | [optional] 

## Example

```python
from shipping.models.address_suggest_response_suggestions import AddressSuggestResponseSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestResponseSuggestions from a JSON string
address_suggest_response_suggestions_instance = AddressSuggestResponseSuggestions.from_json(json)
# print the JSON string representation of the object
print(AddressSuggestResponseSuggestions.to_json())

# convert the object into a dict
address_suggest_response_suggestions_dict = address_suggest_response_suggestions_instance.to_dict()
# create an instance of AddressSuggestResponseSuggestions from a dict
address_suggest_response_suggestions_from_dict = AddressSuggestResponseSuggestions.from_dict(address_suggest_response_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


