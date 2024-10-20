# BulkShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  This is the system generated Batch ID. | [optional] 
**group_name** | **str** | This indicates group name for the Batch. | [optional] 
**name** | **str** |  The name of the Batch. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**address_validation** | [**CounterStatus**](.md) |  | [optional] 
**rating** | [**CounterStatus**](.md) |  | [optional] 
**label_generation** | [**CounterStatus**](.md) |  | [optional] 

## Example

```python
from shipping.models.bulk_shipment_response import BulkShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkShipmentResponse from a JSON string
bulk_shipment_response_instance = BulkShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(BulkShipmentResponse.to_json())

# convert the object into a dict
bulk_shipment_response_dict = bulk_shipment_response_instance.to_dict()
# create an instance of BulkShipmentResponse from a dict
bulk_shipment_response_from_dict = BulkShipmentResponse.from_dict(bulk_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


