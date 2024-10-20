# ManifestDetailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account which is used while creating Manifest. | [optional] 
**carrier_name** | **str** | Name of the Carrier. | [optional] 
**manifest_documents** | [**List[ManifestDetailedResponseManifestDocumentsInner]**](ManifestDetailedResponseManifestDocumentsInner.md) | The electronically generated document that has manifest (end-of-day) records of all shipments of the day. | [optional] 
**manifest_id** | **str** | The unique manifest ID. This field is not returned for APAC Services. | [optional] 
**manifest_tracking_number** | **str** | The manifest tracking number. This is returned only if the carrier has a pre-defined valid value, e.g., UPS, FedEX, or USPS. | [optional] 
**from_address** | [**ManifestDetailedResponseFromAddress**](ManifestDetailedResponseFromAddress.md) |  | [optional] 
**parcel_tracking_numbers** | **List[object]** |  | [optional] 
**submission_date** | **str** | The date the shipments are to be tendered to the carrier, entered as YYYY-MM-DD. | [optional] 

## Example

```python
from shipping.models.manifest_detailed_response import ManifestDetailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestDetailedResponse from a JSON string
manifest_detailed_response_instance = ManifestDetailedResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestDetailedResponse.to_json())

# convert the object into a dict
manifest_detailed_response_dict = manifest_detailed_response_instance.to_dict()
# create an instance of ManifestDetailedResponse from a dict
manifest_detailed_response_from_dict = ManifestDetailedResponse.from_dict(manifest_detailed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


