# ReturnLabelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**ReturnLabelFromAddress**](ReturnLabelFromAddress.md) |  | [optional] 
**parcel** | [**ShipmentDomesticParcel**](ShipmentDomesticParcel.md) |  | [optional] 
**correlation_id** | **str** | correction id | [optional] 
**service_id** | **str** | &gt;-A unique identifier given to the carrier-specific service. This is required for creating a shipment, while it is optional for rating a parcel. | [optional] 
**parcel_tracking_number** | **str** | &gt;-A unique identifier parcel tracking number | [optional] 
**shipment_id** | **str** | &gt;-A unique identifier shipment tracking number | [optional] 
**shipment_options** | [**ShipmentOptionsV2**](ShipmentOptionsV2.md) |  | [optional] 
**label_layout** | [**List[ReturnLabelResponseLabelLayoutInner]**](ReturnLabelResponseLabelLayoutInner.md) | labelLayout details | [optional] 
**to_address** | [**ReturnLabelResponseToAddress**](ReturnLabelResponseToAddress.md) |  | [optional] 
**rate** | [**ReturnLabelResponseRate**](ReturnLabelResponseRate.md) |  | [optional] 

## Example

```python
from shipping.models.return_label_response import ReturnLabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnLabelResponse from a JSON string
return_label_response_instance = ReturnLabelResponse.from_json(json)
# print the JSON string representation of the object
print(ReturnLabelResponse.to_json())

# convert the object into a dict
return_label_response_dict = return_label_response_instance.to_dict()
# create an instance of ReturnLabelResponse from a dict
return_label_response_from_dict = ReturnLabelResponse.from_dict(return_label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


