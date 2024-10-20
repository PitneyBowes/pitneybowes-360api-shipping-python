# SpecialServiceBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_parameters** | [**List[Parameter]**](Parameter.md) | &gt;- The parameters to set for the special service, such as an insurance value or a receipt-number format. This is required if the special service requires input parameters. If a special service does not require input parameters, you can either leave out the array or pass an empty array. | [optional] 
**specialservice_id** | **str** | A unique identifier associated with the special service to be applied. | 

## Example

```python
from shipping.models.special_service_batch import SpecialServiceBatch

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceBatch from a JSON string
special_service_batch_instance = SpecialServiceBatch.from_json(json)
# print the JSON string representation of the object
print(SpecialServiceBatch.to_json())

# convert the object into a dict
special_service_batch_dict = special_service_batch_instance.to_dict()
# create an instance of SpecialServiceBatch from a dict
special_service_batch_from_dict = SpecialServiceBatch.from_dict(special_service_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


