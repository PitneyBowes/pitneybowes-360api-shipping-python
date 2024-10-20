# ReturnLabelResponseToAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | 
**email** | **str** | Email id | [optional] 
**city_town** | **str** | The name of the city or town to where the address belongs. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the destination country from the ISO country list. | [optional] 
**name** | **str** | Name of the recipient to which this address points. | [optional] 
**phone** | **str** | This is recipient&#39;s phone number. Enter the digits with or without spaces or hyphens. The maximum characters for Phone number is 10 digits.  | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | [optional] 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | [optional] 

## Example

```python
from shipping.models.return_label_response_to_address import ReturnLabelResponseToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelResponseToAddress from a JSON string
return_label_response_to_address_instance = ReturnLabelResponseToAddress.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelResponseToAddress.to_json())

# convert the object into a dict
return_label_response_to_address_dict = return_label_response_to_address_instance.to_dict()
# create an instance of ReturnLabelResponseToAddress from a dict
return_label_response_to_address_from_dict = ReturnLabelResponseToAddress.from_dict(return_label_response_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


