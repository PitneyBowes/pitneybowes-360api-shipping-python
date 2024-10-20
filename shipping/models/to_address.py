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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ToAddress(BaseModel):
    """
    The complete address of the Recipient or Department (in case if the address is not pointed to any individual recipient).
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the Recipient. <br /> `Max length = 40`")
    address_line1: StrictStr = Field(description="The addressLine1 contains the Flat number, Building or Apartment Name/number (if any) or company name (if not residential) of the Recipient. <br /> `Max length = 40`", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="The addressLine2 contains the Area or Street Name. This is an optional field. <br /> `Max length = 40`", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="The addressLine3 contains other details for easy reach, e.g. Landmark. This is an optional field. <br /> `Max length = 40`", alias="addressLine3")
    city_town: StrictStr = Field(description="The name of the city or town the Recipient belongs to.", alias="cityTown")
    state_province: StrictStr = Field(description="The name of the State or Province the Sender belongs to. It is the `2-letter` State or Province Code for US or Canadian address(es). <br /> Below is the hyperlink for CA country that will navigate to its Province/State Codes page. Similarly, respective country users can check for their country- State/Province codes. <br /> Please switch to the `Search` tab, select `Country codes` radio button, enter the required country name or country code, and then click `SEARCH` button . <br /> `Max length = 2`", alias="stateProvince")
    postal_code: StrictStr = Field(description="The Postal Code or ZIP Code of the address.<br /> For US addresses, use either the `5-digit` or `9-digit` ZIP Code in one of the following formats: '12345' or '12345-6789'. <br /> While for CA addresses, use a `six-character` alphanumeric string Postal Code in this format: 'A1A 1A1'. ERR supports only US addresses.<br /> *NOTE: USPS supports only US location.*", alias="postalCode")
    country_code: StrictStr = Field(description="The country in which the recipient's address is located. The value will be the two-character ISO Code of the country from the ISO country list. <br /> Use ISO 3166-1 Alpha-2 standard values. For best results this should be included, especially if the country name does not appear in any of the unparsedAddressLines. <br /> Below is the hyperlink, please select `Country codes` and then click `SEARCH` button.  <br /> *NOTE: USPS supports only US location.*", alias="countryCode")
    company: Optional[StrictStr] = Field(default=None, description="The name of the company, in case if the Recipient address is not residential.")
    phone: Optional[StrictStr] = Field(default=None, description="This is recipient's phone number. Enter the digits with or without spaces or hyphens. <br /> `Max length = 15`.")
    email: Optional[StrictStr] = Field(default=None, description="This must be recipients's valid email. <br /> `Max length = 50` ")
    residential: Optional[StrictBool] = Field(default=None, description="The specified address can be Residential or Official. In case if the address is Residential, the boolean value will be 'true', else it will take 'false'.")
    __properties: ClassVar[List[str]] = ["name", "addressLine1", "addressLine2", "addressLine3", "cityTown", "stateProvince", "postalCode", "countryCode", "company", "phone", "email", "residential"]

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
        """Create an instance of ToAddress from a JSON string"""
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
        """Create an instance of ToAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "cityTown": obj.get("cityTown"),
            "stateProvince": obj.get("stateProvince"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "company": obj.get("company"),
            "phone": obj.get("phone"),
            "email": obj.get("email"),
            "residential": obj.get("residential")
        })
        return _obj


