# GetShipmentsForBatchDataInnerStepStatus

It displays different status of shipments at each level- addressValidation, rating, labelGeneration, and voidLabel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_import** | **str** | This is only visible for batch submitted during Import via .CSV. | [optional] 
**address_validation** | **str** | It indicates the status of shipments at addressValidation stage. | [optional] 
**rating** | **str** | It indicates status of shipments at rating level. | [optional] 
**label_generation** | **str** | It indicates status of shipments at labelGeneration step. | [optional] 
**void_label** | **str** | It will only be visible when batch labels are cancelled. | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_data_inner_step_status import GetShipmentsForBatchDataInnerStepStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchDataInnerStepStatus from a JSON string
get_shipments_for_batch_data_inner_step_status_instance = GetShipmentsForBatchDataInnerStepStatus.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchDataInnerStepStatus.to_json())

# convert the object into a dict
get_shipments_for_batch_data_inner_step_status_dict = get_shipments_for_batch_data_inner_step_status_instance.to_dict()
# create an instance of GetShipmentsForBatchDataInnerStepStatus from a dict
get_shipments_for_batch_data_inner_step_status_from_dict = GetShipmentsForBatchDataInnerStepStatus.from_dict(get_shipments_for_batch_data_inner_step_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


