# SingleRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**SingleRateResponseFromAddress**](SingleRateResponseFromAddress.md) |  | [optional] 
**parcel** | [**SingleRateResponseParcel**](SingleRateResponseParcel.md) |  | [optional] 
**rates** | [**List[SingleRateResponseRatesInner]**](SingleRateResponseRatesInner.md) | It displays the rate for the required carrier-service and/or special service combinaion | [optional] 
**to_address** | [**SingleRateResponseToAddress**](SingleRateResponseToAddress.md) |  | [optional] 

## Example

```python
from shipping.models.single_rate_response import SingleRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleRateResponse from a JSON string
single_rate_response_instance = SingleRateResponse.from_json(json)
# print the JSON string representation of the object
print(SingleRateResponse.to_json())

# convert the object into a dict
single_rate_response_dict = single_rate_response_instance.to_dict()
# create an instance of SingleRateResponse from a dict
single_rate_response_from_dict = SingleRateResponse.from_dict(single_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


