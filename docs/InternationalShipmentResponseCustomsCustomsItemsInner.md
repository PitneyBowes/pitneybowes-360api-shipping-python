# InternationalShipmentResponseCustomsCustomsItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A detailed description of the commodity, up to 255 characters. The description will appear on the customs form. If the shipment has multiple types of items, create a separate customsItems object for each. Each description will appear on the form. | [optional] 
**h_s_tariff_code** | **str** | The destination country’s tariff-classification number (HS code) for the commodity. Most countries use the six-digit Harmonized System (HS) as the basis for their tariff classifications and then add digits for more detail. The maximum length for an HS code is 14 characters. The HS code will appear on the customs form. If the shipment has multiple types of items, create a separate customsItems object for each. | [optional] 
**origin_country_code** | **str** | The two-character ISO country code of the shipment’s origin country. Use ISO 3166-1 alpha-2 standard values. | [optional] 
**quantity** | **float** | Enter the total number of items of this type of commodity. | [optional] 
**unit_price** | **float** | The price of one item of this type of commodity. | [optional] 
**weight_unit** | **str** | WeightUnit is a standard for measuring the physical quantities of specified weight. &lt;br&gt; The valid values are:  &lt;br&gt;- OZ: Ounces &lt;br&gt;- GM: Grams &lt;br&gt;- LB: Pounds &lt;br&gt;- KG: Kilograms For USPS shipments, set this to OZ. | [optional] 
**weight** | **float** | Weight is the measure of how heavy an object is. | [optional] 

## Example

```python
from shipping.models.international_shipment_response_customs_customs_items_inner import InternationalShipmentResponseCustomsCustomsItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalShipmentResponseCustomsCustomsItemsInner from a JSON string
international_shipment_response_customs_customs_items_inner_instance = InternationalShipmentResponseCustomsCustomsItemsInner.from_json(json)
# print the JSON string representation of the object
print(InternationalShipmentResponseCustomsCustomsItemsInner.to_json())

# convert the object into a dict
international_shipment_response_customs_customs_items_inner_dict = international_shipment_response_customs_customs_items_inner_instance.to_dict()
# create an instance of InternationalShipmentResponseCustomsCustomsItemsInner from a dict
international_shipment_response_customs_customs_items_inner_from_dict = InternationalShipmentResponseCustomsCustomsItemsInner.from_dict(international_shipment_response_customs_customs_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


