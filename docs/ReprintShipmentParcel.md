# ReprintShipmentParcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height is a part of Dimension objet where it helps determine a parcel’s girth. | 
**length** | **float** | Length is a part of Dimension objet having highest numeric value out of three required parameters (length, width, and height) of Dimension. It helps determine a parcel’s girth. | 
**width** | **float** | Width is a part of Dimension object having lowest numeric value out of three required parameters of dimension (length, width, and height). This helps determine a parcel’s girth. | 
**dim_unit** | **str** | DimUnit is a standard for measuring the physical quantities of specified dimension parameters. | 
**weight_unit** | **str** | WeightUnit is a standard for measuring the physical quantities of specified weight. &lt;br&gt; The valid values are:  &lt;br&gt;- OZ: Ounces &lt;br&gt;- GM: Grams &lt;br&gt;- LB: Pounds &lt;br&gt;- KG: Kilograms For USPS shipments, set this to OZ. | 
**weight** | **float** | Weight is the measure of how heavy an object is. | 

## Example

```python
from shipping.models.reprint_shipment_parcel import ReprintShipmentParcel

# TODO update the JSON string below
json = "{}"
# create an instance of ReprintShipmentParcel from a JSON string
reprint_shipment_parcel_instance = ReprintShipmentParcel.from_json(json)
# print the JSON string representation of the object
print(ReprintShipmentParcel.to_json())

# convert the object into a dict
reprint_shipment_parcel_dict = reprint_shipment_parcel_instance.to_dict()
# create an instance of ReprintShipmentParcel from a dict
reprint_shipment_parcel_from_dict = ReprintShipmentParcel.from_dict(reprint_shipment_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


