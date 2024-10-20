# GetAllPickups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**GetAllPickupsPageInfo**](GetAllPickupsPageInfo.md) |  | [optional] 
**data** | [**List[GetAllPickupsDataInner]**](GetAllPickupsDataInner.md) |  | [optional] 

## Example

```python
from shipping.models.get_all_pickups import GetAllPickups

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPickups from a JSON string
get_all_pickups_instance = GetAllPickups.from_json(json)
# print the JSON string representation of the object
print(GetAllPickups.to_json())

# convert the object into a dict
get_all_pickups_dict = get_all_pickups_instance.to_dict()
# create an instance of GetAllPickups from a dict
get_all_pickups_from_dict = GetAllPickups.from_dict(get_all_pickups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


