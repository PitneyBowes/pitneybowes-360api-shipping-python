# ReprintManifestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | The unique identifier associated with the Carrier account which is used while Manifest process. | 
**manifest_id** | **str** | A unique identifier associated to the created Manifest for a particular Carrier. | 

## Example

```python
from shipping.models.reprint_manifest_request import ReprintManifestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintManifestRequest from a JSON string
reprint_manifest_request_instance = ReprintManifestRequest.from_json(json)
# print the JSON string representation of the object
print(ReprintManifestRequest.to_json())

# convert the object into a dict
reprint_manifest_request_dict = reprint_manifest_request_instance.to_dict()
# create an instance of ReprintManifestRequest from a dict
reprint_manifest_request_from_dict = ReprintManifestRequest.from_dict(reprint_manifest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


