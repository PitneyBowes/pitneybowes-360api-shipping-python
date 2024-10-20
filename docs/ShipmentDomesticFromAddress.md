# ShipmentDomesticFromAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential). | 
**address_line2** | **str** | The addressLine2 contains Street address or Landmark (if any). | [optional] 
**address_line3** | **str** | The addressLine3 contains P.O.Box (if any) near the address. | [optional] 
**city_town** | **str** | The name of the city or town to where the address belongs. | [optional] 
**country_code** | **str** | This indicates the two-character ISO code of the source country from the ISO country list. | 
**name** | **str** | Name of the sender to which this address points. | [optional] 
**company** | **str** | This indicates the name of the company, in case if the sender address is not residential. | [optional] 
**phone** | **str** | This is sender&#39;s phone number. Enter the digits with or without spaces or hyphens. The maximum characters for Phone number is 10 digits.  | [optional] 
**postal_code** | **str** | The postal code or ZIP code of the address. For US addresses, use either the 5-digit or 9-digit ZIP code in one of the following formats: &#39;12345&#39; or &#39;12345-6789&#39;. If you use a different format, such as 12345- or 123451234, will receive an error. | 
**state_province** | **str** | The State or Province of the address. For a US or Canadian address, it is the 2-letter state or province code.  | 
**induction_postal_code** | **str** | The postal code where the shipment is tendered to the carrier. If an induction postal code is specified in the \&quot;fromAddress\&quot;, it will be used for rate calculations and determining manifest eligibility instead of the standard postal code. If not specified, the postal code from the \&quot;fromAddress\&quot; will be used. | [optional] 

## Example

```python
from shipping.models.shipment_domestic_from_address import ShipmentDomesticFromAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDomesticFromAddress from a JSON string
shipment_domestic_from_address_instance = ShipmentDomesticFromAddress.from_json(json)
# print the JSON string representation of the object
print(ShipmentDomesticFromAddress.to_json())

# convert the object into a dict
shipment_domestic_from_address_dict = shipment_domestic_from_address_instance.to_dict()
# create an instance of ShipmentDomesticFromAddress from a dict
shipment_domestic_from_address_from_dict = ShipmentDomesticFromAddress.from_dict(shipment_domestic_from_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


