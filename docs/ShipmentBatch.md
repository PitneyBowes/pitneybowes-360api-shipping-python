# ShipmentBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | This is the system generated Batch ID. | [optional] 
**name** | **str** | Name of the Batch. | [optional] 
**group_name** | **str** |  The group name of the Batch. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**upload_url** | **str** | If this is an import batch, this is the URL to upload the .CSV file. | [optional] 

## Example

```python
from shipping.models.shipment_batch import ShipmentBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBatch from a JSON string
shipment_batch_instance = ShipmentBatch.from_json(json)
# print the JSON string representation of the object
print(ShipmentBatch.to_json())

# convert the object into a dict
shipment_batch_dict = shipment_batch_instance.to_dict()
# create an instance of ShipmentBatch from a dict
shipment_batch_from_dict = ShipmentBatch.from_dict(shipment_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


