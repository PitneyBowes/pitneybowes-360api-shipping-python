# AddressValidateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | [optional] 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any). | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** | The name of the city or town to where the address belongs. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the country from the ISO country list. | [optional] 
**name** | **str** | Name of the person to which this address points. | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | [optional] 
**residential** | **bool** | The specified adress can be Residential or Official. In case if the adress is Residential, the boolean value will be &#39;true&#39;, else it will take &#39;false&#39;. | [optional] 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | [optional] 
**status** | **str** | &gt;- This field applies to the Validate Address and Suggest Addresses APIs. The field indicates whether the submitted address is valid and whether the API made changes to the address. Possible values are: &lt;br&gt;-&#x60;VALIDATED_CHANGED&#x60;: The address is valid, but the API made changes to improve the address. For example, if an address has a valid street number and street name (e.g. “100 Elm”) but is missing the street suffix (e.g. “St”), the API would add the suffix. &lt;br&gt;-&#x60;VALIDATED_AND_NOT_CHANGED&#x60;: The address is valid. The API made no changes. | [optional] 

## Example

```python
from shipping.models.address_validate_response import AddressValidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressValidateResponse from a JSON string
address_validate_response_instance = AddressValidateResponse.from_json(json)
# print the JSON string representation of the object
print(AddressValidateResponse.to_json())

# convert the object into a dict
address_validate_response_dict = address_validate_response_instance.to_dict()
# create an instance of AddressValidateResponse from a dict
address_validate_response_from_dict = AddressValidateResponse.from_dict(address_validate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


