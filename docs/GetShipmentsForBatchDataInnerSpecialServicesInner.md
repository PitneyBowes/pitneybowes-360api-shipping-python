# GetShipmentsForBatchDataInnerSpecialServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The amount of the surcharge. | [optional] 
**special_service_id** | **str** | A unique identifier associated with the Special Service, will be mentioned in this column. If user selects additional service will be entered here. | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_data_inner_special_services_inner import GetShipmentsForBatchDataInnerSpecialServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchDataInnerSpecialServicesInner from a JSON string
get_shipments_for_batch_data_inner_special_services_inner_instance = GetShipmentsForBatchDataInnerSpecialServicesInner.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchDataInnerSpecialServicesInner.to_json())

# convert the object into a dict
get_shipments_for_batch_data_inner_special_services_inner_dict = get_shipments_for_batch_data_inner_special_services_inner_instance.to_dict()
# create an instance of GetShipmentsForBatchDataInnerSpecialServicesInner from a dict
get_shipments_for_batch_data_inner_special_services_inner_from_dict = GetShipmentsForBatchDataInnerSpecialServicesInner.from_dict(get_shipments_for_batch_data_inner_special_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


