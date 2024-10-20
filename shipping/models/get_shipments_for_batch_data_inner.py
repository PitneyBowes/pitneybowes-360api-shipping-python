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
from shipping.models.from_address import FromAddress
from shipping.models.get_shipments_for_batch_data_inner_label_layout import GetShipmentsForBatchDataInnerLabelLayout
from shipping.models.get_shipments_for_batch_data_inner_metadata_inner import GetShipmentsForBatchDataInnerMetadataInner
from shipping.models.get_shipments_for_batch_data_inner_special_services_inner import GetShipmentsForBatchDataInnerSpecialServicesInner
from shipping.models.get_shipments_for_batch_data_inner_step_status import GetShipmentsForBatchDataInnerStepStatus
from shipping.models.parcel import Parcel
from shipping.models.shipment_options import ShipmentOptions
from shipping.models.to_address import ToAddress
from typing import Optional, Set
from typing_extensions import Self

class GetShipmentsForBatchDataInner(BaseModel):
    """
    GetShipmentsForBatchDataInner
    """ # noqa: E501
    batch_id: Optional[StrictStr] = Field(default=None, description="This is a system-generated unique identifier assigned to the Batch while it is processed.", alias="batchId")
    carrier_account_id: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with the Carrier account used by client users during shipment process.", alias="carrierAccountId")
    external_id: Optional[StrictStr] = Field(default=None, description="This is a user-defined value provided by users just for their reference. This is for mapping purpose against each shipment.", alias="externalId")
    from_address: Optional[FromAddress] = Field(default=None, alias="fromAddress")
    label_layout: Optional[GetShipmentsForBatchDataInnerLabelLayout] = Field(default=None, alias="labelLayout")
    metadata: Optional[List[GetShipmentsForBatchDataInnerMetadataInner]] = Field(default=None, description="Additional metadata that needs to be stored for this shipment can be added here. For now, `costAccountName` is supported.")
    parcel: Optional[Parcel] = None
    parcel_type: Optional[StrictStr] = Field(default=None, description="Parcel Type is required for creating a shipment while rating a parcel. And it varies as per carrier selection and corresponding services.", alias="parcelType")
    service_id: Optional[StrictStr] = Field(default=None, description="A unique identifier given to the carrier-specific service. User can override this value by defining it at Shipment level.", alias="serviceId")
    shipment_id: Optional[StrictStr] = Field(default=None, description="Shipment ID is a unique identifier for an individual shipment", alias="shipmentId")
    shipment_identifier: Optional[StrictStr] = Field(default=None, description="Unique identifier generated for each shipment, it can be either success or failed.", alias="shipmentIdentifier")
    shipment_options: Optional[ShipmentOptions] = Field(default=None, alias="shipmentOptions")
    special_services: Optional[List[GetShipmentsForBatchDataInnerSpecialServicesInner]] = Field(default=None, description="Special services used to create shipment", alias="specialServices")
    step_status: Optional[GetShipmentsForBatchDataInnerStepStatus] = Field(default=None, alias="stepStatus")
    to_address: Optional[ToAddress] = Field(default=None, alias="toAddress")
    __properties: ClassVar[List[str]] = ["batchId", "carrierAccountId", "externalId", "fromAddress", "labelLayout", "metadata", "parcel", "parcelType", "serviceId", "shipmentId", "shipmentIdentifier", "shipmentOptions", "specialServices", "stepStatus", "toAddress"]

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
        """Create an instance of GetShipmentsForBatchDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label_layout
        if self.label_layout:
            _dict['labelLayout'] = self.label_layout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of parcel
        if self.parcel:
            _dict['parcel'] = self.parcel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_options
        if self.shipment_options:
            _dict['shipmentOptions'] = self.shipment_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in special_services (list)
        _items = []
        if self.special_services:
            for _item in self.special_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specialServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of step_status
        if self.step_status:
            _dict['stepStatus'] = self.step_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_address
        if self.to_address:
            _dict['toAddress'] = self.to_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetShipmentsForBatchDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batchId": obj.get("batchId"),
            "carrierAccountId": obj.get("carrierAccountId"),
            "externalId": obj.get("externalId"),
            "fromAddress": FromAddress.from_dict(obj["fromAddress"]) if obj.get("fromAddress") is not None else None,
            "labelLayout": GetShipmentsForBatchDataInnerLabelLayout.from_dict(obj["labelLayout"]) if obj.get("labelLayout") is not None else None,
            "metadata": [GetShipmentsForBatchDataInnerMetadataInner.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "parcel": Parcel.from_dict(obj["parcel"]) if obj.get("parcel") is not None else None,
            "parcelType": obj.get("parcelType"),
            "serviceId": obj.get("serviceId"),
            "shipmentId": obj.get("shipmentId"),
            "shipmentIdentifier": obj.get("shipmentIdentifier"),
            "shipmentOptions": ShipmentOptions.from_dict(obj["shipmentOptions"]) if obj.get("shipmentOptions") is not None else None,
            "specialServices": [GetShipmentsForBatchDataInnerSpecialServicesInner.from_dict(_item) for _item in obj["specialServices"]] if obj.get("specialServices") is not None else None,
            "stepStatus": GetShipmentsForBatchDataInnerStepStatus.from_dict(obj["stepStatus"]) if obj.get("stepStatus") is not None else None,
            "toAddress": ToAddress.from_dict(obj["toAddress"]) if obj.get("toAddress") is not None else None
        })
        return _obj


