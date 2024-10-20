# SingleRateResponseFromAddress

Sender address details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | [optional] 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any). | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** | The name of the city or town to where the sender&#39;s address belongs. | [optional] 
**company** | **str** | This indicates the name of the company, in case if the sender address is not residential. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the source country from the ISO country list. | [optional] 
**name** | **str** | Name of the sender to which this address points. | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | [optional] 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | [optional] 

## Example

```python
from shipping.models.single_rate_response_from_address import SingleRateResponseFromAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRateResponseFromAddress from a JSON string
single_rate_response_from_address_instance = SingleRateResponseFromAddress.from_json(json)
# print the JSON string representation of the object
print(SingleRateResponseFromAddress.to_json())

# convert the object into a dict
single_rate_response_from_address_dict = single_rate_response_from_address_instance.to_dict()
# create an instance of SingleRateResponseFromAddress from a dict
single_rate_response_from_address_from_dict = SingleRateResponseFromAddress.from_dict(single_rate_response_from_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


