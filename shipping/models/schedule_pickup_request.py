# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from shipping.models.schedule_pickup_dhlexp_request import SchedulePickupDHLEXPRequest
from shipping.models.schedule_pickup_fedex_request import SchedulePickupFedexRequest
from shipping.models.schedule_pickup_ups_request import SchedulePickupUPSRequest
from shipping.models.schedule_pickup_usps_request import SchedulePickupUSPSRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SCHEDULEPICKUPREQUEST_ONE_OF_SCHEMAS = ["SchedulePickupDHLEXPRequest", "SchedulePickupFedexRequest", "SchedulePickupUPSRequest", "SchedulePickupUSPSRequest"]

class SchedulePickupRequest(BaseModel):
    """
    SchedulePickupRequest
    """
    # data type: SchedulePickupDHLEXPRequest
    oneof_schema_1_validator: Optional[SchedulePickupDHLEXPRequest] = None
    # data type: SchedulePickupUSPSRequest
    oneof_schema_2_validator: Optional[SchedulePickupUSPSRequest] = None
    # data type: SchedulePickupUPSRequest
    oneof_schema_3_validator: Optional[SchedulePickupUPSRequest] = None
    # data type: SchedulePickupFedexRequest
    oneof_schema_4_validator: Optional[SchedulePickupFedexRequest] = None
    actual_instance: Optional[Union[SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest]] = None
    one_of_schemas: Set[str] = { "SchedulePickupDHLEXPRequest", "SchedulePickupFedexRequest", "SchedulePickupUPSRequest", "SchedulePickupUSPSRequest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SchedulePickupRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: SchedulePickupDHLEXPRequest
        if not isinstance(v, SchedulePickupDHLEXPRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulePickupDHLEXPRequest`")
        else:
            match += 1
        # validate data type: SchedulePickupUSPSRequest
        if not isinstance(v, SchedulePickupUSPSRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulePickupUSPSRequest`")
        else:
            match += 1
        # validate data type: SchedulePickupUPSRequest
        if not isinstance(v, SchedulePickupUPSRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulePickupUPSRequest`")
        else:
            match += 1
        # validate data type: SchedulePickupFedexRequest
        if not isinstance(v, SchedulePickupFedexRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulePickupFedexRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SchedulePickupRequest with oneOf schemas: SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SchedulePickupRequest with oneOf schemas: SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into SchedulePickupDHLEXPRequest
        try:
            instance.actual_instance = SchedulePickupDHLEXPRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SchedulePickupUSPSRequest
        try:
            instance.actual_instance = SchedulePickupUSPSRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SchedulePickupUPSRequest
        try:
            instance.actual_instance = SchedulePickupUPSRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SchedulePickupFedexRequest
        try:
            instance.actual_instance = SchedulePickupFedexRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SchedulePickupRequest with oneOf schemas: SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SchedulePickupRequest with oneOf schemas: SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], SchedulePickupDHLEXPRequest, SchedulePickupFedexRequest, SchedulePickupUPSRequest, SchedulePickupUSPSRequest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


