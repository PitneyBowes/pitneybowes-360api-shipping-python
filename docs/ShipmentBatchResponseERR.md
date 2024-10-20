# ShipmentBatchResponseERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | This is a system-generated unique identifier assigned to the ERR Batch while it is processed. | [optional] 
**name** | **str** | Name of the of ERR Batch which consists of multiple shipments (shipments in bulk). | [optional] 
**group_name** | **str** |  Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**upload_url** | **str** | For the stored Batch file under S3, this is the S3 returned URL. The URL is uploaded along with the .CSV file to get the BatchID, which is used to track the import status. | [optional] 

## Example

```python
from shipping.models.shipment_batch_response_err import ShipmentBatchResponseERR

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBatchResponseERR from a JSON string
shipment_batch_response_err_instance = ShipmentBatchResponseERR.from_json(json)
# print the JSON string representation of the object
print(ShipmentBatchResponseERR.to_json())

# convert the object into a dict
shipment_batch_response_err_dict = shipment_batch_response_err_instance.to_dict()
# create an instance of ShipmentBatchResponseERR from a dict
shipment_batch_response_err_from_dict = ShipmentBatchResponseERR.from_dict(shipment_batch_response_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


