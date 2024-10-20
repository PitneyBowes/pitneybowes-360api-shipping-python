# AllDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**AllDefaultsPageInfo**](AllDefaultsPageInfo.md) |  | [optional] 
**data** | [**List[AllDefaultsDataInner]**](AllDefaultsDataInner.md) |  | [optional] 

## Example

```python
from shipping.models.all_defaults import AllDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of AllDefaults from a JSON string
all_defaults_instance = AllDefaults.from_json(json)
# print the JSON string representation of the object
print(AllDefaults.to_json())

# convert the object into a dict
all_defaults_dict = all_defaults_instance.to_dict()
# create an instance of AllDefaults from a dict
all_defaults_from_dict = AllDefaults.from_dict(all_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


