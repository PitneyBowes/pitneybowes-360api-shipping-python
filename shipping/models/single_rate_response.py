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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from shipping.models.single_rate_response_from_address import SingleRateResponseFromAddress
from shipping.models.single_rate_response_parcel import SingleRateResponseParcel
from shipping.models.single_rate_response_rates_inner import SingleRateResponseRatesInner
from shipping.models.single_rate_response_to_address import SingleRateResponseToAddress
from typing import Optional, Set
from typing_extensions import Self

class SingleRateResponse(BaseModel):
    """
    SingleRateResponse
    """ # noqa: E501
    from_address: Optional[SingleRateResponseFromAddress] = Field(default=None, alias="fromAddress")
    parcel: Optional[SingleRateResponseParcel] = None
    rates: Optional[List[SingleRateResponseRatesInner]] = Field(default=None, description="It displays the rate for the required carrier-service and/or special service combinaion")
    to_address: Optional[SingleRateResponseToAddress] = Field(default=None, alias="toAddress")
    __properties: ClassVar[List[str]] = ["fromAddress", "parcel", "rates", "toAddress"]

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
        """Create an instance of SingleRateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of from_address
        if self.from_address:
            _dict['fromAddress'] = self.from_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parcel
        if self.parcel:
            _dict['parcel'] = self.parcel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rates (list)
        _items = []
        if self.rates:
            for _item in self.rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rates'] = _items
        # override the default output from pydantic by calling `to_dict()` of to_address
        if self.to_address:
            _dict['toAddress'] = self.to_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SingleRateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fromAddress": SingleRateResponseFromAddress.from_dict(obj["fromAddress"]) if obj.get("fromAddress") is not None else None,
            "parcel": SingleRateResponseParcel.from_dict(obj["parcel"]) if obj.get("parcel") is not None else None,
            "rates": [SingleRateResponseRatesInner.from_dict(_item) for _item in obj["rates"]] if obj.get("rates") is not None else None,
            "toAddress": SingleRateResponseToAddress.from_dict(obj["toAddress"]) if obj.get("toAddress") is not None else None
        })
        return _obj


