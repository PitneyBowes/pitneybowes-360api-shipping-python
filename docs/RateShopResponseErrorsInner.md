# RateShopResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | This is the error code, which varies as per the case. It reflects or alerts user in case if there is any error while performing RateShop.  | [optional] 
**message** | **str** | This is the error message reflects to user, in case if the user miss or enters incorrect information while performing RateShop. | [optional] 

## Example

```python
from shipping.models.rate_shop_response_errors_inner import RateShopResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RateShopResponseErrorsInner from a JSON string
rate_shop_response_errors_inner_instance = RateShopResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(RateShopResponseErrorsInner.to_json())

# convert the object into a dict
rate_shop_response_errors_inner_dict = rate_shop_response_errors_inner_instance.to_dict()
# create an instance of RateShopResponseErrorsInner from a dict
rate_shop_response_errors_inner_from_dict = RateShopResponseErrorsInner.from_dict(rate_shop_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


