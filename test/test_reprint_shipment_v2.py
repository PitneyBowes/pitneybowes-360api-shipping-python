# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.reprint_shipment_v2 import ReprintShipmentV2

class TestReprintShipmentV2(unittest.TestCase):
    """ReprintShipmentV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReprintShipmentV2:
        """Test ReprintShipmentV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReprintShipmentV2`
        """
        model = ReprintShipmentV2()
        if include_optional:
            return ReprintShipmentV2(
                shipment_id = 'PUROLATOR2200626443337314',
                parcel_tracking_number = '329039098457',
                label_layout = [
                    shipping.models.reprint_shipment_v2_label_layout_inner.reprintShipmentV2_labelLayout_inner(
                        content_type = 'BASE64', 
                        contents = 'Xhsafiuis', 
                        file_format = 'ZPL2', 
                        size = 'DOC_4X6', 
                        type = 'SHIPPING_LABEL', )
                    ],
                parcel = shipping.models.parcel_v2.parcelV2(
                    length = 2, 
                    width = 1, 
                    height = 1, 
                    dim_unit = 'IN', 
                    weight_unit = 'OZ', 
                    weight = 2, 
                    package_value = 2, ),
                rate = shipping.models.rate_response_v2.rateResponseV2(
                    base_charge = 16.15, 
                    carrier = 'PUROLATOR', 
                    currency_code = 'CAD', 
                    parcel_type = 'PKG', 
                    service_id = 'GRD', 
                    surcharges = [
                        shipping.models.rate_response_v2_surcharges_inner.rateResponseV2_surcharges_inner(
                            fee = 2.95, 
                            name = 'ResidentialDelivery', )
                        ], 
                    total_carrier_charge = 22.46, 
                    delivery_commitment = shipping.models.rate_response_v2_delivery_commitment.rateResponseV2_deliveryCommitment(
                        estimated_delivery_date_time = '2024-03-25', 
                        max_estimated_number_of_days = '5', 
                        guarantee = 'None', ), ),
                references = shipping.models.cancel_shipment_v2_references.cancelShipmentV2_references(
                    additional_reference1 = '612987641', 
                    additional_reference2 = '989', ),
                print_status = 'submitted'
            )
        else:
            return ReprintShipmentV2(
        )
        """

    def testReprintShipmentV2(self):
        """Test ReprintShipmentV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
