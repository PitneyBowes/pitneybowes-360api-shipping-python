# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.get_all_pickups import GetAllPickups

class TestGetAllPickups(unittest.TestCase):
    """GetAllPickups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllPickups:
        """Test GetAllPickups
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllPickups`
        """
        model = GetAllPickups()
        if include_optional:
            return GetAllPickups(
                page_info = shipping.models.get_all_pickups_page_info.getAllPickups_pageInfo(
                    total = 78, 
                    pages = 8, 
                    page = 1, ),
                data = [
                    shipping.models.get_all_pickups_data_inner.getAllPickups_data_inner(
                        package_location = 'NONE', 
                        pickup_confirmation_number = 'CBJ180121002626', 
                        pickup_id = 'DHLEXP10191697701225617', 
                        carrier = 'ups', 
                        carrier_account_id = 'j4pqLKjQ5dn', 
                        pickup_address = shipping.models.schedule_pickup_dhlexp_response_pickup_address.schedulePickupDHLEXPResponse_pickupAddress(
                            name = 'Test', 
                            address_line1 = '27 Waterview Dr', 
                            city_town = 'Shelton', 
                            state_province = 'CT', 
                            postal_code = '06484-4301', 
                            residential = True, 
                            country_code = 'US', 
                            phone = '1234567890', 
                            company = 'PB', 
                            email = 'test@xyz.com', ), 
                        shipment_ids = [
                            'UPS2200491973488991'
                            ], 
                        pickup_summary = [
                            shipping.models.get_all_pickups_data_inner_pickup_summary_inner.getAllPickups_data_inner_pickupSummary_inner(
                                service_id = 'NDA', 
                                package_count = 2, 
                                total_weight = 15, 
                                weight_unit = 'OZ', 
                                parcel_type = 'PKG', 
                                to_address_country_code = 'US', 
                                currency_code = 'USD', )
                            ], 
                        special_instructions = 'test notes', 
                        reference = 'test reference', 
                        pickup_date_time = '2023-11-06T17:05:05Z', 
                        pickup_total_weight = 16, 
                        pickup_total_weight_unit = 'OZ', 
                        pickup_options = shipping.models.get_all_pickups_data_inner_pickup_options.getAllPickups_data_inner_pickupOptions(
                            pickup_start_date_time = '2023-11-06T17:05:05Z', 
                            pickup_end_date_time = '2023-11-06T18:30:00Z', 
                            overweight = 2, 
                            carrier_type = 'Express', ), 
                        pickup_rate = shipping.models.schedule_pickup_ups_response_pickup_rate.schedulePickupUPSResponse_pickupRate(
                            base_charge = 8, 
                            surcharges = [
                                shipping.models.schedule_pickup_ups_response_pickup_rate_surcharges_inner.schedulePickupUPSResponse_pickupRate_surcharges_inner(
                                    name = 'FUEL', 
                                    fee = 1.22, )
                                ], 
                            total_carrier_charge = 9.22, ), )
                    ]
            )
        else:
            return GetAllPickups(
        )
        """

    def testGetAllPickups(self):
        """Test GetAllPickups"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
