# RatingCountStatusERR

This indicates the status count of shipments which are at Rating stage. Rating is a process of assessing the shipping/freight charge associated with the ERR Bulk shipment. Rates are calculated based on selected special/extra services corresponding to the selected Services and ParcelType for USPS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of shipments that have been successfully processed for Ratings. | [optional] 
**failed** | **float** | The number of shipments which failed processing at Ratings due to some scenarios like unsupported extra services or incompatible extra services combined for a shipment. | [optional] 
**pending** | **float** | The number of shipments which are pending and in-queue to be processed. | [optional] 

## Example

```python
from shipping.models.rating_count_status_err import RatingCountStatusERR

# TODO update the JSON string below
json = "{}"
# create an instance of RatingCountStatusERR from a JSON string
rating_count_status_err_instance = RatingCountStatusERR.from_json(json)
# print the JSON string representation of the object
print(RatingCountStatusERR.to_json())

# convert the object into a dict
rating_count_status_err_dict = rating_count_status_err_instance.to_dict()
# create an instance of RatingCountStatusERR from a dict
rating_count_status_err_from_dict = RatingCountStatusERR.from_dict(rating_count_status_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


