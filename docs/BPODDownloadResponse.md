# BPODDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | This is the URL for the BPOD (Bulk Proof of Delivery) ZIP file. | [optional] 

## Example

```python
from shipping.models.bpod_download_response import BPODDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BPODDownloadResponse from a JSON string
bpod_download_response_instance = BPODDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(BPODDownloadResponse.to_json())

# convert the object into a dict
bpod_download_response_dict = bpod_download_response_instance.to_dict()
# create an instance of BPODDownloadResponse from a dict
bpod_download_response_from_dict = BPODDownloadResponse.from_dict(bpod_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


