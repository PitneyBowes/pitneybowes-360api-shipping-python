# ManifestCompactResponseManifestDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | The media type of the request entity. | [optional] 
**contents** | **str** | The defines the contents, e.g. URL. | [optional] 
**type** | **str** | The defines the type of contents, e.g. Manifest. | [optional] 

## Example

```python
from shipping.models.manifest_compact_response_manifest_documents_inner import ManifestCompactResponseManifestDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestCompactResponseManifestDocumentsInner from a JSON string
manifest_compact_response_manifest_documents_inner_instance = ManifestCompactResponseManifestDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(ManifestCompactResponseManifestDocumentsInner.to_json())

# convert the object into a dict
manifest_compact_response_manifest_documents_inner_dict = manifest_compact_response_manifest_documents_inner_instance.to_dict()
# create an instance of ManifestCompactResponseManifestDocumentsInner from a dict
manifest_compact_response_manifest_documents_inner_from_dict = ManifestCompactResponseManifestDocumentsInner.from_dict(manifest_compact_response_manifest_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


