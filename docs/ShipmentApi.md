# shipping.ShipmentApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_shipment_by_id**](ShipmentApi.md#cancel_shipment_by_id) | **PUT** /api/v1/shipments/{shipmentId}/cancel | Cancel Shipment
[**cancel_stamps_err**](ShipmentApi.md#cancel_stamps_err) | **POST** /api/v1/err/stamps/void | Cancel Stamps ERR
[**create_return_label**](ShipmentApi.md#create_return_label) | **POST** /api/v1/shipments/{shipmentId}/return | Create Return label shipment
[**create_shipment**](ShipmentApi.md#create_shipment) | **POST** /api/v1/shipments | Create Shipment
[**download_bpod_files**](ShipmentApi.md#download_bpod_files) | **POST** /api/v1/err/shipments/bpod | Download BPOD Files
[**get_all_shipments**](ShipmentApi.md#get_all_shipments) | **GET** /api/v1/shipments | Get All Shipments
[**get_carrier_accounts**](ShipmentApi.md#get_carrier_accounts) | **GET** /api/v1/carrierAccounts | Get Carrier Accounts
[**get_carriers**](ShipmentApi.md#get_carriers) | **GET** /api/v1/carriers | Get Carriers
[**get_countries**](ShipmentApi.md#get_countries) | **GET** /api/v1/countries | Get Countries
[**get_parcel_types**](ShipmentApi.md#get_parcel_types) | **GET** /api/v1/parcelTypes | Get Parcel Types
[**get_rates**](ShipmentApi.md#get_rates) | **POST** /api/v1/rates | Rate Shop and Get Single Rate
[**get_services**](ShipmentApi.md#get_services) | **GET** /api/v1/services | Get Services
[**get_signature_image_err**](ShipmentApi.md#get_signature_image_err) | **GET** /api/v1/err/shipments/{shipmentId}/signaturefile | Signature Image ERR
[**get_special_services**](ShipmentApi.md#get_special_services) | **GET** /api/v1/specialServices | Get Special Services
[**reprint_shipment_by_id**](ShipmentApi.md#reprint_shipment_by_id) | **GET** /api/v1/shipments/{shipmentId}/reprint | Reprint Shipment
[**shipment_by_id**](ShipmentApi.md#shipment_by_id) | **GET** /api/v1/shipments/{shipmentId} | Get Shipment by Id


# **cancel_shipment_by_id**
> CancelShipment cancel_shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Cancel Shipment

This operation cancel/void shipment.

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
    api_instance = shipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | This indicates the shipmentId, a unique identifier assigned for the Shipment.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Cancel Shipment
        api_response = api_instance.cancel_shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->cancel_shipment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->cancel_shipment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| This indicates the shipmentId, a unique identifier assigned for the Shipment. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

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
**200** | The Shipment has been cancelled. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_stamps_err**
> CancelStampsResponseERR cancel_stamps_err(cancel_stamps_request_err, x_pb_developer_partner_id=x_pb_developer_partner_id)

Cancel Stamps ERR

This operation cancels (voids) stamps generated for ERR (Electronic Return Receipt).  - User needs to provide *Stamp IDs* to cancel those specific ERR stamps.  - User can download the *Refund Form* having details of generated Postage.  - At once, maximum 1000 stamps can be requested for cancelation. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.cancel_stamps_request_err import CancelStampsRequestERR
from shipping.models.cancel_stamps_response_err import CancelStampsResponseERR
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
    api_instance = shipping.ShipmentApi(api_client)
    cancel_stamps_request_err = shipping.CancelStampsRequestERR() # CancelStampsRequestERR | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Cancel Stamps ERR
        api_response = api_instance.cancel_stamps_err(cancel_stamps_request_err, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->cancel_stamps_err:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->cancel_stamps_err: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_stamps_request_err** | [**CancelStampsRequestERR**](CancelStampsRequestERR.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**CancelStampsResponseERR**](CancelStampsResponseERR.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stamps Refund Form has been generated. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_return_label**
> ReturnLabelResponse create_return_label(shipment_id, return_label, x_pb_developer_partner_id=x_pb_developer_partner_id)

Create Return label shipment

This operation creates a return label based on a previous shipment. <br> The return label can be created in two ways:  <br> 1. User need not to provide any details of package, address and service. The API would take all details from the shipmentId mentioned in the path parameter and would swap the address and create return label. However for UPS `specialServices` object is required as carrier mandates to provide package description with PRL special service. <br> 2. User can customize the request by passing `fromAddress`, `toAddress`, `parcelType`, `serviceId` in the request itself. <br> Please Note that for UPS it is required to pass `specialServices` object with `PRL` service id and  input parameters with name as `RETURN_PKG_DESCRIPTION`. <br> For FedEx `specialServices` object is not required and PRL is added by default while creating return.  If user wishes to provide RMA number, it can be passed in `specialServices` object in the request body. <br> Please Note If user provides any information in this request it overrides the information in onward shipment which was created <br> For example if user provides toAddress in the request the return label will get created with recipient as mentioned in toAddress and  if user provides fromAddress in the request, the return label will be created with sender as mentioned in fromAddress

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.return_label import ReturnLabel
from shipping.models.return_label_response import ReturnLabelResponse
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
    api_instance = shipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | It specifies the shipmentId of onward shipment against which return label has to be created.
    return_label = shipping.ReturnLabel() # ReturnLabel | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Create Return label shipment
        api_response = api_instance.create_return_label(shipment_id, return_label, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->create_return_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->create_return_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| It specifies the shipmentId of onward shipment against which return label has to be created. | 
 **return_label** | [**ReturnLabel**](ReturnLabel.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**ReturnLabelResponse**](ReturnLabelResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Return Label has been created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shipment**
> CreateShipment200Response create_shipment(create_shipment_request, x_pb_developer_partner_id=x_pb_developer_partner_id)

Create Shipment

This operation creates a new Shipment or Shipment Label. This is for both Domestic and International.<br> For domestic, Create a shipment requires domestic addresses (within same country)- ToAddress and FromAddress, and  carrier service and special service.<br> While for International, Create a shipment requires international delivery, that is ToAddress must be the different country (and not the same country mentioned in From Address), selected services, special services, and customs information. <br> <br> Note- To create Return shipment using this API- If PRL (return special service) is used, user need to provide sender address (from where return shipment is to be created) in `fromAddress` object and recipient address (to where return is to be created) in `toAddress` object. System will not swap the address for return in this API. If you want to create return for the already created shipment, you may use `Create Return Label Shipment` API. <br> <br> Note: Currently Shipment created from below API gets assigned to the Default location of the subscription.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_shipment200_response import CreateShipment200Response
from shipping.models.create_shipment_request import CreateShipmentRequest
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
    api_instance = shipping.ShipmentApi(api_client)
    create_shipment_request = shipping.CreateShipmentRequest() # CreateShipmentRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Create Shipment
        api_response = api_instance.create_shipment(create_shipment_request, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->create_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->create_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shipment_request** | [**CreateShipmentRequest**](CreateShipmentRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**CreateShipment200Response**](CreateShipment200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shipment has been created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_bpod_files**
> BPODDownloadResponse download_bpod_files(x_pb_developer_partner_id=x_pb_developer_partner_id, start_date=start_date, end_date=end_date, body=body)

Download BPOD Files

This API operation is used to download bulk of ERR (*Electronic Return Receipt*) - POD (*Proof of Delivery*) files, which are specific to USPS carrier. <br />   User can download BPOD (*Bulk Proof of Delivery*) files either using *Shipment IDs* or *Date Range*.    If user wants to check records based on dates and download BPOD files accordingly, then *Start Date* and *End Date* need to be passed in the request body as filter. Else *Shipment IDs* will be used as default value when user does not provide *DateRange* filter. <br />   User is restricted to download 1000 BPOD files as max limit. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.bpod_download_request import BPODDownloadRequest
from shipping.models.bpod_download_response import BPODDownloadResponse
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)
    start_date = 'start_date_example' # str | The BPOD files to be downloaded from which Date is the startDate in the Date Range filter. This field is not required if the Shipment IDs provided in the request body. (optional)
    end_date = 'end_date_example' # str | The BPOD files to be downloaded till which Date is the endDate in the Date Range filter. This field is not required if the Shipment IDs provided in the request body. (optional)
    body = shipping.BPODDownloadRequest() # BPODDownloadRequest | This is the request body to download BPOD files. Request body supports max of 1000 ShipmentIDs in a request. (optional)

    try:
        # Download BPOD Files
        api_response = api_instance.download_bpod_files(x_pb_developer_partner_id=x_pb_developer_partner_id, start_date=start_date, end_date=end_date, body=body)
        print("The response of ShipmentApi->download_bpod_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->download_bpod_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 
 **start_date** | **str**| The BPOD files to be downloaded from which Date is the startDate in the Date Range filter. This field is not required if the Shipment IDs provided in the request body. | [optional] 
 **end_date** | **str**| The BPOD files to be downloaded till which Date is the endDate in the Date Range filter. This field is not required if the Shipment IDs provided in the request body. | [optional] 
 **body** | [**BPODDownloadRequest**](BPODDownloadRequest.md)| This is the request body to download BPOD files. Request body supports max of 1000 ShipmentIDs in a request. | [optional] 

### Return type

[**BPODDownloadResponse**](BPODDownloadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ZIP URL for BPOD files has been created for download. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_shipments**
> GetAllShipments get_all_shipments(x_pb_developer_partner_id=x_pb_developer_partner_id, start_date=start_date, end_date=end_date, page=page, size=size)

Get All Shipments

This operation fetches all created Shipments. If query parameters are not provided, it will default endDate as current date, page as 1 and size as 10.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_all_shipments import GetAllShipments
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    start_date = 'start_date_example' # str | While searching shipments, user set a date range to get all created shipments. This indicatesthe start date of the set date range under shipment search criteria. The date format must be: YYYY-MM-DD. (optional)
    end_date = 'end_date_example' # str | While searching shipments, user set a date range to get all created shipments. This indicatesthe end date of the set date range under shipment search criteria. The date format must be: YYYY-MM-DD. (optional)
    page = 'page_example' # str | This indicates the page of the Shipments search result list. (optional)
    size = 'size_example' # str | This indicates the size/count of the searched result list. (optional)

    try:
        # Get All Shipments
        api_response = api_instance.get_all_shipments(x_pb_developer_partner_id=x_pb_developer_partner_id, start_date=start_date, end_date=end_date, page=page, size=size)
        print("The response of ShipmentApi->get_all_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_all_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **start_date** | **str**| While searching shipments, user set a date range to get all created shipments. This indicatesthe start date of the set date range under shipment search criteria. The date format must be: YYYY-MM-DD. | [optional] 
 **end_date** | **str**| While searching shipments, user set a date range to get all created shipments. This indicatesthe end date of the set date range under shipment search criteria. The date format must be: YYYY-MM-DD. | [optional] 
 **page** | **str**| This indicates the page of the Shipments search result list. | [optional] 
 **size** | **str**| This indicates the size/count of the searched result list. | [optional] 

### Return type

[**GetAllShipments**](GetAllShipments.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shipments. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carrier_accounts**
> GetCarrierAccounts200Response get_carrier_accounts(x_pb_developer_partner_id=x_pb_developer_partner_id)

Get Carrier Accounts

This operation retrieves onboarded Carriers with their Carrier Account Ids which uniquely identify multiple accounts of same carrier.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_carrier_accounts200_response import GetCarrierAccounts200Response
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Get Carrier Accounts
        api_response = api_instance.get_carrier_accounts(x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->get_carrier_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_carrier_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**GetCarrierAccounts200Response**](GetCarrierAccounts200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Carrier Accounts has been fetched. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carriers**
> Carriers get_carriers(x_pb_developer_partner_id=x_pb_developer_partner_id)

Get Carriers

This operation fetches all supported carriers. This service is used to get list of supported carriers and their properties.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.carriers import Carriers
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Get Carriers
        api_response = api_instance.get_carriers(x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->get_carriers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_carriers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**Carriers**](Carriers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available carriers have been fetched. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> List[CountriesInner] get_countries(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code)

Get Countries

This operation fetches list of supported destination countries for a provided carrier and origin country. If query parameters are not provided, it will default to `USPS` as carrier and `US` as origin country.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.countries_inner import CountriesInner
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    carrier = 'carrier_example' # str | This indicates the carrierID, a unique identifier given to  an individual carrier. (optional)
    origin_country_code = 'origin_country_code_example' # str | This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. (optional)

    try:
        # Get Countries
        api_response = api_instance.get_countries(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code)
        print("The response of ShipmentApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **carrier** | **str**| This indicates the carrierID, a unique identifier given to  an individual carrier. | [optional] 
 **origin_country_code** | **str**| This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. | [optional] 

### Return type

[**List[CountriesInner]**](CountriesInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Countries has been fetched. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_types**
> List[ParcelTypesInner] get_parcel_types(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)

Get Parcel Types

This operation fetches Parcel Types based on the provided carrier, origin county, and the destination country. If query parameters are not provided, this will default to `USPS` as carrier, `US` as both origin and destination country code.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.parcel_types_inner import ParcelTypesInner
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    carrier = 'carrier_example' # str | This indicates the CarrierID, a unique identifier given to an individual carrier. It can be referred from the response of Get Carriers API (optional)
    origin_country_code = 'origin_country_code_example' # str | This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. (optional)
    destination_country_code = 'destination_country_code_example' # str | This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. (optional)

    try:
        # Get Parcel Types
        api_response = api_instance.get_parcel_types(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)
        print("The response of ShipmentApi->get_parcel_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_parcel_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **carrier** | **str**| This indicates the CarrierID, a unique identifier given to an individual carrier. It can be referred from the response of Get Carriers API | [optional] 
 **origin_country_code** | **str**| This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. | [optional] 
 **destination_country_code** | **str**| This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. | [optional] 

### Return type

[**List[ParcelTypesInner]**](ParcelTypesInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Parcel Types has been fetched. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rates**
> GetRates200Response get_rates(get_rates_request, x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response)

Rate Shop and Get Single Rate

This API contains 2 operations, rate shop and single rate. Rate shop will fetch rates for all carrier services based on the given addresses (From and To), weight, and dimension for given parcelType. If parcelType is not provided, it will default to `PKG`. Single rate will get rate for specific service and special service (if requested) based on the given addresses (From and To), weight, and dimension, parcelType and serviceId with or without specialServices. Single rate will be used mainly to a rate a shipment before creating shipment.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_rates200_response import GetRates200Response
from shipping.models.get_rates_request import GetRatesRequest
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
    api_instance = shipping.ShipmentApi(api_client)
    get_rates_request = shipping.GetRatesRequest() # GetRatesRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    compact_response = true # bool | This header defines if the response required is detailed or compact. When value is set to true, it will only return rates object in response. (optional)

    try:
        # Rate Shop and Get Single Rate
        api_response = api_instance.get_rates(get_rates_request, x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response)
        print("The response of ShipmentApi->get_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_rates_request** | [**GetRatesRequest**](GetRatesRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **compact_response** | **bool**| This header defines if the response required is detailed or compact. When value is set to true, it will only return rates object in response. | [optional] 

### Return type

[**GetRates200Response**](GetRates200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Rating is done for the shipment(s). |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> List[ServicesInner] get_services(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)

Get Services

This operation fetches a list of supported services for a carrier with respect to specific origin and destination country. If query parameters are not provided, this will default to `USPS` as carrier, `US` as both origin and destination country code.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.services_inner import ServicesInner
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    carrier = 'carrier_example' # str | This indicates the CarrierID, a unique identifier provided to an individual carrier. It can be referred from the response of Get Carriers API (optional)
    origin_country_code = 'origin_country_code_example' # str | This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. (optional)
    destination_country_code = 'destination_country_code_example' # str | This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. (optional)

    try:
        # Get Services
        api_response = api_instance.get_services(x_pb_developer_partner_id=x_pb_developer_partner_id, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)
        print("The response of ShipmentApi->get_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **carrier** | **str**| This indicates the CarrierID, a unique identifier provided to an individual carrier. It can be referred from the response of Get Carriers API | [optional] 
 **origin_country_code** | **str**| This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. | [optional] 
 **destination_country_code** | **str**| This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. | [optional] 

### Return type

[**List[ServicesInner]**](ServicesInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of services has been fetched. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_image_err**
> SignatureFileResponse get_signature_image_err(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Signature Image ERR

This operation provides a downloadable link which consists of a signature image for specific ERR (Electronic Return Receipt) shipment, and this is known as POD. <br /> Proof of Delivery (POD) is a document or file that shows an evidence of shipment delivery. This file contains the digital copy of recipient's signature, i.e., the signature image, in the form of downloadable link or URL.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.signature_file_response import SignatureFileResponse
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
    api_instance = shipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | Shipment ID is a unique identifier for an individual shipment.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Signature Image ERR
        api_response = api_instance.get_signature_image_err(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->get_signature_image_err:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_signature_image_err: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| Shipment ID is a unique identifier for an individual shipment. | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**SignatureFileResponse**](SignatureFileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signature image as proof of delivered shipment. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_special_services**
> SpecialServices get_special_services(x_pb_developer_partner_id=x_pb_developer_partner_id, service=service, parcel=parcel, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)

Get Special Services

This operation fetches Special Services for a given carrier, service, origin country, and the destination country. If query parameters are not provided, it will default to `USPS` as carrier,`US` as both origin and destination country and would show for all service and parcel types

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.special_services import SpecialServices
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
    api_instance = shipping.ShipmentApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    service = 'service_example' # str | This indicates the serviceId. It can be referred from response of `Get Services` API (optional)
    parcel = 'parcel_example' # str | This indicates the parcel Id, a unique identifier named to individual package. It can be referred from response of `Get Parcel Types` API (optional)
    carrier = 'carrier_example' # str | This indicates the CarrierID, a unique identifier given to  an individual carrier. It can be referred from response of `Get Carriers` API (optional)
    origin_country_code = 'origin_country_code_example' # str | This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. (optional)
    destination_country_code = 'destination_country_code_example' # str | This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. (optional)

    try:
        # Get Special Services
        api_response = api_instance.get_special_services(x_pb_developer_partner_id=x_pb_developer_partner_id, service=service, parcel=parcel, carrier=carrier, origin_country_code=origin_country_code, destination_country_code=destination_country_code)
        print("The response of ShipmentApi->get_special_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->get_special_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **service** | **str**| This indicates the serviceId. It can be referred from response of &#x60;Get Services&#x60; API | [optional] 
 **parcel** | **str**| This indicates the parcel Id, a unique identifier named to individual package. It can be referred from response of &#x60;Get Parcel Types&#x60; API | [optional] 
 **carrier** | **str**| This indicates the CarrierID, a unique identifier given to  an individual carrier. It can be referred from response of &#x60;Get Carriers&#x60; API | [optional] 
 **origin_country_code** | **str**| This indicates the Source Country. The two-character ISO country code for the country where the Shipment originates. | [optional] 
 **destination_country_code** | **str**| This indicates the Destination Country for the Shipment. The two-character ISO country code for the country where the shipment is to be delivered. | [optional] 

### Return type

[**SpecialServices**](SpecialServices.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Special Service has been fetched successfully. |  * X-Pb-Transactionid - The X-PB-TransactionId is unique id for this request. <br>  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reprint_shipment_by_id**
> ReprintShipment reprint_shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response)

Reprint Shipment

This operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentId returned by the original Created Shipment request. Use this only if the shipping label in the Create Shipment response was spoilt or lost.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.reprint_shipment import ReprintShipment
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
    api_instance = shipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | This indicates the shipmentId, a unique identifier assigned to the Shipment.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)
    compact_response = false # bool | This header defines if the response required is detailed or compact. When value is set to true, it will only return label layout details and parcel tracking number object in response. (optional)

    try:
        # Reprint Shipment
        api_response = api_instance.reprint_shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id, compact_response=compact_response)
        print("The response of ShipmentApi->reprint_shipment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->reprint_shipment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| This indicates the shipmentId, a unique identifier assigned to the Shipment. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 
 **compact_response** | **bool**| This header defines if the response required is detailed or compact. When value is set to true, it will only return label layout details and parcel tracking number object in response. | [optional] 

### Return type

[**ReprintShipment**](ReprintShipment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shipment has been reprinted. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_by_id**
> GetSingleShipment shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Get Shipment by Id

This operation retrieves shipment details using shipmentId.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_single_shipment import GetSingleShipment
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
    api_instance = shipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | This indicates the shipmentId, a unique identifier for an individual Shipment.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Get Shipment by Id
        api_response = api_instance.shipment_by_id(shipment_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of ShipmentApi->shipment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| This indicates the shipmentId, a unique identifier for an individual Shipment. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**GetSingleShipment**](GetSingleShipment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shipment has been retrieved. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

