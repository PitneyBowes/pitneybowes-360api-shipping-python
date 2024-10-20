# CustomsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A detailed description of the commodity. | 
**h_s_tariff_code** | **str** | &gt;- The destination country&#39;s tariff-classification number for the commodity. Most countries use the six-digit Harmonized System (HS) as the basis for their tariff classifications and add additional digits for more detail. The maximum length is 14 characters.If you are issuing the HS Code API, you can use this field to help with the HS code prediction by entering the commodity&#39;s HS code from another country, such as from the origin country. Enter the country that the code comes from in the hSTariffCodeCountry field. | [optional] 
**quantity** | **int** | Enter the total number of items of this type of commodity. | 
**unit_price** | **float** | &gt;- The price of one item of this type of commodity. Currency should be declared under customsInfo. | 
**weight_unit** | **str** | The unit of measurement. This field is required by the unitWeight object. | 
**weight** | **float** | The weight of the item. | 

## Example

```python
from shipping.models.customs_item import CustomsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsItem from a JSON string
customs_item_instance = CustomsItem.from_json(json)
# print the JSON string representation of the object
print(CustomsItem.to_json())

# convert the object into a dict
customs_item_dict = customs_item_instance.to_dict()
# create an instance of CustomsItem from a dict
customs_item_from_dict = CustomsItem.from_dict(customs_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


