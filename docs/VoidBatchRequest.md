# VoidBatchRequest

The request to cancel Batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Indicates the name of the Batch, i.e., a list of shipments, which need to be cancelled. | 
**reason** | **str** | Reason to cancel the batch of shipments. | [optional] 
**shipment_ids** | **List[str]** | &gt;- Shipment ID is a unique identifier for an individual shipment. If ShipmentID(s) are passed in the array, then corresponding shipments will be cancelled. If ShipmentID(s) is/are not provided, then the entire shipments of the Batch will be cancelled. | [optional] 

## Example

```python
from shipping.models.void_batch_request import VoidBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidBatchRequest from a JSON string
void_batch_request_instance = VoidBatchRequest.from_json(json)
# print the JSON string representation of the object
print(VoidBatchRequest.to_json())

# convert the object into a dict
void_batch_request_dict = void_batch_request_instance.to_dict()
# create an instance of VoidBatchRequest from a dict
void_batch_request_from_dict = VoidBatchRequest.from_dict(void_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


