# Customs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customs_info** | [**CustomsInfo**](CustomsInfo.md) |  | 
**customs_items** | [**List[CustomsItem]**](CustomsItem.md) | This operation asks the information for each commodity for Customs clearance. | 

## Example

```python
from shipping.models.customs import Customs

# TODO update the JSON string below
json = "{}"
# create an instance of Customs from a JSON string
customs_instance = Customs.from_json(json)
# print the JSON string representation of the object
print(Customs.to_json())

# convert the object into a dict
customs_dict = customs_instance.to_dict()
# create an instance of Customs from a dict
customs_from_dict = Customs.from_dict(customs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


