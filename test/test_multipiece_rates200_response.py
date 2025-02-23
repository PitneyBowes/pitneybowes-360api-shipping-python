# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.multipiece_rates200_response import MultipieceRates200Response

class TestMultipieceRates200Response(unittest.TestCase):
    """MultipieceRates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultipieceRates200Response:
        """Test MultipieceRates200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultipieceRates200Response`
        """
        model = MultipieceRates200Response()
        if include_optional:
            return MultipieceRates200Response(
                from_address = shipping.models.multipiece_rates_request_from_address.MultipieceRatesRequest_fromAddress(
                    address_line1 = '27 Waterview Dr', 
                    city_town = 'Shelton', 
                    state_province = 'CT', 
                    postal_code = '06484-4301', 
                    country_code = 'US', 
                    company = 'ABC Company', 
                    name = 'Sasha Sekrotov', 
                    phone = '323 555-1212', 
                    email = 'rs.canid@gmail.com', 
                    residential = True, ),
                to_address = shipping.models.multipiece_rates_request_to_address.MultipieceRatesRequest_toAddress(
                    company = 'Pitney Bowes Inc.', 
                    name = 'sender_fname', 
                    phone = '2032032033', 
                    email = 'sender@email.com', 
                    residential = True, 
                    address_line1 = '27 Waterview Drive', 
                    city_town = 'Shelton', 
                    state_province = 'CT', 
                    postal_code = '06484-4301', 
                    country_code = 'US', ),
                service_id = 'NDA',
                rates = [
                    shipping.models.multipiece_rates_response_rates_inner.MultipieceRatesResponse_rates_inner(
                        total_carrier_charge = 172.68, 
                        carrier = 'UPS', 
                        currency_code = 'USD', 
                        rate_type_id = 'COMMERCIAL', 
                        service_id = 'NDA', 
                        multi_piece_parcels = [
                            shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner.MultipieceRatesResponse_rates_inner_multiPieceParcels_inner(
                                parcel_type = 'PKG', 
                                parcel = shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel.MultipieceRatesResponse_rates_inner_multiPieceParcels_inner_parcel(
                                    length = 10, 
                                    height = 10, 
                                    width = 10, 
                                    dim_unit = 'IN', 
                                    weight_unit = 'OZ', 
                                    weight = 16, ), 
                                parcel_rate = shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate.MultipieceRatesResponse_rates_inner_multiPieceParcels_inner_parcelRate(
                                    base_charge = 145.36, 
                                    delivery_commitment = shipping.models.rate_shop_response_rates_inner_delivery_commitment.rateShopResponse_rates_inner_deliveryCommitment(
                                        additional_details = 'By end of Day', 
                                        estimated_delivery_date_time = '2023-12-01', 
                                        guarantee = 'NONE', 
                                        max_estimated_number_of_days = '3', 
                                        min_estimated_number_of_days = '3', ), 
                                    surcharges = [
                                        shipping.models.multipiece_rates_response_rates_inner_multi_piece_parcels_inner_parcel_rate_surcharges_inner.MultipieceRatesResponse_rates_inner_multiPieceParcels_inner_parcelRate_surcharges_inner(
                                            fee = 23.41, 
                                            name = 'FUEL', )
                                        ], ), )
                            ], 
                        surcharges = [
                            shipping.models.multipiece_rates_response_rates_inner_surcharges_inner.MultipieceRatesResponse_rates_inner_surcharges_inner(
                                fee = 5.65, 
                                name = 'RESIDENTIAL', )
                            ], )
                    ],
                errors = [{code=validation_error, message=error while geting rates for  carrier with carrierAccount eRMnRx4mzPP : }]
            )
        else:
            return MultipieceRates200Response(
        )
        """

    def testMultipieceRates200Response(self):
        """Test MultipieceRates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
