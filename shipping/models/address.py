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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    address_line1: StrictStr = Field(description="The addressLine1 can contain the Flat number, Building or Apartment Name/number (if any) or company name (if not residential).", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="The addressLine2 contains Street address or Landmark (if any).", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="The addressLine3 contains P.O.Box (if any) near the address.", alias="addressLine3")
    city_town: Optional[StrictStr] = Field(default=None, description=" This indicates the city or town in the Address.", alias="cityTown")
    company: Optional[StrictStr] = Field(default=None, description=" This indicates the name of the company.")
    country_code: StrictStr = Field(description="This indicates the two-character ISO code of the country.", alias="countryCode")
    email: Optional[StrictStr] = Field(default=None, description="The email address of the Recipient or Department where the delivery address is pointed to.")
    name: Optional[StrictStr] = Field(default=None, description="The first and last name of the Recipient or Department.")
    phone: Optional[StrictStr] = Field(default=None, description=">-The phone number. Enter the digits with or without spaces or hyphens. When used for Pickups, the maximum is 10 digits.")
    postal_code: StrictStr = Field(description="The postal code or ZIP code of the Address.", alias="postalCode")
    residential: Optional[StrictBool] = Field(default=None, description=">-Indicates whether this is a residential address. Pitney Bowes recommends including this parameter to improve address verification.")
    state_province: StrictStr = Field(description=">-The state or province. For a US or Canadian address, use the 2-letter state or province code.", alias="stateProvince")
    status: Optional[StrictStr] = Field(default=None, description=">- This field applies to the Validate Address and Suggest Addresses APIs. The field indicates whether the submitted address is valid and whether the API made changes to the address. Possible values are: `VALIDATED_CHANGED`: The address is valid, but the API made changes to improve the address. For example, if an address has a valid street number and street name (e.g. “100 Elm”) but is missing the street suffix (e.g. “St”), the API would add the suffix. `VALIDATED_AND_NOT_CHANGED`: The address is valid. The API made no changes.")
    tax_id: Optional[StrictStr] = Field(default=None, description=">-Tax identification number (TIN) or Employer Identification number (EIN) or GST or VAT number or RFC or EORI.", alias="taxId")
    tax_id_type: Optional[StrictStr] = Field(default=None, description=">-Tax identification Type, valid values are EIN or GST or VAT or RFC or EORI.", alias="taxIdType")
    __properties: ClassVar[List[str]] = ["addressLine1", "addressLine2", "addressLine3", "cityTown", "company", "countryCode", "email", "name", "phone", "postalCode", "residential", "stateProvince", "status", "taxId", "taxIdType"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED']):
            raise ValueError("must be one of enum values ('VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED')")
        return value

    @field_validator('tax_id_type')
    def tax_id_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EIN', 'GST', 'VAT', 'EORI']):
            raise ValueError("must be one of enum values ('EIN', 'GST', 'VAT', 'EORI')")
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
        """Create an instance of Address from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "cityTown": obj.get("cityTown"),
            "company": obj.get("company"),
            "countryCode": obj.get("countryCode"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "phone": obj.get("phone"),
            "postalCode": obj.get("postalCode"),
            "residential": obj.get("residential"),
            "stateProvince": obj.get("stateProvince"),
            "status": obj.get("status"),
            "taxId": obj.get("taxId"),
            "taxIdType": obj.get("taxIdType")
        })
        return _obj


