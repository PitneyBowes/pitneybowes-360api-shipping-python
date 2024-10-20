# GetShipmentsForBatchDataInnerMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key of metadata is CostAccount. User needs to enter the name of the CostAccount. | [optional] 
**value** | **str** | User needs to enter the Cost Account Code. | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_data_inner_metadata_inner import GetShipmentsForBatchDataInnerMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchDataInnerMetadataInner from a JSON string
get_shipments_for_batch_data_inner_metadata_inner_instance = GetShipmentsForBatchDataInnerMetadataInner.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchDataInnerMetadataInner.to_json())

# convert the object into a dict
get_shipments_for_batch_data_inner_metadata_inner_dict = get_shipments_for_batch_data_inner_metadata_inner_instance.to_dict()
# create an instance of GetShipmentsForBatchDataInnerMetadataInner from a dict
get_shipments_for_batch_data_inner_metadata_inner_from_dict = GetShipmentsForBatchDataInnerMetadataInner.from_dict(get_shipments_for_batch_data_inner_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


