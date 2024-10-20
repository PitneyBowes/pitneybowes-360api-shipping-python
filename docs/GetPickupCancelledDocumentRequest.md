# GetPickupCancelledDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_ids** | **List[str]** | It specified the pickup Ids which are cancelled and for which receipt is required. | [optional] 

## Example

```python
from shipping.models.get_pickup_cancelled_document_request import GetPickupCancelledDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickupCancelledDocumentRequest from a JSON string
get_pickup_cancelled_document_request_instance = GetPickupCancelledDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(GetPickupCancelledDocumentRequest.to_json())

# convert the object into a dict
get_pickup_cancelled_document_request_dict = get_pickup_cancelled_document_request_instance.to_dict()
# create an instance of GetPickupCancelledDocumentRequest from a dict
get_pickup_cancelled_document_request_from_dict = GetPickupCancelledDocumentRequest.from_dict(get_pickup_cancelled_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


