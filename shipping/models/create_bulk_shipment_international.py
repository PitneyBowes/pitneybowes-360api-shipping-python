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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from shipping.models.shipment_international import ShipmentInternational
from shipping.models.special_service import SpecialService
from typing import Optional, Set
from typing_extensions import Self

class CreateBulkShipmentInternational(BaseModel):
    """
    ShipmentBatch information contains the `BatchId`, `Carrier`,`To` and `From` addresses, `Tracking details`, and `Event information` of the Ship Request.
    """ # noqa: E501
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    size: StrictStr = Field(description="This indicates the label size of the Bulk Shipment, e.g., DocSize can be 8' X 11'.")
    type: StrictStr = Field(description="This indicates the type of the Batch Shipment, e.g., Shipping Label.")
    format: Optional[StrictStr] = Field(default=None, description="This defines the type of the shipment which is printed, e.g., Shipping label gets printed in PDF form.")
    name: StrictStr
    carrier_account_id: StrictStr = Field(description="Default `carrierAccountId` to be used for this batch. You can override this value by defining it at shipment level.", alias="carrierAccountId")
    parcel_type: StrictStr = Field(description="Default `parcelType` specific to the carrier, e.g., FRPKG, LGENV, TUBE,PKG to be used for this batch. You can override this value by defining it at shipment level.", alias="parcelType")
    service_id: StrictStr = Field(description="Default abbreviated name `serviceId` of the carrier-specific service to be used for this batch. You can override this value by defining it at shipment level.", alias="serviceId")
    special_services: Optional[List[SpecialService]] = Field(default=None, description="Default `specialServices` to be used for this batch. You can override this value by defining it at shipment level.", alias="specialServices")
    shipments: List[ShipmentInternational]
    __properties: ClassVar[List[str]] = ["groupName", "size", "type", "format", "name", "carrierAccountId", "parcelType", "serviceId", "specialServices", "shipments"]

    @field_validator('size')
    def size_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DOC_8X11']):
            raise ValueError("must be one of enum values ('DOC_8X11')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SHIPPING_LABEL']):
            raise ValueError("must be one of enum values ('SHIPPING_LABEL')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PDF']):
            raise ValueError("must be one of enum values ('PDF')")
        return value

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
        """Create an instance of CreateBulkShipmentInternational from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in special_services (list)
        _items = []
        if self.special_services:
            for _item in self.special_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specialServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipments (list)
        _items = []
        if self.shipments:
            for _item in self.shipments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateBulkShipmentInternational from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupName": obj.get("groupName"),
            "size": obj.get("size"),
            "type": obj.get("type"),
            "format": obj.get("format"),
            "name": obj.get("name"),
            "carrierAccountId": obj.get("carrierAccountId"),
            "parcelType": obj.get("parcelType"),
            "serviceId": obj.get("serviceId"),
            "specialServices": [SpecialService.from_dict(_item) for _item in obj["specialServices"]] if obj.get("specialServices") is not None else None,
            "shipments": [ShipmentInternational.from_dict(_item) for _item in obj["shipments"]] if obj.get("shipments") is not None else None
        })
        return _obj


