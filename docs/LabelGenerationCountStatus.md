# LabelGenerationCountStatus

Indicates the status of shipping labels/coversheets which are at final steps before printing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of shipment labels which have been successfully generated. | [optional] 
**failed** | **float** | The number of shipment labels which failed processing and could not be generated due to some errors with shipment. | [optional] 
**pending** | **float** | The number of shipment labels which are pending and in-queue to be processed. | [optional] 

## Example

```python
from shipping.models.label_generation_count_status import LabelGenerationCountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LabelGenerationCountStatus from a JSON string
label_generation_count_status_instance = LabelGenerationCountStatus.from_json(json)
# print the JSON string representation of the object
print(LabelGenerationCountStatus.to_json())

# convert the object into a dict
label_generation_count_status_dict = label_generation_count_status_instance.to_dict()
# create an instance of LabelGenerationCountStatus from a dict
label_generation_count_status_from_dict = LabelGenerationCountStatus.from_dict(label_generation_count_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


