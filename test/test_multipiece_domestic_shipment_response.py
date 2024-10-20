# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.multipiece_domestic_shipment_response import MultipieceDomesticShipmentResponse

class TestMultipieceDomesticShipmentResponse(unittest.TestCase):
    """MultipieceDomesticShipmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultipieceDomesticShipmentResponse:
        """Test MultipieceDomesticShipmentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultipieceDomesticShipmentResponse`
        """
        model = MultipieceDomesticShipmentResponse()
        if include_optional:
            return MultipieceDomesticShipmentResponse(
                correlation_id = '00da5e928af44bcc9e5c092163e036f9',
                label_layout = [
                    shipping.models.multipiece_domestic_shipment_response_label_layout_inner.MultipieceDomesticShipmentResponse_labelLayout_inner(
                        content_type = 'URL', 
                        contents = 'https://225934331380-sending-service-qa.s3-fips.us-east-1.amazonaws.com/temp-labels/UPS2200619919802570P0.pdf', 
                        file_format = 'PDF', 
                        size = 'DOC_8X11', 
                        type = 'SHIPPING_LABEL', )
                    ],
                from_address = shipping.models.multipiece_domestic_shipment_request_from_address.MultipieceDomesticShipmentRequest_fromAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'Stamford', 
                    country_code = 'US', 
                    name = 'Paul Wright', 
                    phone = '203-555-1213', 
                    postal_code = '06905', 
                    state_province = 'CT', ),
                multi_piece_rates = [
                    shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner.MultipieceDomesticShipmentResponse_multiPieceRates_inner(
                        total_carrier_charge = 217.11, 
                        carrier = 'UPS', 
                        currency_code = 'USD', 
                        rate_type_id = 'commercial', 
                        service_id = 'NDA', 
                        service_name = 'NDA', 
                        multi_piece_parcels = [
                            shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner.MultipieceDomesticShipmentResponse_multiPieceRates_inner_multiPieceParcels_inner(
                                parcel_type = 'PKG', 
                                parcel = shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_parcel.MultipieceDomesticShipmentResponse_multiPieceRates_inner_multiPieceParcels_inner_parcel(
                                    length = 10, 
                                    height = 10, 
                                    width = 10, 
                                    dim_unit = 'IN', 
                                    weight_unit = 'OZ', 
                                    weight = 10, ), 
                                parcel_rate = shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_parcel_rate.MultipieceDomesticShipmentResponse_multiPieceRates_inner_multiPieceParcels_inner_parcelRate(
                                    base_charge = 88.67, 
                                    surcharges = [
                                        shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_multi_piece_parcels_inner_parcel_rate_surcharges_inner.MultipieceDomesticShipmentResponse_multiPieceRates_inner_multiPieceParcels_inner_parcelRate_surcharges_inner(
                                            fee = 15.33, 
                                            name = 'FUEL', )
                                        ], ), 
                                parcel_tracking_number = 'UPS2200619919802570P0', )
                            ], 
                        surcharges = [
                            shipping.models.multipiece_domestic_shipment_response_multi_piece_rates_inner_surcharges_inner.MultipieceDomesticShipmentResponse_multiPieceRates_inner_surcharges_inner(
                                fee = 11.3, 
                                name = 'RESIDENTIAL', )
                            ], )
                    ],
                parcel_tracking_number = 'UPS2200619919802570P0',
                shipment_id = 'UPS2200619919802570',
                shipment_options = shipping.models.multipiece_domestic_shipment_request_shipment_options.MultipieceDomesticShipmentRequest_shipmentOptions(
                    print_custom_message = 'custom message', ),
                to_address = shipping.models.multipiece_domestic_shipment_request_to_address.MultipieceDomesticShipmentRequest_toAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'Stamford', 
                    country_code = 'US', 
                    name = 'Paul Wright', 
                    phone = '203-555-1213', 
                    postal_code = '06905', 
                    state_province = 'CT', )
            )
        else:
            return MultipieceDomesticShipmentResponse(
        )
        """

    def testMultipieceDomesticShipmentResponse(self):
        """Test MultipieceDomesticShipmentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
