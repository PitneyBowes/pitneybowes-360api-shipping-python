# GetAllShipments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**GetAllPickupsPageInfo**](GetAllPickupsPageInfo.md) |  | [optional] 
**data** | [**List[GetAllShipmentsDataInner]**](GetAllShipmentsDataInner.md) |  | [optional] 

## Example

```python
from shipping.models.get_all_shipments import GetAllShipments

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllShipments from a JSON string
get_all_shipments_instance = GetAllShipments.from_json(json)
# print the JSON string representation of the object
print(GetAllShipments.to_json())

# convert the object into a dict
get_all_shipments_dict = get_all_shipments_instance.to_dict()
# create an instance of GetAllShipments from a dict
get_all_shipments_from_dict = GetAllShipments.from_dict(get_all_shipments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


