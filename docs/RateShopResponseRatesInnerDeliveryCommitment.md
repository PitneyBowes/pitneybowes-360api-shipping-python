# RateShopResponseRatesInnerDeliveryCommitment

It specifies the delivery commitment provided by carrier for this shipment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **str** | It specifies the additional details for the delivery commitment | [optional] 
**estimated_delivery_date_time** | **str** | It specifies estimated delivery date time | [optional] 
**guarantee** | **str** | It specifies if guarantee is provided. | [optional] 
**max_estimated_number_of_days** | **str** | It specifies the maximum estimated number of days | [optional] 
**min_estimated_number_of_days** | **str** | It specifies the minimum estimated number of days | [optional] 

## Example

```python
from shipping.models.rate_shop_response_rates_inner_delivery_commitment import RateShopResponseRatesInnerDeliveryCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of RateShopResponseRatesInnerDeliveryCommitment from a JSON string
rate_shop_response_rates_inner_delivery_commitment_instance = RateShopResponseRatesInnerDeliveryCommitment.from_json(json)
# print the JSON string representation of the object
print(RateShopResponseRatesInnerDeliveryCommitment.to_json())

# convert the object into a dict
rate_shop_response_rates_inner_delivery_commitment_dict = rate_shop_response_rates_inner_delivery_commitment_instance.to_dict()
# create an instance of RateShopResponseRatesInnerDeliveryCommitment from a dict
rate_shop_response_rates_inner_delivery_commitment_from_dict = RateShopResponseRatesInnerDeliveryCommitment.from_dict(rate_shop_response_rates_inner_delivery_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


