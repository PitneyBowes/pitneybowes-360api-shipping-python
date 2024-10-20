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
from shipping.models.print_document_request_reference import PrintDocumentRequestReference
from typing import Optional, Set
from typing_extensions import Self

class PrintDocumentRequest(BaseModel):
    """
    PrintDocumentRequest
    """ # noqa: E501
    printer_alias_name: StrictStr = Field(description="Name of the Printer connected (directly or via network) to a Computer. `Max length = 30`", alias="printerAliasName")
    data: StrictStr = Field(description="Content/Identifier of document e.g. DOCUMENT_REFERECE_ID. Actual document name e.g. abc.pdf. [IN] i.e base64 string, URL, file path")
    data_type: StrictStr = Field(description="Data Type of the document e.g. DOCUMENT_REFERENCE. [IN/OUT]", alias="dataType")
    document_type: StrictStr = Field(description="The format of the document file the print takes.", alias="documentType")
    form_name: StrictStr = Field(description="The name of the Document Form.", alias="formName")
    orientation: Optional[StrictStr] = Field(default=None, description="The orientation of the document layout: Portrait or Landscape.")
    reference: Optional[PrintDocumentRequestReference] = None
    __properties: ClassVar[List[str]] = ["printerAliasName", "data", "dataType", "documentType", "formName", "orientation", "reference"]

    @field_validator('data')
    def data_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PDF', 'URL']):
            raise ValueError("must be one of enum values ('PDF', 'URL')")
        return value

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BASE64', 'URL']):
            raise ValueError("must be one of enum values ('BASE64', 'URL')")
        return value

    @field_validator('document_type')
    def document_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ZPL2', 'PDF']):
            raise ValueError("must be one of enum values ('ZPL2', 'PDF')")
        return value

    @field_validator('form_name')
    def form_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['8x11', '4x6', '2x1', 'ENV10', 'ENV9', 'A1']):
            raise ValueError("must be one of enum values ('8x11', '4x6', '2x1', 'ENV10', 'ENV9', 'A1')")
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
        """Create an instance of PrintDocumentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reference
        if self.reference:
            _dict['reference'] = self.reference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintDocumentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "printerAliasName": obj.get("printerAliasName"),
            "data": obj.get("data"),
            "dataType": obj.get("dataType"),
            "documentType": obj.get("documentType"),
            "formName": obj.get("formName"),
            "orientation": obj.get("orientation"),
            "reference": PrintDocumentRequestReference.from_dict(obj["reference"]) if obj.get("reference") is not None else None
        })
        return _obj


