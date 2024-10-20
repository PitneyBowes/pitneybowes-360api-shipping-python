# ReferenceV2

References are tags or information that is printed on Shipping Label based on the customer's requirement. <br /> Reference Fields can have values/indication like department name, invoice no., package description, purchase order no., carrier note, cost account no., transportation no., or PO no., etc. <br /> Each of the reference field can have only one indication/value. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference1** | **str** | Reference 1 can have one of the above-indicated values/information, which is printed on Label, e.g. Cost Account No. (if any) or Invoice Number. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**reference2** | **str** | Reference 2 can have other details as indicated in the example values above. This is also printed on Label, e.g. Package Description . &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**reference3** | **str** | Reference 3 can have the information which were not fulfilled in Ref1 and Ref2, e.g. Order No. or Purchase Order ID. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**reference4** | **str** | Reference 4 can have more information which were not provided in Ref1, Ref2, or Ref3 e.g. Carrier Note. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**po_number** | **str** | The Postal Office Number. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**department** | **str** | The department of the Recipient. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**additional_reference1** | **str** | Additional Reference is hardly used, but sender can mention anything as per requirement, just for Recipient&#39;s information. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 
**additional_reference2** | **str** | Any tags or information that to be shown to Recipient, can be mentioned by Sender, which is not indicated on AdditionalReference1 field, e.g. PO No, Order No. etc.&lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;. | [optional] 

## Example

```python
from shipping.models.reference_v2 import ReferenceV2

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceV2 from a JSON string
reference_v2_instance = ReferenceV2.from_json(json)
# print the JSON string representation of the object
print(ReferenceV2.to_json())

# convert the object into a dict
reference_v2_dict = reference_v2_instance.to_dict()
# create an instance of ReferenceV2 from a dict
reference_v2_from_dict = ReferenceV2.from_dict(reference_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


