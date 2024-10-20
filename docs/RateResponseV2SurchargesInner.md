# RateResponseV2SurchargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The amount of the surcharge. | [optional] 
**name** | **str** | The type of surcharge. | [optional] 

## Example

```python
from shipping.models.rate_response_v2_surcharges_inner import RateResponseV2SurchargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RateResponseV2SurchargesInner from a JSON string
rate_response_v2_surcharges_inner_instance = RateResponseV2SurchargesInner.from_json(json)
# print the JSON string representation of the object
print(RateResponseV2SurchargesInner.to_json())

# convert the object into a dict
rate_response_v2_surcharges_inner_dict = rate_response_v2_surcharges_inner_instance.to_dict()
# create an instance of RateResponseV2SurchargesInner from a dict
rate_response_v2_surcharges_inner_from_dict = RateResponseV2SurchargesInner.from_dict(rate_response_v2_surcharges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


