# SpecialServicesServicesInnerParcelTypeRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branded_name** | **str** | The branded name of Parcel Type | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection. Here, it reflects as per the defined ParcelType Rules. ParcelType have categories like Package, Envelopes, Paks, Boxes, Tube, etc.  | [optional] 
**trackable** | **str** | Whether this parcel type is trackable. Valid Values are: TRACKABLE, NON_TRACKABLE, REQUIRES_TRACKABLE_SPECIAL_SERVICE | [optional] 
**suggested_trackable_special_service** | **str** | If trackable is set to REQUIRES_TRACKABLE_SPECIAL_SERVICE, this is a free or low-cost special service that allows the shipper to track the shipment. | [optional] 
**special_service_rules** | [**List[SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner]**](SpecialServicesServicesInnerParcelTypeRulesInnerSpecialServiceRulesInner.md) | It displays all the available special services, their details and prerequisites and/or incompatible details with other special services | [optional] 

## Example

```python
from shipping.models.special_services_services_inner_parcel_type_rules_inner import SpecialServicesServicesInnerParcelTypeRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServicesServicesInnerParcelTypeRulesInner from a JSON string
special_services_services_inner_parcel_type_rules_inner_instance = SpecialServicesServicesInnerParcelTypeRulesInner.from_json(json)
# print the JSON string representation of the object
print(SpecialServicesServicesInnerParcelTypeRulesInner.to_json())

# convert the object into a dict
special_services_services_inner_parcel_type_rules_inner_dict = special_services_services_inner_parcel_type_rules_inner_instance.to_dict()
# create an instance of SpecialServicesServicesInnerParcelTypeRulesInner from a dict
special_services_services_inner_parcel_type_rules_inner_from_dict = SpecialServicesServicesInnerParcelTypeRulesInner.from_dict(special_services_services_inner_parcel_type_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


