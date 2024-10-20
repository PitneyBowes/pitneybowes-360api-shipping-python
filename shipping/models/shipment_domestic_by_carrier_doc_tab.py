# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shipping.models.doc_tab_item import DocTabItem
from typing import Optional, Set
from typing_extensions import Self

class ShipmentDomesticByCarrierDocTab(BaseModel):
    """
    This option is used to provide additional information into the label's additional space
    """ # noqa: E501
    template_name: Optional[StrictStr] = Field(default=None, description="This is an optional field and will be used when the client has multiple doctab options.", alias="templateName")
    to_address_name: Optional[DocTabItem] = Field(default=None, alias="toAddressName")
    parcel_tracking_number: Optional[DocTabItem] = Field(default=None, alias="parcelTrackingNumber")
    carrier: Optional[DocTabItem] = None
    service_id: Optional[DocTabItem] = Field(default=None, alias="serviceId")
    date_of_shipment: Optional[DocTabItem] = Field(default=None, alias="dateOfShipment")
    piece_number: Optional[DocTabItem] = Field(default=None, alias="pieceNumber")
    package_total_carrier_charge: Optional[DocTabItem] = Field(default=None, alias="packageTotalCarrierCharge")
    total_carrier_charge: Optional[DocTabItem] = Field(default=None, alias="totalCarrierCharge")
    package_weight: Optional[DocTabItem] = Field(default=None, alias="packageWeight")
    total_weight: Optional[DocTabItem] = Field(default=None, alias="totalWeight")
    custom_field1: Optional[DocTabItem] = Field(default=None, alias="customField1")
    custom_field2: Optional[DocTabItem] = Field(default=None, alias="customField2")
    custom_field3: Optional[DocTabItem] = Field(default=None, alias="customField3")
    custom_field4: Optional[DocTabItem] = Field(default=None, alias="customField4")
    __properties: ClassVar[List[str]] = ["templateName", "toAddressName", "parcelTrackingNumber", "carrier", "serviceId", "dateOfShipment", "pieceNumber", "packageTotalCarrierCharge", "totalCarrierCharge", "packageWeight", "totalWeight", "customField1", "customField2", "customField3", "customField4"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ShipmentDomesticByCarrierDocTab from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of to_address_name
        if self.to_address_name:
            _dict['toAddressName'] = self.to_address_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parcel_tracking_number
        if self.parcel_tracking_number:
            _dict['parcelTrackingNumber'] = self.parcel_tracking_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of carrier
        if self.carrier:
            _dict['carrier'] = self.carrier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_id
        if self.service_id:
            _dict['serviceId'] = self.service_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of date_of_shipment
        if self.date_of_shipment:
            _dict['dateOfShipment'] = self.date_of_shipment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of piece_number
        if self.piece_number:
            _dict['pieceNumber'] = self.piece_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package_total_carrier_charge
        if self.package_total_carrier_charge:
            _dict['packageTotalCarrierCharge'] = self.package_total_carrier_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_carrier_charge
        if self.total_carrier_charge:
            _dict['totalCarrierCharge'] = self.total_carrier_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package_weight
        if self.package_weight:
            _dict['packageWeight'] = self.package_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_weight
        if self.total_weight:
            _dict['totalWeight'] = self.total_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field1
        if self.custom_field1:
            _dict['customField1'] = self.custom_field1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field2
        if self.custom_field2:
            _dict['customField2'] = self.custom_field2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field3
        if self.custom_field3:
            _dict['customField3'] = self.custom_field3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field4
        if self.custom_field4:
            _dict['customField4'] = self.custom_field4.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipmentDomesticByCarrierDocTab from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templateName": obj.get("templateName"),
            "toAddressName": DocTabItem.from_dict(obj["toAddressName"]) if obj.get("toAddressName") is not None else None,
            "parcelTrackingNumber": DocTabItem.from_dict(obj["parcelTrackingNumber"]) if obj.get("parcelTrackingNumber") is not None else None,
            "carrier": DocTabItem.from_dict(obj["carrier"]) if obj.get("carrier") is not None else None,
            "serviceId": DocTabItem.from_dict(obj["serviceId"]) if obj.get("serviceId") is not None else None,
            "dateOfShipment": DocTabItem.from_dict(obj["dateOfShipment"]) if obj.get("dateOfShipment") is not None else None,
            "pieceNumber": DocTabItem.from_dict(obj["pieceNumber"]) if obj.get("pieceNumber") is not None else None,
            "packageTotalCarrierCharge": DocTabItem.from_dict(obj["packageTotalCarrierCharge"]) if obj.get("packageTotalCarrierCharge") is not None else None,
            "totalCarrierCharge": DocTabItem.from_dict(obj["totalCarrierCharge"]) if obj.get("totalCarrierCharge") is not None else None,
            "packageWeight": DocTabItem.from_dict(obj["packageWeight"]) if obj.get("packageWeight") is not None else None,
            "totalWeight": DocTabItem.from_dict(obj["totalWeight"]) if obj.get("totalWeight") is not None else None,
            "customField1": DocTabItem.from_dict(obj["customField1"]) if obj.get("customField1") is not None else None,
            "customField2": DocTabItem.from_dict(obj["customField2"]) if obj.get("customField2") is not None else None,
            "customField3": DocTabItem.from_dict(obj["customField3"]) if obj.get("customField3") is not None else None,
            "customField4": DocTabItem.from_dict(obj["customField4"]) if obj.get("customField4") is not None else None
        })
        return _obj


