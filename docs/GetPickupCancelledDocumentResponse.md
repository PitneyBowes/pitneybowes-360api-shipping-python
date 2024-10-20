# GetPickupCancelledDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | It displays the URL for the receipt generated. | [optional] 

## Example

```python
from shipping.models.get_pickup_cancelled_document_response import GetPickupCancelledDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickupCancelledDocumentResponse from a JSON string
get_pickup_cancelled_document_response_instance = GetPickupCancelledDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetPickupCancelledDocumentResponse.to_json())

# convert the object into a dict
get_pickup_cancelled_document_response_dict = get_pickup_cancelled_document_response_instance.to_dict()
# create an instance of GetPickupCancelledDocumentResponse from a dict
get_pickup_cancelled_document_response_from_dict = GetPickupCancelledDocumentResponse.from_dict(get_pickup_cancelled_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


