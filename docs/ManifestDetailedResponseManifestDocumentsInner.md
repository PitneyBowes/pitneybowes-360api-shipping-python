# ManifestDetailedResponseManifestDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Determines type of the document as a URL. &lt;br&gt;- URL: The response returns a link to the label or manifest. | [optional] 
**contents** | **str** | When contentType is URL, this is the URL to access the label or manifest. Note: The document is available for 24 hours after it is created. | [optional] 
**type** | **str** | Specifies the type of manifest. | [optional] 

## Example

```python
from shipping.models.manifest_detailed_response_manifest_documents_inner import ManifestDetailedResponseManifestDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestDetailedResponseManifestDocumentsInner from a JSON string
manifest_detailed_response_manifest_documents_inner_instance = ManifestDetailedResponseManifestDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(ManifestDetailedResponseManifestDocumentsInner.to_json())

# convert the object into a dict
manifest_detailed_response_manifest_documents_inner_dict = manifest_detailed_response_manifest_documents_inner_instance.to_dict()
# create an instance of ManifestDetailedResponseManifestDocumentsInner from a dict
manifest_detailed_response_manifest_documents_inner_from_dict = ManifestDetailedResponseManifestDocumentsInner.from_dict(manifest_detailed_response_manifest_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


