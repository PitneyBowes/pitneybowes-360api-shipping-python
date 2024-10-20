# GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  This indicates the identifier at DB level mapped with Shipment ID. | [optional] 
**shipment_id** | **str** |  Shipment ID is a unique identifier for an individual shipment. | [optional] 
**external_id** | **str** |  This is a user-defined value provided by users just for their reference. This is for mapping purpose against each shipment. | [optional] 

## Example

```python
from shipping.models.get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner import GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner from a JSON string
get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner_instance = GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner.from_json(json)
# print the JSON string representation of the object
print(GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner.to_json())

# convert the object into a dict
get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner_dict = get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner_instance.to_dict()
# create an instance of GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner from a dict
get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner_from_dict = GetStatusDetailedResponseLabelDetailsResultsInnerShipmentIdentifiersInner.from_dict(get_status_detailed_response_label_details_results_inner_shipment_identifiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


