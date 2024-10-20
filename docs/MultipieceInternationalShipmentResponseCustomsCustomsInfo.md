# MultipieceInternationalShipmentResponseCustomsCustomsInfo

This is additional customs information required along with item details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_for_export** | **str** | The reason the commodity is being exported. | 
**customs_declared_value** | **float** | Item value in mentioned currencyCode | 
**currency_code** | **str** | The currency used for declared value. Use three uppercase letters, per ISO 4217 | 
**eelpfc** | **str** | A number provided by the Automated Export System (AES). This is required if the item is valued at more than $2,500 USD per Schedule B export codes. | [optional] 
**certificate_number** | **str** | The certificate number associated with the commodity. | [optional] 
**comments** | **str** | Free-form comments regarding the exported shipment. | [optional] 
**from_customs_reference** | **str** | Free-form reference information provided by the requestor of the shipment. Depending on the carrier this information may or may not be rendered on the customs documents. | [optional] 
**importer_customs_reference** | **str** | A reference number used by the importer, such as a VAT number, PO number, or insured number. | [optional] 
**invoice_number** | **str** | The commercial invoice number assigned by the exporter. | [optional] 
**license_number** | **str** | The export license number associated with the commodity. | [optional] 
**sdr_value** | **float** | When an international parcel is insured, the insured value must be expressed in Special Drawing Rights values. | [optional] 

## Example

```python
from shipping.models.multipiece_international_shipment_response_customs_customs_info import MultipieceInternationalShipmentResponseCustomsCustomsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MultipieceInternationalShipmentResponseCustomsCustomsInfo from a JSON string
multipiece_international_shipment_response_customs_customs_info_instance = MultipieceInternationalShipmentResponseCustomsCustomsInfo.from_json(json)
# print the JSON string representation of the object
print(MultipieceInternationalShipmentResponseCustomsCustomsInfo.to_json())

# convert the object into a dict
multipiece_international_shipment_response_customs_customs_info_dict = multipiece_international_shipment_response_customs_customs_info_instance.to_dict()
# create an instance of MultipieceInternationalShipmentResponseCustomsCustomsInfo from a dict
multipiece_international_shipment_response_customs_customs_info_from_dict = MultipieceInternationalShipmentResponseCustomsCustomsInfo.from_dict(multipiece_international_shipment_response_customs_customs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


