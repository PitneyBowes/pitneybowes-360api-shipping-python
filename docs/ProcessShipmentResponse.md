# ProcessShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  This is a system-generated unique identifier assigned to the Batch while it is processed. | [optional] 
**name** | **str** | Name of the of Batch which consists of multiple shipments (shipments in bulk). | [optional] 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**status** | **str** |  The batch will show the status &#x60;SUBMITTED&#x60; on successful execution of Batch. | [optional] 

## Example

```python
from shipping.models.process_shipment_response import ProcessShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessShipmentResponse from a JSON string
process_shipment_response_instance = ProcessShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(ProcessShipmentResponse.to_json())

# convert the object into a dict
process_shipment_response_dict = process_shipment_response_instance.to_dict()
# create an instance of ProcessShipmentResponse from a dict
process_shipment_response_from_dict = ProcessShipmentResponse.from_dict(process_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


