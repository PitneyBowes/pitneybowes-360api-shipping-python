# ImportCountStatus

This will display the status counts for shipments or batch which are submitted via Import .CSV file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of shipments which have been successfully imported. | [optional] 
**failed** | **float** | The number of shipments failed during Import. | [optional] 
**pending** | **float** | The number of shipments which are pending and in-queue to be imported. | [optional] 

## Example

```python
from shipping.models.import_count_status import ImportCountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCountStatus from a JSON string
import_count_status_instance = ImportCountStatus.from_json(json)
# print the JSON string representation of the object
print(ImportCountStatus.to_json())

# convert the object into a dict
import_count_status_dict = import_count_status_instance.to_dict()
# create an instance of ImportCountStatus from a dict
import_count_status_from_dict = ImportCountStatus.from_dict(import_count_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


