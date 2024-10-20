# GetStatusDetailedResponseLabelDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | [**BulkShipmentResponseERRLabelDetailsLayout**](BulkShipmentResponseERRLabelDetailsLayout.md) |  | [optional] 
**results** | [**List[GetStatusDetailedResponseLabelDetailsResultsInner]**](GetStatusDetailedResponseLabelDetailsResultsInner.md) |  This indicates the results of the label generation. | [optional] 

## Example

```python
from shipping.models.get_status_detailed_response_label_details import GetStatusDetailedResponseLabelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusDetailedResponseLabelDetails from a JSON string
get_status_detailed_response_label_details_instance = GetStatusDetailedResponseLabelDetails.from_json(json)
# print the JSON string representation of the object
print(GetStatusDetailedResponseLabelDetails.to_json())

# convert the object into a dict
get_status_detailed_response_label_details_dict = get_status_detailed_response_label_details_instance.to_dict()
# create an instance of GetStatusDetailedResponseLabelDetails from a dict
get_status_detailed_response_label_details_from_dict = GetStatusDetailedResponseLabelDetails.from_dict(get_status_detailed_response_label_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


