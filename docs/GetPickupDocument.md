# GetPickupDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_id** | **str** | It displays the pickup id for which request is made. | [optional] 
**url** | **str** | It displays the url of the PDF generated. | [optional] 

## Example

```python
from shipping.models.get_pickup_document import GetPickupDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickupDocument from a JSON string
get_pickup_document_instance = GetPickupDocument.from_json(json)
# print the JSON string representation of the object
print(GetPickupDocument.to_json())

# convert the object into a dict
get_pickup_document_dict = get_pickup_document_instance.to_dict()
# create an instance of GetPickupDocument from a dict
get_pickup_document_from_dict = GetPickupDocument.from_dict(get_pickup_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


