# CancelStampsRequestERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stamp_ids** | **List[str]** |  This is a list of StampIDs which is used for cancelling ERR postage. | [optional] 

## Example

```python
from shipping.models.cancel_stamps_request_err import CancelStampsRequestERR

# TODO update the JSON string below
json = "{}"
# create an instance of CancelStampsRequestERR from a JSON string
cancel_stamps_request_err_instance = CancelStampsRequestERR.from_json(json)
# print the JSON string representation of the object
print(CancelStampsRequestERR.to_json())

# convert the object into a dict
cancel_stamps_request_err_dict = cancel_stamps_request_err_instance.to_dict()
# create an instance of CancelStampsRequestERR from a dict
cancel_stamps_request_err_from_dict = CancelStampsRequestERR.from_dict(cancel_stamps_request_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


