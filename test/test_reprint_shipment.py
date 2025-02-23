# coding: utf-8

"""
    Shipping APIs

    ### Introduction  The Shipping APIs include a variety of operations that allow users to manage and track their shipping requests.   Some of the key API operations available in the Shipping API includes: ### Shipment API  | Operation      | Description | | ----------- | ----------- |  | Get Carriers    | This operation fetches all onboarded carriers. Typically, user will use this service to get list of onboarded carriers and supported properties for those carriers.  |  | Get Countries | This operation fetches list of supported destination countries for a provided carrier and origin country.  |  | Get Services | This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. |  | Get ParcelTypes| This operation fetches ParcelTypes based on carrier, origin and destination country. |  | Get Special Services| This operation fetches Special Services for a given carrier, service, origin and destination country. |  | Get Carrier Accounts| This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.  |  | Rate Shop and Get Single Rate| This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  |  | Create Shipment| This operation creates a new Shipment or Shipment Label. This is for both Domestic and International. | | Get All Shipments| This operation fetches all created Shipments. |  | Get Shipment by Id| Retrieves single shipment using Shipment Id. |  | Reprint Shipment| This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost. |  | Cancel Shipment| This operation cancels previously created shipment. |  

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shipping.models.reprint_shipment import ReprintShipment

class TestReprintShipment(unittest.TestCase):
    """ReprintShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReprintShipment:
        """Test ReprintShipment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReprintShipment`
        """
        model = ReprintShipment()
        if include_optional:
            return ReprintShipment(
                correlation_id = '00adf56ed852487ba9caec62b7ab2635',
                size = 'DOC_8X11',
                type = 'SHIPPING_LABEL',
                format = 'PDF',
                from_address = shipping.models.reprint_shipment_from_address.reprintShipment_fromAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'Stamford', 
                    company = 'Pitney Bowes Inc.', 
                    country_code = 'US', 
                    email = 'john.publica@pb.com', 
                    name = 'Paul Wright', 
                    phone = '203-555-1213', 
                    postal_code = '06905-4317', 
                    residential = False, 
                    state_province = 'CT', ),
                parcel = shipping.models.reprint_shipment_parcel.reprintShipment_parcel(
                    height = 1, 
                    length = 2, 
                    width = 1, 
                    dim_unit = 'IN', 
                    weight_unit = 'OZ', 
                    weight = 1, ),
                parcel_tracking_number = '9471309105156000826739',
                rate = {"baseCharge":25.5,"carrier":"USPS","currencyCode":"USD","parcelType":"PKG","rateTypeId":"CONTRACT_RATES","serviceId":"EM","specialServices":[{"fee":88.5,"inputParameters":[{"name":"INPUT_VALUE","value":"5000"}],"specialServiceId":"Ins"},{"fee":0,"specialServiceId":"PO to Addressee"},{"fee":3.35,"inputParameters":[{"name":"INPUT_VALUE","value":"12345"}],"specialServiceId":"RR"},{"fee":0,"specialServiceId":"Sig"},{"fee":0,"specialServiceId":"liveanimal"}],"totalCarrierCharge":117.35},
                shipment_id = 'USPS2200579677758143',
                shipment_options = shipping.models.shipment_options.shipmentOptions(
                    add_to_manifest = True, 
                    print_custom_message = 'Print Message 1', 
                    receipt_option = 'RECEIPT_WITH_INSTRUCTIONS', 
                    print_department = 'department', 
                    print_invoice_number = 'invoicenumber', 
                    print_po_number = 'ponumber', 
                    package_description = 'packagedescription', ),
                to_address = shipping.models.reprint_shipment_to_address.reprintShipment_toAddress(
                    address_line1 = '27 Watervw Dr', 
                    address_line2 = 'near abc street', 
                    address_line3 = 'near xyz street', 
                    city_town = 'Rochester', 
                    company = 'ABC Company', 
                    country_code = 'US', 
                    email = 'rs.canid@gmail.com', 
                    name = 'Rufous Sirius Canid', 
                    phone = '323 555-1212', 
                    postal_code = '14609-7418', 
                    residential = False, 
                    state_province = 'NY', )
            )
        else:
            return ReprintShipment(
        )
        """

    def testReprintShipment(self):
        """Test ReprintShipment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
