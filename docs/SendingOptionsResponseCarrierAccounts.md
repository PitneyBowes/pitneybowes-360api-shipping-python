# SendingOptionsResponseCarrierAccounts

Name of the carrier account which is provided while adding carrier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key mapped with the name of the carrier. | [optional] 
**value** | **str** | Value mapped with the CarrierAccount of the used carrier. | [optional] 

## Example

```python
from shipping.models.sending_options_response_carrier_accounts import SendingOptionsResponseCarrierAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of SendingOptionsResponseCarrierAccounts from a JSON string
sending_options_response_carrier_accounts_instance = SendingOptionsResponseCarrierAccounts.from_json(json)
# print the JSON string representation of the object
print(SendingOptionsResponseCarrierAccounts.to_json())

# convert the object into a dict
sending_options_response_carrier_accounts_dict = sending_options_response_carrier_accounts_instance.to_dict()
# create an instance of SendingOptionsResponseCarrierAccounts from a dict
sending_options_response_carrier_accounts_from_dict = SendingOptionsResponseCarrierAccounts.from_dict(sending_options_response_carrier_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


