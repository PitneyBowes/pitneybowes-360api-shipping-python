# AllDefaultsPageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Defines Total number of records. | [optional] 
**pages** | **int** | Defines Total number of pages. | [optional] 
**page** | **int** | Defines Current page number. | [optional] 

## Example

```python
from shipping.models.all_defaults_page_info import AllDefaultsPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AllDefaultsPageInfo from a JSON string
all_defaults_page_info_instance = AllDefaultsPageInfo.from_json(json)
# print the JSON string representation of the object
print(AllDefaultsPageInfo.to_json())

# convert the object into a dict
all_defaults_page_info_dict = all_defaults_page_info_instance.to_dict()
# create an instance of AllDefaultsPageInfo from a dict
all_defaults_page_info_from_dict = AllDefaultsPageInfo.from_dict(all_defaults_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


