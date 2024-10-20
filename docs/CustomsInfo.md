# CustomsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_for_export** | **str** | &gt;-The reason the commodity is being exported. Valid values are: Valid Values : [GIFT COMMERCIAL_SAMPLE MERCHANDISE DOCUMENTS RETURNED_GOODS OTHER SOLD NOT_SOLD] | [optional] 
**currency_code** | **str** | &gt;-The type of currency used for the monetary values in this API request. Use three uppercase letters, per ISO 4217. For example, use USD for US Dollars, CAD for Canadian Dollars, and EUR for Euros. | 
**eelpfc** | **str** | &gt;- A number provided by the Automated Export System (AES). This field is required if the item is valued at more than $2,500 USD per Schedule B export codes. | [optional] 
**certificate_number** | **str** | The certificate number associated with the commodity. | [optional] 
**comments** | **str** | &gt;-Free form comments regarding the exported shipment entered by the shipper. | [optional] 
**from_customs_reference** | **str** | &gt;-Free form reference information provided by the requestor of the shipment. Depending on the carrier this information may or may not be rendered on the customs documents. | [optional] 
**importer_customs_reference** | **str** | &gt;- A reference number used by the importer, such as a VAT number, PO number, or insured number. &#x60;Shipments to the EU&#x60; : Merchants shipping to the European Union (EU) from outside the EU must provide a VAT or IOSS number. Enter the number in this field and specify the reference type in the importerCustomsReferenceType field. | [optional] 
**invoice_number** | **str** | The commercial invoice number assigned by the exporter. It is rquired for DHL Express | [optional] 
**license_number** | **str** | The export license number associated with the commodity. | [optional] 
**declaration_statement** | **str** | This is declaration statement from the Shipper for the items being shipped. | [optional] 
**importer_customs_reference_type** | **str** | &gt;-A reference type used by the importer to determine the type of importerCustomsReference. Valid Values are TAX_CODE, IMPORTER_CODE, VAT_NUMBER, IOSS_NUMBER. | [optional] 
**insured_amount** | **float** | Enter the insurance fee, if applicable. | [optional] 
**insured_number** | **str** | &gt;- If the sender wishes to insure the contents, they complete an insurance receipt and affix the insured numbered label to the package. The insured number label is what this field represents. | [optional] 
**sdr_value** | **float** | &gt;-When an international parcel is insured, the insured value must be expressed in Special Drawing Rights values. E.g. $100 USD &#x3D; 66.87 SDR. | [optional] 
**terms_of_sale** | **str** | Three-digit codes describing Terms of sale required for DHL Express shipments. Terms of sale is some sort of agreement between a buyer and seller which serves the purpose of creating uniform expectations between them. Possible values are- CFR (description- Cost and Freight), CIF (description- Cost, Insurance and Freight), CIP (description- Carriage and Insurance Paid To), DAF (description- Delivered at Frontier), DAP (description- Delivered At Place), DAT (description- Delivered At Terminal), DDP (description- Delivered Duty Paid), DDU (description- Delivered Duty Unpaid), DEQ (description- Delivery ex Quay), DES (description- Delivered ex Ship), DPU (description- Delivered At Place Unloaded), EXW (description- Ex Works), FAS (description- FAS Free Alongside Ship), FCA (description- Free Carrier), FOB (description- FOB Free On Board) | [optional] 
**recipient_tax_type** | **str** | The tax type to choose for recipient. | [optional] 
**recipient_tax_id** | **str** | The respective taxID for the taxType chosen | [optional] 
**sender_tax_type** | **str** | The tax type to choose for recipient. | [optional] 
**sender_tax_id** | **str** | The respective taxID for the taxType chosen | [optional] 

## Example

```python
from shipping.models.customs_info import CustomsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsInfo from a JSON string
customs_info_instance = CustomsInfo.from_json(json)
# print the JSON string representation of the object
print(CustomsInfo.to_json())

# convert the object into a dict
customs_info_dict = customs_info_instance.to_dict()
# create an instance of CustomsInfo from a dict
customs_info_from_dict = CustomsInfo.from_dict(customs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


