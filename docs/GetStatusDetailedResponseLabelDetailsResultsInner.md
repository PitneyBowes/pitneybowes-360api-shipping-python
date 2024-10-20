# GetStatusDetailedResponseLabelDetailsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  This indicates URL of the shipping label in PDF format. | [optional] 
**shipment_identifiers** | [**List[GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner]**](GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner.md) |  Indicates the following identifiers related to Shipment. | [optional] 

## Example

```python
from shipping.models.get_status_detailed_response_label_details_results_inner import GetStatusDetailedResponseLabelDetailsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusDetailedResponseLabelDetailsResultsInner from a JSON string
get_status_detailed_response_label_details_results_inner_instance = GetStatusDetailedResponseLabelDetailsResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetStatusDetailedResponseLabelDetailsResultsInner.to_json())

# convert the object into a dict
get_status_detailed_response_label_details_results_inner_dict = get_status_detailed_response_label_details_results_inner_instance.to_dict()
# create an instance of GetStatusDetailedResponseLabelDetailsResultsInner from a dict
get_status_detailed_response_label_details_results_inner_from_dict = GetStatusDetailedResponseLabelDetailsResultsInner.from_dict(get_status_detailed_response_label_details_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


