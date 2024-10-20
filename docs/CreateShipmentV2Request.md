# CreateShipmentV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_address** | [**FromAddressV2**](FromAddressV2.md) |  | 
**to_address** | [**ToAddressV2**](ToAddressV2.md) |  | 
**parcel** | [**ParcelV2**](ParcelV2.md) |  | [optional] 
**parcel_type** | **str** | Parcel Type is required for creating a shipment while rating a parcel, which varies as per Carrier selection.&lt;br /&gt; ParcelType can have categories like Package, Envelopes, Paks, Boxes, Tube, etc. &lt;br /&gt; &#x60;Max length &#x3D; 30&#x60;  | 
**rate_shop_by** | **str** | RateShop, which is attached to an Enterprise or Location, is done through three approaches: by Carrier, by RateGroup, and by Ruleset. &lt;br /&gt;  Through Carrier, customers can choose the carriers as per requirement, based on which services, parcel types, and special services can be selected, and RateShop is done. &lt;br /&gt; Through RateGroup, customers can select the RateGroup, which has been divided into two categories: Cheapest (w.r.t. price) and Fastest (w.r.t. delivery hours). &lt;br /&gt; Through Ruleset, customers can define the Condition/rule for selecting carriers and their services, so they do not need to worry for Rate Shopping every time they create Shipment. For example, For a particular location, they can set one definite carrier, or apply RateGroup - Cheapest/Fastest. Similarly, for a particular amount like below $1000 Dollars, they can select a definite carrier service, based on RateGroup. | 
**by_carrier** | [**ByCarrierV2**](ByCarrierV2.md) |  | [optional] 
**shipment_options** | [**ShipmentDomesticByRulesetShipmentOptions**](ShipmentDomesticByRulesetShipmentOptions.md) |  | [optional] 
**doc_tab** | [**ShipmentDomesticByCarrierDocTab**](ShipmentDomesticByCarrierDocTab.md) |  | [optional] 
**delivery_confirmation** | **str** | Indicates the supporting special service or document as an evidence of shipment delivery.  For the delivery confirmation, user can select any of the following special services, but they may vary as per the carrier selection. &lt;br /&gt;   - Signature Required/ Indirect Signature Required : SIG   - Signed Hard Copy: SIGHC   - Delivery confirmation: DEL_CON   - Proof of age required (18 years) Adult Signature Required: ADULT_SIG   - Proof of age required (19 years): ADULT_SIG_19   - No Signature Required: NO_SIG   - Direct Signature Required: DIRECT_SIG   - Chain of Signature: COS       Carrier specific options:   - UPS supports *SIG and ADULT_SIG*.    - FedEx supports *SIG, ADULT_SIG, NO_SIG, and DIRECT_SIG*.   - Purolator supports *ADULT_SIG, NO_SIG, and COS*.   - GoFor supports *SIG*.   - CPC supports *SIG, SIGHC, DEL_CON, ADULT_SIG, ADULT_SIG_19, and NO_SIG*.      | [optional] 
**handling** | **str** | Few shipments need a special handling, and the reason can be fragile items or highly secured shipments. There might be other case scenarios. In a simple term, this field defines shipment handling, which provides users a capability to select handling options. &lt;br /&gt; User can select any of the following handling options (special services), but they may vary as per the carrier selection.   - Hold For Pickup: HOLD   - Saturday Delivery: SAT_DELIVERY   - UPS Premium Care: PREM_CARE   - Direct Delivery Only: DIRECT   - Additional Handling: ADD_HDL       Carrier specific options:   - UPS supports all handling options mentioned above.    - FedEx supports *HOLD, SAT_DELIVERY, and ADD_HDL*.   - Purolator supports *HOLD, SAT_DELIVERY, and ADD_HDL*.     | [optional] 
**insurance** | **str** | Indicates the insurance coverage, which is selected by users while create shipment - rate shopping. User can select below-mentioned special service for insurance:    - Declared Value Surcharge: INS      Carrier specific options:   - UPS, FedEx, Purolator, and CPC support special service *INS*.     | [optional] 
**references** | [**ReferenceV2**](ReferenceV2.md) |  | [optional] 
**metadata** | [**List[ShipmentDomesticByRulesetMetadataInner]**](ShipmentDomesticByRulesetMetadataInner.md) | Additional metadata that needs to be stored for this shipment can be added here.&lt;br /&gt; For now, &#39;Cost Account Name&#39; is supported. | [optional] 
**label_size** | **str** | Defines the label size of the Shipment, that is, the Shipping Label is available in different Doc Size. &lt;br /&gt; &#x60;Max length &#x3D; 10&#x60; | 
**label_type** | **str** | Defines the type of the Shipment. &lt;br /&gt; &#x60;Max length &#x3D; 14&#x60; | 
**label_format** | **str** | Defines the file/format in which the label is printed. &lt;br /&gt; &#x60;Max length &#x3D; 14&#x60; | 
**printer_alias_name** | **str** | Refers to a printer connected (directly or via network) to a computer. &#x60;Max length &#x3D; 60&#x60; | [optional] 
**date_of_shipment** | **date** | The date when shipment is created/shipped. The format of the Date is YYYY-MM-DD. | [optional] 
**delivery_option** | [**ShipmentDomesticByRulesetDeliveryOption**](ShipmentDomesticByRulesetDeliveryOption.md) |  | [optional] 
**by_rate_group** | [**ShipmentDomesticByRateGroupByRateGroup**](ShipmentDomesticByRateGroupByRateGroup.md) |  | [optional] 
**by_rule_set** | [**ShipmentDomesticByRulesetByRuleSet**](ShipmentDomesticByRulesetByRuleSet.md) |  | [optional] 

## Example

```python
from shipping.models.create_shipment_v2_request import CreateShipmentV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipmentV2Request from a JSON string
create_shipment_v2_request_instance = CreateShipmentV2Request.from_json(json)
# print the JSON string representation of the object
print(CreateShipmentV2Request.to_json())

# convert the object into a dict
create_shipment_v2_request_dict = create_shipment_v2_request_instance.to_dict()
# create an instance of CreateShipmentV2Request from a dict
create_shipment_v2_request_from_dict = CreateShipmentV2Request.from_dict(create_shipment_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


