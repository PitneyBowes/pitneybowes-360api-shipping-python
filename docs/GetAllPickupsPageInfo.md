# GetAllPickupsPageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | This defines Total number of records. | [optional] 
**pages** | **int** | This defines Total number of pages. | [optional] 
**page** | **int** | This defines Current page number. | [optional] 

## Example

```python
from shipping.models.get_all_pickups_page_info import GetAllPickupsPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPickupsPageInfo from a JSON string
get_all_pickups_page_info_instance = GetAllPickupsPageInfo.from_json(json)
# print the JSON string representation of the object
print(GetAllPickupsPageInfo.to_json())

# convert the object into a dict
get_all_pickups_page_info_dict = get_all_pickups_page_info_instance.to_dict()
# create an instance of GetAllPickupsPageInfo from a dict
get_all_pickups_page_info_from_dict = GetAllPickupsPageInfo.from_dict(get_all_pickups_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


