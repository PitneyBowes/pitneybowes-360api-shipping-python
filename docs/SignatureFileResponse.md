# SignatureFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | Indicates the shipment identifier, a unique identifier for an individual shipment. | [optional] 
**signature_file_url** | **str** | A link or URL that consists of Proof of Delivery (POD) - Recipient&#39;s Signature image file. Clicking the link will download the POD Signature. | [optional] 

## Example

```python
from shipping.models.signature_file_response import SignatureFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureFileResponse from a JSON string
signature_file_response_instance = SignatureFileResponse.from_json(json)
# print the JSON string representation of the object
print(SignatureFileResponse.to_json())

# convert the object into a dict
signature_file_response_dict = signature_file_response_instance.to_dict()
# create an instance of SignatureFileResponse from a dict
signature_file_response_from_dict = SignatureFileResponse.from_dict(signature_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


