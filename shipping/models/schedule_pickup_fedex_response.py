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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from shipping.models.get_all_pickups_data_inner_pickup_options import GetAllPickupsDataInnerPickupOptions
from shipping.models.schedule_pickup_dhlexp_response_pickup_address import SchedulePickupDHLEXPResponsePickupAddress
from shipping.models.schedule_pickup_usps_response_pickup_summary_inner import SchedulePickupUSPSResponsePickupSummaryInner
from typing import Optional, Set
from typing_extensions import Self

class SchedulePickupFedexResponse(BaseModel):
    """
    SchedulePickupFedexResponse
    """ # noqa: E501
    package_location: Optional[StrictStr] = Field(default=None, description="It specifies the location from where packages would be collected.", alias="packageLocation")
    pickup_confirmation_number: Optional[StrictStr] = Field(default=None, description="It displays the unique confirmation number of the pickup", alias="pickupConfirmationNumber")
    pickup_id: Optional[StrictStr] = Field(default=None, description="It displays the unique pickup Id which can be further used to get scheduled PDF and cancel pdf if required.", alias="pickupId")
    carrier: Optional[StrictStr] = Field(default=None, description="It dispays the carrier")
    carrier_account_id: Optional[StrictStr] = Field(default=None, description="It displays the carrier acount id which is used to create the shipment", alias="carrierAccountId")
    pickup_address: Optional[SchedulePickupDHLEXPResponsePickupAddress] = Field(default=None, alias="pickupAddress")
    shipment_ids: Optional[List[StrictStr]] = Field(default=None, description="It indicates the shipmentIds for which pickup is scheduled.", alias="shipmentIds")
    pickup_summary: Optional[List[SchedulePickupUSPSResponsePickupSummaryInner]] = Field(default=None, description="It displays the package details provided in the request.", alias="pickupSummary")
    additionalnotes: Optional[StrictStr] = Field(default=None, description="It displays additional comments or remarks provided in the request, it would be printed on the scheduled pickup document")
    reference: Optional[StrictStr] = Field(default=None, description="It displays any reference information provided in the request.")
    pickup_date_time: Optional[StrictStr] = Field(default=None, description="It displays the scheduled pickup date and time (in UTC)", alias="pickupDateTime")
    pickup_total_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="It displays the total package weight.", alias="pickupTotalWeight")
    pickup_total_weight_unit: Optional[StrictStr] = Field(default=None, description="It displays the weight unit.", alias="pickupTotalWeightUnit")
    pickup_options: Optional[GetAllPickupsDataInnerPickupOptions] = Field(default=None, alias="pickupOptions")
    __properties: ClassVar[List[str]] = ["packageLocation", "pickupConfirmationNumber", "pickupId", "carrier", "carrierAccountId", "pickupAddress", "shipmentIds", "pickupSummary", "additionalnotes", "reference", "pickupDateTime", "pickupTotalWeight", "pickupTotalWeightUnit", "pickupOptions"]

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
        """Create an instance of SchedulePickupFedexResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pickup_address
        if self.pickup_address:
            _dict['pickupAddress'] = self.pickup_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pickup_summary (list)
        _items = []
        if self.pickup_summary:
            for _item in self.pickup_summary:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pickupSummary'] = _items
        # override the default output from pydantic by calling `to_dict()` of pickup_options
        if self.pickup_options:
            _dict['pickupOptions'] = self.pickup_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchedulePickupFedexResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "packageLocation": obj.get("packageLocation"),
            "pickupConfirmationNumber": obj.get("pickupConfirmationNumber"),
            "pickupId": obj.get("pickupId"),
            "carrier": obj.get("carrier"),
            "carrierAccountId": obj.get("carrierAccountId"),
            "pickupAddress": SchedulePickupDHLEXPResponsePickupAddress.from_dict(obj["pickupAddress"]) if obj.get("pickupAddress") is not None else None,
            "shipmentIds": obj.get("shipmentIds"),
            "pickupSummary": [SchedulePickupUSPSResponsePickupSummaryInner.from_dict(_item) for _item in obj["pickupSummary"]] if obj.get("pickupSummary") is not None else None,
            "additionalnotes": obj.get("additionalnotes"),
            "reference": obj.get("reference"),
            "pickupDateTime": obj.get("pickupDateTime"),
            "pickupTotalWeight": obj.get("pickupTotalWeight"),
            "pickupTotalWeightUnit": obj.get("pickupTotalWeightUnit"),
            "pickupOptions": GetAllPickupsDataInnerPickupOptions.from_dict(obj["pickupOptions"]) if obj.get("pickupOptions") is not None else None
        })
        return _obj


