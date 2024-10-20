# GetShipmentsForBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetShipmentsForBatchDataInner]**](GetShipmentsForBatchDataInner.md) | It displays all the shipment details based on the paramter selected in the request body. | [optional] 
**page_info** | [**GetShipmentsForBatchPageInfo**](GetShipmentsForBatchPageInfo.md) |  | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch import GetShipmentsForBatch

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatch from a JSON string
get_shipments_for_batch_instance = GetShipmentsForBatch.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatch.to_json())

# convert the object into a dict
get_shipments_for_batch_dict = get_shipments_for_batch_instance.to_dict()
# create an instance of GetShipmentsForBatch from a dict
get_shipments_for_batch_from_dict = GetShipmentsForBatch.from_dict(get_shipments_for_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


