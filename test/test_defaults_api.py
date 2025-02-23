# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.api.defaults_api import DefaultsApi


class TestDefaultsApi(unittest.TestCase):
    """DefaultsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultsApi()

    def tearDown(self) -> None:
        pass

    def test_create_defaults(self) -> None:
        """Test case for create_defaults

        Create Defaults
        """
        pass

    def test_delete_defaults_by_id(self) -> None:
        """Test case for delete_defaults_by_id

        Delete Defaults by ID
        """
        pass

    def test_get_all_defaults(self) -> None:
        """Test case for get_all_defaults

        Get All Defaults
        """
        pass

    def test_get_defaults_by_id(self) -> None:
        """Test case for get_defaults_by_id

        Get Defaults By ID
        """
        pass

    def test_put_defaults_by_id(self) -> None:
        """Test case for put_defaults_by_id

        Update Defaults
        """
        pass


if __name__ == '__main__':
    unittest.main()
