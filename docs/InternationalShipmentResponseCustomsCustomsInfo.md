# InternationalShipmentResponseCustomsCustomsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eelpfc** | **str** | A number provided by the Automated Export System (AES). This is required if the item is valued at more than $2,500 USD per Schedule B export codes. | [optional] 
**certificate_number** | **str** | The certificate number associated with the commodity. | [optional] 
**comments** | **str** | Free-form comments regarding the exported shipment. | [optional] 
**currency_code** | **str** | The currency used for declared value. Use three uppercase letters, per ISO 4217. | [optional] 
**from_customs_reference** | **str** | Free-form reference information provided by the requestor of the shipment. Depending on the carrier this information may or may not be rendered on the customs documents. | [optional] 
**importer_customs_reference** | **str** | A reference number used by the importer, such as a VAT number, PO number, or insured number. | [optional] 
**invoice_number** | **str** | The commercial invoice number assigned by the exporter. It is rquired for DHL Express. | [optional] 
**license_number** | **str** | The export license number associated with the commodity. | [optional] 
**reason_for_export** | **str** | The reason the commodity is being exported. | [optional] 
**sdr_value** | **float** | When an international parcel is insured, the insured value must be expressed in Special Drawing Rights values. | [optional] 
**terms_of_sale** | **str** | Three-digit codes describing Terms of sale required for DHL Express shipments. Terms of sale is some sort of agreement between a buyer and seller which serves the purpose of creating uniform expectations between them. Possible values are- CFR (description- Cost and Freight), CIF (description- Cost, Insurance and Freight), CIP (description- Carriage and Insurance Paid To), DAF (description- Delivered at Frontier), DAP (description- Delivered At Place), DAT (description- Delivered At Terminal), DDP (description- Delivered Duty Paid), DDU (description- Delivered Duty Unpaid), DEQ (description- Delivery ex Quay), DES (description- Delivered ex Ship), DPU (description- Delivered At Place Unloaded), EXW (description- Ex Works), FAS (description- FAS Free Alongside Ship), FCA (description- Free Carrier), FOB (description- FOB Free On Board) | [optional] 
**recipient_tax_type** | **str** | The tax type to choose for recipient. | [optional] 
**recipient_tax_id** | **str** | The respective taxID for the taxType chosen | [optional] 
**sender_tax_type** | **str** | The tax type to choose for recipient. | [optional] 
**sender_tax_id** | **str** | The respective taxID for the taxType chosen | [optional] 

## Example

```python
from shipping.models.international_shipment_response_customs_customs_info import InternationalShipmentResponseCustomsCustomsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalShipmentResponseCustomsCustomsInfo from a JSON string
international_shipment_response_customs_customs_info_instance = InternationalShipmentResponseCustomsCustomsInfo.from_json(json)
# print the JSON string representation of the object
print(InternationalShipmentResponseCustomsCustomsInfo.to_json())

# convert the object into a dict
international_shipment_response_customs_customs_info_dict = international_shipment_response_customs_customs_info_instance.to_dict()
# create an instance of InternationalShipmentResponseCustomsCustomsInfo from a dict
international_shipment_response_customs_customs_info_from_dict = InternationalShipmentResponseCustomsCustomsInfo.from_dict(international_shipment_response_customs_customs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


