# ReturnLabelResponseRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_charge** | **float** | Description | [optional] 
**carrier** | **str** | Description | [optional] 
**currency_code** | **str** | Description | [optional] 
**parcel_type** | **str** | Description | [optional] 
**rate_type_id** | **str** | Description | [optional] 
**service_id** | **str** | Description | [optional] 
**special_services** | [**List[ReturnLabelResponseRateSpecialServicesInner]**](ReturnLabelResponseRateSpecialServicesInner.md) |  | [optional] 
**surcharges** | [**List[ReturnLabelResponseRateSurchargesInner]**](ReturnLabelResponseRateSurchargesInner.md) |  | [optional] 
**total_carrier_charge** | **float** | Description | [optional] 

## Example

```python
from shipping.models.return_label_response_rate import ReturnLabelResponseRate

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelResponseRate from a JSON string
return_label_response_rate_instance = ReturnLabelResponseRate.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelResponseRate.to_json())

# convert the object into a dict
return_label_response_rate_dict = return_label_response_rate_instance.to_dict()
# create an instance of ReturnLabelResponseRate from a dict
return_label_response_rate_from_dict = ReturnLabelResponseRate.from_dict(return_label_response_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


