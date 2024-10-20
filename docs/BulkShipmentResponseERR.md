# BulkShipmentResponseERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  This is a system-generated unique identifier assigned to the Batch while it is processed. | [optional] 
**name** | **str** |  Name of the of ERR Batch which consists of multiple shipments (shipments in bulk). | [optional] 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**address_validation** | [**AddressCountStatus**](.md) |  | [optional] 
**rating** | [**RatingCountStatusERR**](.md) |  | [optional] 
**label_generation** | [**LabelGenerationCountStatus**](.md) |  | [optional] 
**label_details** | [**BulkShipmentResponseERRLabelDetails**](BulkShipmentResponseERRLabelDetails.md) |  | [optional] 

## Example

```python
from shipping.models.bulk_shipment_response_err import BulkShipmentResponseERR

# TODO update the JSON string below
json = "{}"
# create an instance of BulkShipmentResponseERR from a JSON string
bulk_shipment_response_err_instance = BulkShipmentResponseERR.from_json(json)
# print the JSON string representation of the object
print(BulkShipmentResponseERR.to_json())

# convert the object into a dict
bulk_shipment_response_err_dict = bulk_shipment_response_err_instance.to_dict()
# create an instance of BulkShipmentResponseERR from a dict
bulk_shipment_response_err_from_dict = BulkShipmentResponseERR.from_dict(bulk_shipment_response_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


