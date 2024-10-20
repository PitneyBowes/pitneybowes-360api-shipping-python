# CreateManifest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | A unique identifier associated with the Carrier account which is used while creating Manifest. | [optional] 
**carrier_name** | **str** | Name of the Carrier. | [optional] 
**manifest_documents** | [**List[ManifestCompactResponseManifestDocumentsInner]**](ManifestCompactResponseManifestDocumentsInner.md) |  | [optional] 
**manifest_id** | **str** |  | [optional] 
**manifest_tracking_number** | **str** |  | [optional] 
**from_address** | [**ManifestDetailedResponseFromAddress**](ManifestDetailedResponseFromAddress.md) |  | [optional] 
**parcel_tracking_numbers** | **List[object]** |  | [optional] 
**submission_date** | **str** | The date the shipments are to be tendered to the carrier, entered as YYYY-MM-DD. | [optional] 

## Example

```python
from shipping.models.create_manifest200_response import CreateManifest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManifest200Response from a JSON string
create_manifest200_response_instance = CreateManifest200Response.from_json(json)
# print the JSON string representation of the object
print(CreateManifest200Response.to_json())

# convert the object into a dict
create_manifest200_response_dict = create_manifest200_response_instance.to_dict()
# create an instance of CreateManifest200Response from a dict
create_manifest200_response_from_dict = CreateManifest200Response.from_dict(create_manifest200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


