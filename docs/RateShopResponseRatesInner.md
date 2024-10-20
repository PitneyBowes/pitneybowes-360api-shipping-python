# RateShopResponseRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | The base service charge is payable to the carrier, excluding special service charges. | [optional] 
**carrier** | **str** | Carrier is a service used to transport the parcels or couriers from one place to another. | [optional] 
**carrier_account** | **str** | Carrier Account is the account associated to specific carrier service. | [optional] 
**delivery_commitment** | [**RateShopResponseRatesInnerDeliveryCommitment**](RateShopResponseRatesInnerDeliveryCommitment.md) |  | [optional] 
**currency_code** | **str** | A three-character (all uppercase letter) symbol of a currency according to the international ISO standard. As a rule, the first two letters denote the name of the country, and the third letter, the name of the currency thereof.For example, for US - the currency is Dollars and code is USD. Similarly for Canada, the currencycode is CAD, and for India, it is INR.  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. ParcelType have categories like Package, Envelopes, Paks, Boxes, Tube, etc.  | [optional] 
**parcel_id** | **str** | It indicates parcelId chosen in the request | [optional] 
**rate_type_id** | **str** | Its value can be CONTRACT_RATES, COMMERCIAL or COMMERCIAL_BASE for USPS and COMMERCIAL for other carriers depending on the Pitney Bowes contract/subscription | [optional] 
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 
**surcharges** | [**List[RateShopResponseRatesInnerSurchargesInner]**](RateShopResponseRatesInnerSurchargesInner.md) |  Additional fees or surcharges for the shipment. Each object in the array defines a surcharge and fee. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties | [optional] 

## Example

```python
from shipping.models.rate_shop_response_rates_inner import RateShopResponseRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RateShopResponseRatesInner from a JSON string
rate_shop_response_rates_inner_instance = RateShopResponseRatesInner.from_json(json)
# print the JSON string representation of the object
print(RateShopResponseRatesInner.to_json())

# convert the object into a dict
rate_shop_response_rates_inner_dict = rate_shop_response_rates_inner_instance.to_dict()
# create an instance of RateShopResponseRatesInner from a dict
rate_shop_response_rates_inner_from_dict = RateShopResponseRatesInner.from_dict(rate_shop_response_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


