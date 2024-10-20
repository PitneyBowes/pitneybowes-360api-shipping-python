# BPODDownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_ids** | **List[str]** | &gt;- This shows the list of Shipment IDs. If this is present, then user does not need to provide &#x60;Date Range&#x60; filter. Else &#x60;startDate&#x60; and &#x60;endDate&#x60; need to be passed in the Query Parameters. | [optional] 

## Example

```python
from shipping.models.bpod_download_request import BPODDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BPODDownloadRequest from a JSON string
bpod_download_request_instance = BPODDownloadRequest.from_json(json)
# print the JSON string representation of the object
print(BPODDownloadRequest.to_json())

# convert the object into a dict
bpod_download_request_dict = bpod_download_request_instance.to_dict()
# create an instance of BPODDownloadRequest from a dict
bpod_download_request_from_dict = BPODDownloadRequest.from_dict(bpod_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


