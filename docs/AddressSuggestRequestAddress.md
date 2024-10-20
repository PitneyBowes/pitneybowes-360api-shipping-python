# AddressSuggestRequestAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any).  | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** | The name of the city or town to where the address belongs. | 
**country_code** | **str** | This indicates the two-character ISO code of the country from the ISO country list. | 
**name** | **str** | Name of the person to which this address points. | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | 

## Example

```python
from shipping.models.address_suggest_request_address import AddressSuggestRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestRequestAddress from a JSON string
address_suggest_request_address_instance = AddressSuggestRequestAddress.from_json(json)
# print the JSON string representation of the object
print(AddressSuggestRequestAddress.to_json())

# convert the object into a dict
address_suggest_request_address_dict = address_suggest_request_address_instance.to_dict()
# create an instance of AddressSuggestRequestAddress from a dict
address_suggest_request_address_from_dict = AddressSuggestRequestAddress.from_dict(address_suggest_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


