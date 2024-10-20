# shipping.PickupsApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pickups**](PickupsApi.md#cancel_pickups) | **PUT** /api/v1/pickups/cancel | Cancel Pickups
[**cancelled_pickup_document**](PickupsApi.md#cancelled_pickup_document) | **POST** /api/v1/pickups/document | Cancelled Pickup Document
[**get_pickup_document**](PickupsApi.md#get_pickup_document) | **GET** /api/v1/pickups/{pickupId}/document | Get Pickup Document
[**get_pickups**](PickupsApi.md#get_pickups) | **GET** /api/v1/pickups | Get Pickups
[**schedule_pickup**](PickupsApi.md#schedule_pickup) | **POST** /api/v1/pickups | Schedule Pickup


# **cancel_pickups**
> SchedulePickupCancelResponse cancel_pickups(schedule_pickup_cancel_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Cancel Pickups

This operation is used to Cancel the scheduled pickup.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.schedule_pickup_cancel_request import SchedulePickupCancelRequest
from shipping.models.schedule_pickup_cancel_response import SchedulePickupCancelResponse
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
    api_instance = shipping.PickupsApi(api_client)
    schedule_pickup_cancel_request = shipping.SchedulePickupCancelRequest() # SchedulePickupCancelRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Cancel Pickups
        api_response = api_instance.cancel_pickups(schedule_pickup_cancel_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of PickupsApi->cancel_pickups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupsApi->cancel_pickups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_pickup_cancel_request** | [**SchedulePickupCancelRequest**](SchedulePickupCancelRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**SchedulePickupCancelResponse**](SchedulePickupCancelResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pick up cancelled successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancelled_pickup_document**
> GetPickupCancelledDocumentResponse cancelled_pickup_document(type, get_pickup_cancelled_document_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Cancelled Pickup Document

This operation is used to get receipt for pickup cancellation. The receipt generated is in PDF format. <br> This operation can create receipt for multiple pickups which are cancelled.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_pickup_cancelled_document_request import GetPickupCancelledDocumentRequest
from shipping.models.get_pickup_cancelled_document_response import GetPickupCancelledDocumentResponse
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
    api_instance = shipping.PickupsApi(api_client)
    type = 'cancelled' # str | Indicates type of pickup. Supported value is `cancelled`.
    get_pickup_cancelled_document_request = shipping.GetPickupCancelledDocumentRequest() # GetPickupCancelledDocumentRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Cancelled Pickup Document
        api_response = api_instance.cancelled_pickup_document(type, get_pickup_cancelled_document_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of PickupsApi->cancelled_pickup_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupsApi->cancelled_pickup_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Indicates type of pickup. Supported value is &#x60;cancelled&#x60;. | 
 **get_pickup_cancelled_document_request** | [**GetPickupCancelledDocumentRequest**](GetPickupCancelledDocumentRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**GetPickupCancelledDocumentResponse**](GetPickupCancelledDocumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pick up has been cancelled. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pickup_document**
> GetPickupDocument get_pickup_document(pickup_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Get Pickup Document

This operation returns the scheduled pickup or cancellation receipt in PDF format.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_pickup_document import GetPickupDocument
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
    api_instance = shipping.PickupsApi(api_client)
    pickup_id = 'pickup_id_example' # str | It specified the pickupId for which PDF receipt is needed.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Get Pickup Document
        api_response = api_instance.get_pickup_document(pickup_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of PickupsApi->get_pickup_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupsApi->get_pickup_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickup_id** | **str**| It specified the pickupId for which PDF receipt is needed. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**GetPickupDocument**](GetPickupDocument.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pick up document have been fetched. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pickups**
> GetAllPickups get_pickups(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, start_date=start_date, end_date=end_date, status=status, page=page, size=size)

Get Pickups

This operation is used to view the history of pickups scheduled or cancelled for your packages.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_all_pickups import GetAllPickups
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
    api_instance = shipping.PickupsApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    carrier = 'carrier_example' # str | Indicates CarrierID. If not provided, it would show pickups for all the carriers. (optional)
    start_date = 'start_date_example' # str | Indicates start date from when you want to see the history. If not provided, it will take today's date. (optional)
    end_date = 'end_date_example' # str | Indicates end date till you want to see the pickups history. If not provide, it will take today's date. (optional)
    status = 'status_example' # str | Indicates status of the pickup(schedule or cancel). If not provided, it will show the response for both status. (optional)
    page = 3.4 # float | Indicates page number, if not provided page would be 1. (optional)
    size = 3.4 # float | Indicates size of records, if not provided size would be 20 (optional)

    try:
        # Get Pickups
        api_response = api_instance.get_pickups(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, start_date=start_date, end_date=end_date, status=status, page=page, size=size)
        print("The response of PickupsApi->get_pickups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupsApi->get_pickups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **carrier** | **str**| Indicates CarrierID. If not provided, it would show pickups for all the carriers. | [optional] 
 **start_date** | **str**| Indicates start date from when you want to see the history. If not provided, it will take today&#39;s date. | [optional] 
 **end_date** | **str**| Indicates end date till you want to see the pickups history. If not provide, it will take today&#39;s date. | [optional] 
 **status** | **str**| Indicates status of the pickup(schedule or cancel). If not provided, it will show the response for both status. | [optional] 
 **page** | **float**| Indicates page number, if not provided page would be 1. | [optional] 
 **size** | **float**| Indicates size of records, if not provided size would be 20 | [optional] 

### Return type

[**GetAllPickups**](GetAllPickups.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pickups. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_pickup**
> SchedulePickup200Response schedule_pickup(schedule_pickup_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Schedule Pickup

This operation allows to schedule Pickups with USPS, UPS, FedEx and DHLExpress for eligible shipments. <br> Below are four possible combinations for scheduling pickup <br>  <br> 1. When request does not specify `pickupSummary` and `shipmentIds`- The system would consider all eligible shipments created in a current day. <br> 2. When request specifies only `shipmentIds`- Pickup will be created for the shipmentIds mentioned <br> 3. When request specifies only `pickupSummary`- Pickup will be created for the pickup details mentioned in the pickupSummary <br> 4. When request specifies both `pickupSummary` and `shipmentIds`- Pickup will be created including details mentioned in both objects.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.schedule_pickup200_response import SchedulePickup200Response
from shipping.models.schedule_pickup_request import SchedulePickupRequest
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
    api_instance = shipping.PickupsApi(api_client)
    schedule_pickup_request = shipping.SchedulePickupRequest() # SchedulePickupRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Schedule Pickup
        api_response = api_instance.schedule_pickup(schedule_pickup_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of PickupsApi->schedule_pickup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupsApi->schedule_pickup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_pickup_request** | [**SchedulePickupRequest**](SchedulePickupRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**SchedulePickup200Response**](SchedulePickup200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Pick up has been created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

