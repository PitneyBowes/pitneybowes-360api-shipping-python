# CancelStampsResponseERR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_form_url** | **str** | This is the *Refund Form* having postage details | [optional] 

## Example

```python
from shipping.models.cancel_stamps_response_err import CancelStampsResponseERR

# TODO update the JSON string below
json = "{}"
# create an instance of CancelStampsResponseERR from a JSON string
cancel_stamps_response_err_instance = CancelStampsResponseERR.from_json(json)
# print the JSON string representation of the object
print(CancelStampsResponseERR.to_json())

# convert the object into a dict
cancel_stamps_response_err_dict = cancel_stamps_response_err_instance.to_dict()
# create an instance of CancelStampsResponseERR from a dict
cancel_stamps_response_err_from_dict = CancelStampsResponseERR.from_dict(cancel_stamps_response_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


