# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.create_manifest_request import CreateManifestRequest

class TestCreateManifestRequest(unittest.TestCase):
    """CreateManifestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateManifestRequest:
        """Test CreateManifestRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateManifestRequest`
        """
        model = CreateManifestRequest()
        if include_optional:
            return CreateManifestRequest(
                carrier_account_id = 'abcd12',
                from_address = shipping.models.create_manifest_request_from_address.createManifest_request_fromAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'shelton', 
                    company = '', 
                    country_code = 'US', 
                    email = '', 
                    name = '', 
                    phone = '', 
                    postal_code = '06484', 
                    state_province = 'CT', ),
                submission_date = '2023-05-25'
            )
        else:
            return CreateManifestRequest(
                carrier_account_id = 'abcd12',
                from_address = shipping.models.create_manifest_request_from_address.createManifest_request_fromAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'shelton', 
                    company = '', 
                    country_code = 'US', 
                    email = '', 
                    name = '', 
                    phone = '', 
                    postal_code = '06484', 
                    state_province = 'CT', ),
        )
        """

    def testCreateManifestRequest(self):
        """Test CreateManifestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
