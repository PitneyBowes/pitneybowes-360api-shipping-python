# GetShipmentsForBatchPageInfo

It displays the pagination details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** | It displays current page number. | [optional] 
**pages** | **float** | It displays total number of pages. | [optional] 
**total** | **float** | It displays total records which are filtered. | [optional] 

## Example

```python
from shipping.models.get_shipments_for_batch_page_info import GetShipmentsForBatchPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentsForBatchPageInfo from a JSON string
get_shipments_for_batch_page_info_instance = GetShipmentsForBatchPageInfo.from_json(json)
# print the JSON string representation of the object
print(GetShipmentsForBatchPageInfo.to_json())

# convert the object into a dict
get_shipments_for_batch_page_info_dict = get_shipments_for_batch_page_info_instance.to_dict()
# create an instance of GetShipmentsForBatchPageInfo from a dict
get_shipments_for_batch_page_info_from_dict = GetShipmentsForBatchPageInfo.from_dict(get_shipments_for_batch_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


