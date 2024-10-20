# RateResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | The base service charge is payable to the carrier, excluding special service charges. | [optional] 
**carrier** | **str** | Carrier is a service used to transport the parcels or couriers from one place to another. | [optional] 
**currency_code** | **str** | A three-character (all uppercase letter) symbol of a currency according to the international ISO standard.&lt;br /&gt; As a rule, the first two letters denote the name of the country, and the third letter, the name of the currency thereof. For example, for US - the currency is Dollars and code is USD. Similarly for Canada, the currencycode is CAD, and for India, it is INR.  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection.&lt;br /&gt; ParcelType have categories like Package, Envelopes, Paks, Boxes, Tube, etc. | [optional] 
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 
**surcharges** | [**List[RateResponseV2SurchargesInner]**](RateResponseV2SurchargesInner.md) | Additional fees or surcharges for the shipment. Each object in the array defines a surcharge and fee. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties, except as noted below: | [optional] 
**delivery_commitment** | [**RateResponseV2DeliveryCommitment**](RateResponseV2DeliveryCommitment.md) |  | [optional] 

## Example

```python
from shipping.models.rate_response_v2 import RateResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of RateResponseV2 from a JSON string
rate_response_v2_instance = RateResponseV2.from_json(json)
# print the JSON string representation of the object
print(RateResponseV2.to_json())

# convert the object into a dict
rate_response_v2_dict = rate_response_v2_instance.to_dict()
# create an instance of RateResponseV2 from a dict
rate_response_v2_from_dict = RateResponseV2.from_dict(rate_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


