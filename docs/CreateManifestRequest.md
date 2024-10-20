# CreateManifestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_account_id** | **str** | A unique identifier associated with the specific carrier account, which is used in the Manifest process. | 
**from_address** | [**CreateManifestRequestFromAddress**](CreateManifestRequestFromAddress.md) |  | 
**submission_date** | **str** | The date the shipments are to be tendered to the carrier, entered as YYYY-MM-DD. | [optional] 

## Example

```python
from shipping.models.create_manifest_request import CreateManifestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManifestRequest from a JSON string
create_manifest_request_instance = CreateManifestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateManifestRequest.to_json())

# convert the object into a dict
create_manifest_request_dict = create_manifest_request_instance.to_dict()
# create an instance of CreateManifestRequest from a dict
create_manifest_request_from_dict = CreateManifestRequest.from_dict(create_manifest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


