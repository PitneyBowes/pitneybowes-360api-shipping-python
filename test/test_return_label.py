# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.return_label import ReturnLabel

class TestReturnLabel(unittest.TestCase):
    """ReturnLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnLabel:
        """Test ReturnLabel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnLabel`
        """
        model = ReturnLabel()
        if include_optional:
            return ReturnLabel(
                size = 'DOC_8X11',
                type = 'SHIPPING_LABEL',
                from_address = shipping.models.return_label_from_address.returnLabel_fromAddress(
                    address_line1 = '27 Watervw Dr', 
                    email = 'watervw@gmail.com', 
                    city_town = 'Stamford', 
                    country_code = 'US', 
                    name = 'Paul Wright', 
                    phone = '203-555-1213', 
                    postal_code = '06905', 
                    state_province = 'CT', ),
                parcel = shipping.models.shipment_domestic_parcel.shipmentDomestic_parcel(
                    height = 1, 
                    length = 2, 
                    width = 1, 
                    dim_unit = 'IN', 
                    weight_unit = 'OZ', 
                    weight = 1, ),
                carrier_account_id = 'asas2223',
                parcel_type = 'PKG',
                parcel_id = 'PKG',
                service_id = 'PM',
                special_services = [
                    shipping.models.return_label_special_services_inner.returnLabel_specialServices_inner(
                        special_service_id = 'PRL', 
                        input_parameters = [
                            shipping.models.return_label_special_services_inner_input_parameters_inner.returnLabel_specialServices_inner_inputParameters_inner(
                                name = 'RETURN_PKG_DESCRIPTION', 
                                value = 'test', )
                            ], )
                    ],
                shipment_options = shipping.models.shipment_options_v2.shipmentOptionsV2(
                    add_to_manifest = True, 
                    print_custom_message = 'Print Message 1', 
                    receipt_option = 'RECEIPT_WITH_INSTRUCTIONS', 
                    print_department = 'department', 
                    print_invoice_number = 'invoicenumber', 
                    print_po_number = 'ponumber', 
                    minimal_address_validation = True, ),
                metadata = [
                    shipping.models.shipment_international_metadata_inner.shipmentInternational_metadata_inner(
                        name = 'costAccountName', 
                        value = 'cost account 123', )
                    ],
                to_address = shipping.models.return_label_to_address.returnLabel_toAddress(
                    address_line1 = '762 Atlantic Ave', 
                    email = 'email@gmail.com', 
                    city_town = 'Rochester', 
                    country_code = 'US', 
                    name = 'Rufous Sirius Canid', 
                    company = 'ABC Company', 
                    phone = '203-555-1213', 
                    postal_code = '14609', 
                    state_province = 'NY', )
            )
        else:
            return ReturnLabel(
        )
        """

    def testReturnLabel(self):
        """Test ReturnLabel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
