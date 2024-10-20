# SpecialServiceBatchERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_parameters** | [**List[Parameter]**](Parameter.md) | &gt;- These parameters are required to set for the special service, such as an Insurance value or a Receipt-number format. This is applicable only when Special Service requires input parameters. If a Special Service does not require input parameters, user can or pass an empty array. | [optional] 
**specialservice_id** | **str** | A unique identifier associated with the special service which varies based on selected USPS Service and ParcelTypes/PackageTypes. | 

## Example

```python
from shipping.models.special_service_batch_err import SpecialServiceBatchERR

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceBatchERR from a JSON string
special_service_batch_err_instance = SpecialServiceBatchERR.from_json(json)
# print the JSON string representation of the object
print(SpecialServiceBatchERR.to_json())

# convert the object into a dict
special_service_batch_err_dict = special_service_batch_err_instance.to_dict()
# create an instance of SpecialServiceBatchERR from a dict
special_service_batch_err_from_dict = SpecialServiceBatchERR.from_dict(special_service_batch_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


