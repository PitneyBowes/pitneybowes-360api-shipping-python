# RateResponseV2DeliveryCommitment

Check for estimated delivery date, guarantee (if any), and number of days for shipment to be delivered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_delivery_date_time** | **str** | Estimated Delivery Date. | [optional] 
**max_estimated_number_of_days** | **str** | Max days to deliver shipment. | [optional] 
**guarantee** | **str** | Checks if there is any guarantee or committment for shipment delivery. | [optional] 

## Example

```python
from shipping.models.rate_response_v2_delivery_commitment import RateResponseV2DeliveryCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of RateResponseV2DeliveryCommitment from a JSON string
rate_response_v2_delivery_commitment_instance = RateResponseV2DeliveryCommitment.from_json(json)
# print the JSON string representation of the object
print(RateResponseV2DeliveryCommitment.to_json())

# convert the object into a dict
rate_response_v2_delivery_commitment_dict = rate_response_v2_delivery_commitment_instance.to_dict()
# create an instance of RateResponseV2DeliveryCommitment from a dict
rate_response_v2_delivery_commitment_from_dict = RateResponseV2DeliveryCommitment.from_dict(rate_response_v2_delivery_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


