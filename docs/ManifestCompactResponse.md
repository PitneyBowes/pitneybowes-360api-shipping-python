# ManifestCompactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_documents** | [**List[ManifestCompactResponseManifestDocumentsInner]**](ManifestCompactResponseManifestDocumentsInner.md) |  | [optional] 
**manifest_id** | **str** |  | [optional] 
**manifest_tracking_number** | **str** |  | [optional] 

## Example

```python
from shipping.models.manifest_compact_response import ManifestCompactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestCompactResponse from a JSON string
manifest_compact_response_instance = ManifestCompactResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestCompactResponse.to_json())

# convert the object into a dict
manifest_compact_response_dict = manifest_compact_response_instance.to_dict()
# create an instance of ManifestCompactResponse from a dict
manifest_compact_response_from_dict = ManifestCompactResponse.from_dict(manifest_compact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


