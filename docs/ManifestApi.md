# shipping.ManifestApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manifest**](ManifestApi.md#create_manifest) | **POST** /api/v1/manifests | Create Manifest
[**reprint_manifest**](ManifestApi.md#reprint_manifest) | **POST** /api/v1/manifests/reprint | Reprint manifest


# **create_manifest**
> CreateManifest200Response create_manifest(x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response, create_manifest_request=create_manifest_request)

Create Manifest

This operation creates an end-of-day manifest (a compilation of information about all shipments) that combines all shipments of the day into a single form or electronic record, depending on the carrier. For different carriers, the Manifest process varies, e.g., USPS use SCAN Form while FedEx has Manifest Form.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_manifest200_response import CreateManifest200Response
from shipping.models.create_manifest_request import CreateManifestRequest
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
    api_instance = shipping.ManifestApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    compact_response = false # bool | This header defines if the response required is detailed or compact. When value is set to true, it will only return manifest details in response.  (optional)
    create_manifest_request = {"carrierAccountId":"abcd12","fromAddress":{"addressLine1":"27 Watervw Dr","addressLine2":"near abc street","addressLine3":"near xyz street","cityTown":"shelton","company":"","countryCode":"US","email":"","name":"","phone":"","postalCode":"06484","stateProvince":"CT"},"submissionDate":"2023-05-25"} # CreateManifestRequest |  (optional)

    try:
        # Create Manifest
        api_response = api_instance.create_manifest(x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response, create_manifest_request=create_manifest_request)
        print("The response of ManifestApi->create_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->create_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **compact_response** | **bool**| This header defines if the response required is detailed or compact. When value is set to true, it will only return manifest details in response.  | [optional] 
 **create_manifest_request** | [**CreateManifestRequest**](CreateManifestRequest.md)|  | [optional] 

### Return type

[**CreateManifest200Response**](CreateManifest200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Manifest has been generated for the given carrier. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reprint_manifest**
> CreateManifest200Response reprint_manifest(x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response, reprint_manifest_request=reprint_manifest_request)

Reprint manifest

This operation reprints a manifest for which the initial created manifest request was successful.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_manifest200_response import CreateManifest200Response
from shipping.models.reprint_manifest_request import ReprintManifestRequest
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
    api_instance = shipping.ManifestApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    compact_response = false # bool | This header defines if the response required is detailed or compact. When value is set to true, it will only return manifest details in response. (optional)
    reprint_manifest_request = {"carrierAccountId":"JORx6bVG8mr","manifestID":"1234567890"} # ReprintManifestRequest |  (optional)

    try:
        # Reprint manifest
        api_response = api_instance.reprint_manifest(x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response, reprint_manifest_request=reprint_manifest_request)
        print("The response of ManifestApi->reprint_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->reprint_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **compact_response** | **bool**| This header defines if the response required is detailed or compact. When value is set to true, it will only return manifest details in response. | [optional] 
 **reprint_manifest_request** | [**ReprintManifestRequest**](ReprintManifestRequest.md)|  | [optional] 

### Return type

[**CreateManifest200Response**](CreateManifest200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Manifest has been printed successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

