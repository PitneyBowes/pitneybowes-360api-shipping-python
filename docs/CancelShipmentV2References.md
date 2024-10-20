# CancelShipmentV2References

Contains key value map for passing references which is printed on Shipping Label. <br />For example Department Name, Invoice No., PO No., Package description, Order No./ Purchase Order No., Carrier note, Cost Account No., Transportation No., etc. . Max references allowed here is 2, and max length of each Reference field is 35. [IN/OUT].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_reference1** | **str** | Additional Reference is hardly used, but sender can mention anything as per requirement, just for Recipient&#39;s information. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**additional_reference2** | **str** | Any tags or information that to be shown to Recipient, can be mentioned by Sender, which is not indicated on AdditionalReference1 field, e.g. PO No, Order No. etc.&lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 

## Example

```python
from shipping.models.cancel_shipment_v2_references import CancelShipmentV2References

# TODO update the JSON string below
json = "{}"
# create an instance of CancelShipmentV2References from a JSON string
cancel_shipment_v2_references_instance = CancelShipmentV2References.from_json(json)
# print the JSON string representation of the object
print(CancelShipmentV2References.to_json())

# convert the object into a dict
cancel_shipment_v2_references_dict = cancel_shipment_v2_references_instance.to_dict()
# create an instance of CancelShipmentV2References from a dict
cancel_shipment_v2_references_from_dict = CancelShipmentV2References.from_dict(cancel_shipment_v2_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


