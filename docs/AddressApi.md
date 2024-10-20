# shipping.AddressApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_suggest**](AddressApi.md#address_suggest) | **POST** /api/v1/address/suggest | Address Suggest
[**address_validate**](AddressApi.md#address_validate) | **POST** /api/v1/address/verify | Address Validate


# **address_suggest**
> AddressSuggestResponse address_suggest(address_suggest_request)

Address Suggest

This operation displays a valid address to match the entered address, only if the address does not seem valid to the system address map. User can select the suggested address or edit the entered address to make it valid.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.address_suggest_request import AddressSuggestRequest
from shipping.models.address_suggest_response import AddressSuggestResponse
from shipping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.sendpro360.pitneybowes.com/shipping
# See configuration.py for a list of all supported configuration parameters.
configuration = shipping.Configuration(
    host = "https://api-sandbox.sendpro360.pitneybowes.com/shipping"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = shipping.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shipping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping.AddressApi(api_client)
    address_suggest_request = shipping.AddressSuggestRequest() # AddressSuggestRequest | 

    try:
        # Address Suggest
        api_response = api_instance.address_suggest(address_suggest_request)
        print("The response of AddressApi->address_suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->address_suggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_suggest_request** | [**AddressSuggestRequest**](AddressSuggestRequest.md)|  | 

### Return type

[**AddressSuggestResponse**](AddressSuggestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The address is suggested to use. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_validate**
> AddressValidateResponse address_validate(address_validate_request, minimal_address_validation=minimal_address_validation)

Address Validate

This operation validates address. This improves postal addresses within the country (e.g., United States) to help ensure that parcels are rated accurately and shipments arrive at the final destination on time.<br> The verify address operation sends an address to be verified. The response indicates whether the address is valid.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.address_validate_request import AddressValidateRequest
from shipping.models.address_validate_response import AddressValidateResponse
from shipping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.sendpro360.pitneybowes.com/shipping
# See configuration.py for a list of all supported configuration parameters.
configuration = shipping.Configuration(
    host = "https://api-sandbox.sendpro360.pitneybowes.com/shipping"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = shipping.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with shipping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping.AddressApi(api_client)
    address_validate_request = shipping.AddressValidateRequest() # AddressValidateRequest | 
    minimal_address_validation = true # bool | If true, then only City, State, and PostalCode (zip) are validated. This option is specific for US domestic addresses only. (optional)

    try:
        # Address Validate
        api_response = api_instance.address_validate(address_validate_request, minimal_address_validation=minimal_address_validation)
        print("The response of AddressApi->address_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->address_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_validate_request** | [**AddressValidateRequest**](AddressValidateRequest.md)|  | 
 **minimal_address_validation** | **bool**| If true, then only City, State, and PostalCode (zip) are validated. This option is specific for US domestic addresses only. | [optional] 

### Return type

[**AddressValidateResponse**](AddressValidateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The address has been verified. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

