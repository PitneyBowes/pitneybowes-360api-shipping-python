# AddressCountStatus

This indicates the status count of addresses which are at validation stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of addresses which have been successfully validated. | [optional] 
**failed** | **float** | The number of addresses failed at validation due to incorrect entry in the address. | [optional] 
**pending** | **float** | The number of addresses which are pending and in-queue to be processed. | [optional] 

## Example

```python
from shipping.models.address_count_status import AddressCountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCountStatus from a JSON string
address_count_status_instance = AddressCountStatus.from_json(json)
# print the JSON string representation of the object
print(AddressCountStatus.to_json())

# convert the object into a dict
address_count_status_dict = address_count_status_instance.to_dict()
# create an instance of AddressCountStatus from a dict
address_count_status_from_dict = AddressCountStatus.from_dict(address_count_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


