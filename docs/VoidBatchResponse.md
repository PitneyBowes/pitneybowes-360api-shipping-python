# VoidBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | This is a system-generated unique identifier assigned to the Batch while it is processed. | [optional] 
**status** | **str** | Indicates the status of the Batch while executing &#x60;voidShippingLabel&#x60;. | [optional] 

## Example

```python
from shipping.models.void_batch_response import VoidBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoidBatchResponse from a JSON string
void_batch_response_instance = VoidBatchResponse.from_json(json)
# print the JSON string representation of the object
print(VoidBatchResponse.to_json())

# convert the object into a dict
void_batch_response_dict = void_batch_response_instance.to_dict()
# create an instance of VoidBatchResponse from a dict
void_batch_response_from_dict = VoidBatchResponse.from_dict(void_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


