import os

sys.path.append('./shipping')
import shipping
from shipping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.sendpro360.pitneybowes.com/shipping
# See configuration.py for a list of all supported configuration parameters.
configuration = shipping.Configuration(
    host = "https://api-sandbox.sendpro360.pitneybowes.com/shipping"
)

# Configure Bearer authorization: bearerAuth
configuration.access_token = os.environ["BEARER_TOKEN"]

# Enter a context with an instance of the API client
with shipping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping.CarrierApi(api_client)

    try:
        # Get all carrier accounts
        api_response = api_instance.get_carrier_accounts()
        print("The response of CarrierApi->get_carrier_accounts:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CarrierApi->get_carrier_accounts: %s\n" % e)