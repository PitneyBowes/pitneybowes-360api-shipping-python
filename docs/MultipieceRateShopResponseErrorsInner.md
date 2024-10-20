# MultipieceRateShopResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | This is the error code, which varies as per the case. It reflects or alerts user in case if there is any error while performing RateShop.  | [optional] 
**message** | **str** | This is the error message reflects to user, in case if the user miss or enters incorrect information while performing RateShop. | [optional] 

## Example

```python
from shipping.models.multipiece_rate_shop_response_errors_inner import MultipieceRateShopResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceRateShopResponseErrorsInner from a JSON string
multipiece_rate_shop_response_errors_inner_instance = MultipieceRateShopResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(MultipieceRateShopResponseErrorsInner.to_json())

# convert the object into a dict
multipiece_rate_shop_response_errors_inner_dict = multipiece_rate_shop_response_errors_inner_instance.to_dict()
# create an instance of MultipieceRateShopResponseErrorsInner from a dict
multipiece_rate_shop_response_errors_inner_from_dict = MultipieceRateShopResponseErrorsInner.from_dict(multipiece_rate_shop_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


