# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any). | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** |  This indicates the city or town in the Address. | [optional] 
**company** | **str** |  This indicates the name of the company. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the country. | 
**email** | **str** | The email address of the Recipient or Department where the delivery address is pointed to. | [optional] 
**name** | **str** | The first and last name of the Recipient or Department. | [optional] 
**phone** | **str** | &gt;-The phone number. Enter the digits with or without spaces or hyphens. When used for Pickups, the maximum is 10 digits. | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the Address. | 
**residential** | **bool** | &gt;-Indicates whether this is a residential address. Pitney Bowes recommends including this parameter to improve address verification. | [optional] 
**state_province** | **str** | &gt;-The state or province. For a US or Canadian address, use the 2-letter state or province code. | 
**status** | **str** | &gt;- This field applies to the Validate Address and Suggest Addresses APIs. The field indicates whether the submitted address is valid and whether the API made changes to the address. Possible values are: &#x60;VALIDATED_CHANGED&#x60;: The address is valid, but the API made changes to improve the address. For example, if an address has a valid street number and street name (e.g. “100 Elm”) but is missing the street suffix (e.g. “St”), the API would add the suffix. &#x60;VALIDATED_AND_NOT_CHANGED&#x60;: The address is valid. The API made no changes. | [optional] 
**tax_id** | **str** | &gt;-Tax identification number (TIN) or Employer Identification number (EIN) or GST or VAT number or RFC or EORI. | [optional] 
**tax_id_type** | **str** | &gt;-Tax identification Type, valid values are EIN or GST or VAT or RFC or EORI. | [optional] 

## Example

```python
from shipping.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


