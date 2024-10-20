# GetCarrierAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_accounts** | [**List[GetCarrierAccounts200ResponseCarrierAccountsInner]**](GetCarrierAccounts200ResponseCarrierAccountsInner.md) |  | [optional] 

## Example

```python
from shipping.models.get_carrier_accounts200_response import GetCarrierAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCarrierAccounts200Response from a JSON string
get_carrier_accounts200_response_instance = GetCarrierAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetCarrierAccounts200Response.to_json())

# convert the object into a dict
get_carrier_accounts200_response_dict = get_carrier_accounts200_response_instance.to_dict()
# create an instance of GetCarrierAccounts200Response from a dict
get_carrier_accounts200_response_from_dict = GetCarrierAccounts200Response.from_dict(get_carrier_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


