# GetStatusDetailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  This is a system-generated unique identifier assigned to the Batch while it is processed. | [optional] 
**name** | **str** |  Name of the of Batch which consists of multiple shipments (shipments in bulk). | [optional] 
**group_name** | **str** | Indicates the name of the group of batches, which consists of multiple Batch groups. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**var_import** | [**ImportCountStatus**](.md) |  | [optional] 
**address_validation** | [**AddressCountStatus**](.md) |  | [optional] 
**rating** | [**RatingCountStatus**](.md) |  | [optional] 
**label_generation** | [**LabelGenerationCountStatus**](.md) |  | [optional] 
**void_label** | [**VoidCountStatus**](.md) |  | [optional] 
**label_details** | [**GetStatusDetailedResponseLabelDetails**](GetStatusDetailedResponseLabelDetails.md) |  | [optional] 

## Example

```python
from shipping.models.get_status_detailed_response import GetStatusDetailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusDetailedResponse from a JSON string
get_status_detailed_response_instance = GetStatusDetailedResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatusDetailedResponse.to_json())

# convert the object into a dict
get_status_detailed_response_dict = get_status_detailed_response_instance.to_dict()
# create an instance of GetStatusDetailedResponse from a dict
get_status_detailed_response_from_dict = GetStatusDetailedResponse.from_dict(get_status_detailed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


