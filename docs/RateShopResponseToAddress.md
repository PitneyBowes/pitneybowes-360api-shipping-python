# RateShopResponseToAddress

Recipient address details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | [optional] 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any). | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** | The name of the city or town to where the address belongs. | [optional] 
**company** | **str** | This indicates the name of the company, in case if the Recipient address is not residential. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the destination country from the ISO country list. | [optional] 
**email** | **str** | The email address of the recipient. It can be person&#39;s email address or company email address (for non-residential). | [optional] 
**name** | **str** | Name of the recipient to which this address points. | [optional] 
**phone** | **str** | This is recipient&#39;s phone number. Enter the digits with or without spaces or hyphens. The maximum characters for Phone number is 10 digits.  | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | [optional] 
**residential** | **bool** | The specified adress can be Residential or Official. In case if the adress is Residential, the boolean value will be &#39;true&#39;, else it will take &#39;false&#39;. | [optional] 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | [optional] 

## Example

```python
from shipping.models.rate_shop_response_to_address import RateShopResponseToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RateShopResponseToAddress from a JSON string
rate_shop_response_to_address_instance = RateShopResponseToAddress.from_json(json)
# print the JSON string representation of the object
print(RateShopResponseToAddress.to_json())

# convert the object into a dict
rate_shop_response_to_address_dict = rate_shop_response_to_address_instance.to_dict()
# create an instance of RateShopResponseToAddress from a dict
rate_shop_response_to_address_from_dict = RateShopResponseToAddress.from_dict(rate_shop_response_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


