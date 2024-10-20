# ShipmentInternationalParcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** |  | 
**length** | **float** |  | 
**width** | **float** |  | 
**dim_unit** | **str** |  | 
**weight_unit** | **str** |  | 
**weight** | **float** |  | 

## Example

```python
from shipping.models.shipment_international_parcel import ShipmentInternationalParcel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentInternationalParcel from a JSON string
shipment_international_parcel_instance = ShipmentInternationalParcel.from_json(json)
# print the JSON string representation of the object
print(ShipmentInternationalParcel.to_json())

# convert the object into a dict
shipment_international_parcel_dict = shipment_international_parcel_instance.to_dict()
# create an instance of ShipmentInternationalParcel from a dict
shipment_international_parcel_from_dict = ShipmentInternationalParcel.from_dict(shipment_international_parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


