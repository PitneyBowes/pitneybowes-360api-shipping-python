# GetCarrierAccounts200ResponseCarrierAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | A unique identifier assigned to the specific carrier account. | [optional] 
**carrier_name** | **str** | Name of the carrier. | [optional] 
**description** | **str** | Description of this carrier account. | [optional] 

## Example

```python
from shipping.models.get_carrier_accounts200_response_carrier_accounts_inner import GetCarrierAccounts200ResponseCarrierAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCarrierAccounts200ResponseCarrierAccountsInner from a JSON string
get_carrier_accounts200_response_carrier_accounts_inner_instance = GetCarrierAccounts200ResponseCarrierAccountsInner.from_json(json)
# print the JSON string representation of the object
print(GetCarrierAccounts200ResponseCarrierAccountsInner.to_json())

# convert the object into a dict
get_carrier_accounts200_response_carrier_accounts_inner_dict = get_carrier_accounts200_response_carrier_accounts_inner_instance.to_dict()
# create an instance of GetCarrierAccounts200ResponseCarrierAccountsInner from a dict
get_carrier_accounts200_response_carrier_accounts_inner_from_dict = GetCarrierAccounts200ResponseCarrierAccountsInner.from_dict(get_carrier_accounts200_response_carrier_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


