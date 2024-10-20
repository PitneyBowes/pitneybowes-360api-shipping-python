# SingleRateResponseRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | The base service charge is payable to the carrier, excluding special service charges. | [optional] 
**carrier** | **str** | Carrier is a service used to transport the parcels or couriers from one place to another. | [optional] 
**carrier_account** | **str** | Carrier Account is the account associated to specific carrier service. | [optional] 
**delivery_commitment** | [**RateShopResponseRatesInnerDeliveryCommitment**](RateShopResponseRatesInnerDeliveryCommitment.md) |  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. ParcelType have categories like Package, Envelopes, Paks, Boxes, Tube, etc.  | [optional] 
**parcel_id** | **str** | It indicates parcelId chosen in the request if was provided | [optional] 
**rate_type_id** | **str** | Its value can be CONTRACT_RATES, COMMERCIAL or COMMERCIAL_BASE for USPS and COMMERCIAL for other carriers depending on the Pitney Bowes contract/subscription | [optional] 
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 
**special_services** | [**List[SingleRateResponseRatesInnerSpecialServicesInner]**](SingleRateResponseRatesInnerSpecialServicesInner.md) |  This provides a carrier-service based special or extra sevice. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties. | [optional] 
**is_hazmat** | **bool** | It indicated if isHazmat is supported by the service | [optional] 

## Example

```python
from shipping.models.single_rate_response_rates_inner import SingleRateResponseRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRateResponseRatesInner from a JSON string
single_rate_response_rates_inner_instance = SingleRateResponseRatesInner.from_json(json)
# print the JSON string representation of the object
print(SingleRateResponseRatesInner.to_json())

# convert the object into a dict
single_rate_response_rates_inner_dict = single_rate_response_rates_inner_instance.to_dict()
# create an instance of SingleRateResponseRatesInner from a dict
single_rate_response_rates_inner_from_dict = SingleRateResponseRatesInner.from_dict(single_rate_response_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


