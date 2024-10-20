# shipping.MultipieceApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multipiece_rates**](MultipieceApi.md#multipiece_rates) | **POST** /api/v1/multipiece/rates | Multipiece Rateshop and Rates
[**multipiece_shipment**](MultipieceApi.md#multipiece_shipment) | **POST** /api/v1/multipiece/shipments | Multipiece Shipment
[**multipiece_shipment_cancel**](MultipieceApi.md#multipiece_shipment_cancel) | **PUT** /api/v1/multipiece/shipments/{shipmentId}/cancel | Cancel Multipiece Shipment
[**multipiece_shipment_reprint**](MultipieceApi.md#multipiece_shipment_reprint) | **GET** /api/v1/multipiece/shipments/{shipmentId}/reprint | Reprint Multipiece Shipment


# **multipiece_rates**
> MultipieceRates200Response multipiece_rates(multipiece_rates_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Multipiece Rateshop and Rates

This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType in multiPieceParcels object. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.  <br> For UPS- multipiece shipment with Envelopes (having parcel Type as LTR) is not supported.  <br> For FEDEX Multipiece, all parcels must be of same packaging type while creating multipiece shipment

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.multipiece_rates200_response import MultipieceRates200Response
from shipping.models.multipiece_rates_request import MultipieceRatesRequest
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
    api_instance = shipping.MultipieceApi(api_client)
    multipiece_rates_request = shipping.MultipieceRatesRequest() # MultipieceRatesRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Develover Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Multipiece Rateshop and Rates
        api_response = api_instance.multipiece_rates(multipiece_rates_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of MultipieceApi->multipiece_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipieceApi->multipiece_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multipiece_rates_request** | [**MultipieceRatesRequest**](MultipieceRatesRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Develover Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**MultipieceRates200Response**](MultipieceRates200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Multipiece Rates created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multipiece_shipment**
> MultipieceShipment200Response multipiece_shipment(multipiece_shipment_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Multipiece Shipment

This operation is used to create Multipiece Shipments. UPS, FedEx and DHL Express are supported for Multipiece Shipments.  <br> For UPS- multipiece shipment with Envelopes (having parcel Type as LTR) is not supported.  <br> For FEDEX Multipiece, all parcels must be of same packaging type while creating multipiece shipment

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.multipiece_shipment200_response import MultipieceShipment200Response
from shipping.models.multipiece_shipment_request import MultipieceShipmentRequest
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
    api_instance = shipping.MultipieceApi(api_client)
    multipiece_shipment_request = shipping.MultipieceShipmentRequest() # MultipieceShipmentRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Develover Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Multipiece Shipment
        api_response = api_instance.multipiece_shipment(multipiece_shipment_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of MultipieceApi->multipiece_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipieceApi->multipiece_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multipiece_shipment_request** | [**MultipieceShipmentRequest**](MultipieceShipmentRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Develover Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**MultipieceShipment200Response**](MultipieceShipment200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Multipiece Shipment created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multipiece_shipment_cancel**
> CancelShipment multipiece_shipment_cancel(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Cancel Multipiece Shipment

This operation is used to cancel the multipiece label. It takes the shipmentId of the multipiece shipment done.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.cancel_shipment import CancelShipment
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
    api_instance = shipping.MultipieceApi(api_client)
    shipment_id = 'shipment_id_example' # str | It specifies the shipmentId of onward shipment against which return label has to be created.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Develover Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Cancel Multipiece Shipment
        api_response = api_instance.multipiece_shipment_cancel(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of MultipieceApi->multipiece_shipment_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipieceApi->multipiece_shipment_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| It specifies the shipmentId of onward shipment against which return label has to be created. | 
 **x_pb_developer_partner_id** | **str**| This is the Develover Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**CancelShipment**](CancelShipment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Multipiece Shipment created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multipiece_shipment_reprint**
> MultipieceDomesticShipmentResponse multipiece_shipment_reprint(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Reprint Multipiece Shipment

This operation is used to reprint the multipiece label. It takes the shipmentId of the multipiece shipment done.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.multipiece_domestic_shipment_response import MultipieceDomesticShipmentResponse
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
    api_instance = shipping.MultipieceApi(api_client)
    shipment_id = 'shipment_id_example' # str | It specifies the shipmentId of onward shipment against which return label has to be created.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Develover Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Reprint Multipiece Shipment
        api_response = api_instance.multipiece_shipment_reprint(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of MultipieceApi->multipiece_shipment_reprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultipieceApi->multipiece_shipment_reprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| It specifies the shipmentId of onward shipment against which return label has to be created. | 
 **x_pb_developer_partner_id** | **str**| This is the Develover Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**MultipieceDomesticShipmentResponse**](MultipieceDomesticShipmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Multipiece Shipment created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

