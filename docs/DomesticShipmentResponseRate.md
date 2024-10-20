# DomesticShipmentResponseRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | The base service charge is payable to the carrier, excluding special service charges. | [optional] 
**carrier** | **str** | Carrier is a service used to transport the parcels or couriers from one place to another. | [optional] 
**currency_code** | **str** | A three-character (all uppercase letter) symbol of a currency according to the international ISO standard. As a rule, the first two letters denote the name of the country, and the third letter, the name of the currency thereof.For example, for US - the currency is Dollars and code is USD. Similarly for Canada, the currencycode is CAD, and for India, it is INR.  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. ParcelType have categories like Package, Envelopes, Paks, Boxes, Tube, etc.  | [optional] 
**rate_type_id** | **str** | Its value can be CONTRACT_RATES, COMMERCIAL or COMMERCIAL_BASE for USPS and COMMERCIAL for other carriers depending on the Pitney Bowes contract/subscription | [optional] 
**service_id** | **str** | The unique identifier given to the carrier specific service. | [optional] 
**special_services** | [**List[DomesticShipmentResponseRateSpecialServicesInner]**](DomesticShipmentResponseRateSpecialServicesInner.md) | This provides a carrier-service based special or extra sevice. | [optional] 
**total_carrier_charge** | **float** | The total amount payable to the carrier, including special service fees, surcharges, and any international taxes and duties, except as noted below: | [optional] 

## Example

```python
from shipping.models.domestic_shipment_response_rate import DomesticShipmentResponseRate

# TODO update the JSON string below
json = "{}"
# create an instance of DomesticShipmentResponseRate from a JSON string
domestic_shipment_response_rate_instance = DomesticShipmentResponseRate.from_json(json)
# print the JSON string representation of the object
print(DomesticShipmentResponseRate.to_json())

# convert the object into a dict
domestic_shipment_response_rate_dict = domestic_shipment_response_rate_instance.to_dict()
# create an instance of DomesticShipmentResponseRate from a dict
domestic_shipment_response_rate_from_dict = DomesticShipmentResponseRate.from_dict(domestic_shipment_response_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


