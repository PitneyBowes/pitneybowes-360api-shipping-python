# SendingOptions

Sending Options will include carrier and its account details, sender details, and parcel details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** | Name of the carrier. E.g., FedEx. | [optional] 
**service** | **str** | Name of the carrier-based service. E.g., 2DA. | [optional] 
**carrier_accounts** | [**SendingOptionsCarrierAccounts**](SendingOptionsCarrierAccounts.md) |  | [optional] 
**label_size** | **str** | Size of the label, e.g., DOC_4X6. | [optional] 
**label_type** | **str** | Type of the Label, e.g., Shipping_Label. | [optional] 
**label_format** | **str** | Format of the Label, e.g., PDF. | [optional] 
**from_address** | [**FromAddressV2**](FromAddressV2.md) |  | [optional] 
**parcel** | [**ParcelV2**](ParcelV2.md) |  | [optional] 

## Example

```python
from shipping.models.sending_options import SendingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SendingOptions from a JSON string
sending_options_instance = SendingOptions.from_json(json)
# print the JSON string representation of the object
print(SendingOptions.to_json())

# convert the object into a dict
sending_options_dict = sending_options_instance.to_dict()
# create an instance of SendingOptions from a dict
sending_options_from_dict = SendingOptions.from_dict(sending_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


