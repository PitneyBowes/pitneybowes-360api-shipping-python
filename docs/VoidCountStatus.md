# VoidCountStatus

Indicates the status of shipping labels/shipments which are sent to be cancelled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of shipment labels which have been successfully cancelled. | [optional] 
**failed** | **float** | The number of shipment labels which failed cancelling due to some validation issue. | [optional] 
**pending** | **float** | The number of shipment labels which are pending and in-queue to be cancelled. | [optional] 

## Example

```python
from shipping.models.void_count_status import VoidCountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VoidCountStatus from a JSON string
void_count_status_instance = VoidCountStatus.from_json(json)
# print the JSON string representation of the object
print(VoidCountStatus.to_json())

# convert the object into a dict
void_count_status_dict = void_count_status_instance.to_dict()
# create an instance of VoidCountStatus from a dict
void_count_status_from_dict = VoidCountStatus.from_dict(void_count_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


