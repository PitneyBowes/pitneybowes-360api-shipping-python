# shipping.BatchApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_import_api**](BatchApi.md#bulk_import_api) | **POST** /api/v1/shipments/importUrl | Bulk Import Shipments
[**bulk_import_apierr**](BatchApi.md#bulk_import_apierr) | **POST** /api/v1/err/shipments/importUrl | Bulk Import Shipments ERR
[**create_bulk_shipments_api**](BatchApi.md#create_bulk_shipments_api) | **POST** /api/v1/bulkShipments | Create Bulk Shipments
[**create_bulk_shipments_apierr**](BatchApi.md#create_bulk_shipments_apierr) | **POST** /api/v1/err/bulkShipments | Create Bulk Shipments ERR
[**get_batch_status_api**](BatchApi.md#get_batch_status_api) | **GET** /api/v1/shipments/batch/{batchId}/status | Get Batch Status
[**get_shipment_details_for_batch_api**](BatchApi.md#get_shipment_details_for_batch_api) | **GET** /api/v1/shipments/batch/{batchId}/shipments | Get Batch Shipment Details
[**process_batch_api**](BatchApi.md#process_batch_api) | **POST** /api/v1/shipments/batch/{batchId}/process | Process Batch
[**void_shipping_label**](BatchApi.md#void_shipping_label) | **POST** /api/v1/shipments/batch/{batchId}/void | Void Batch Shipping Labels


# **bulk_import_api**
> ShipmentBatch bulk_import_api(body, x_pb_developer_partner_id=x_pb_developer_partner_id)

Bulk Import Shipments

This operation imports the .CSV file, which includes all the required fields to create shipments in bulk. The payload contains information about the shipments you want to import, such as `carrier account`, `label layout`, `service`, and any `special services` required for the shipments. After batch is submitted, user needs to upload csv file of shipment transactions to the uploadURL returned in response.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_batch_request import CreateBatchRequest
from shipping.models.shipment_batch import ShipmentBatch
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
    api_instance = shipping.BatchApi(api_client)
    body = shipping.CreateBatchRequest() # CreateBatchRequest |  This is the Request body to bulk import shipments.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Bulk Import Shipments
        api_response = api_instance.bulk_import_api(body, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->bulk_import_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->bulk_import_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBatchRequest**](CreateBatchRequest.md)|  This is the Request body to bulk import shipments. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**ShipmentBatch**](ShipmentBatch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  The bulk shipment has been successfully imported. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_import_apierr**
> ShipmentBatchResponseERR bulk_import_apierr(body, x_pb_developer_partner_id=x_pb_developer_partner_id)

Bulk Import Shipments ERR

This operation imports the .CSV file which includes fields required for creating ERR (Electronic Return Receipt) Bulk Shipments.    The payload, which is used for shipment transactions, contains the following essential information in .CSV file:   - Carrier Account   - Output format: Shipping Label and Coversheet    - Services, and   - Special Services     The above-mentioned information are stored in AWS-S3 which in turn provides URL to users. When Batch is submitted, S3 returned URL along with .CSV file are uploaded, which generates BatchID.    The same BatchID is used to track the status of BulkImport. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_batch_request_err import CreateBatchRequestERR
from shipping.models.shipment_batch_response_err import ShipmentBatchResponseERR
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
    api_instance = shipping.BatchApi(api_client)
    body = shipping.CreateBatchRequestERR() # CreateBatchRequestERR |  This is the request body to import ERR Bulk shipments.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The PB-Developer-Partner-ID is assigned by PB to uniquely identify a developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Bulk Import Shipments ERR
        api_response = api_instance.bulk_import_apierr(body, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->bulk_import_apierr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->bulk_import_apierr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBatchRequestERR**](CreateBatchRequestERR.md)|  This is the request body to import ERR Bulk shipments. | 
 **x_pb_developer_partner_id** | **str**| The PB-Developer-Partner-ID is assigned by PB to uniquely identify a developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**ShipmentBatchResponseERR**](ShipmentBatchResponseERR.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  ERR Bulk Shipment has been successfully imported. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bulk_shipments_api**
> BulkShipmentResponse create_bulk_shipments_api(body, x_pb_developer_partner_id=x_pb_developer_partner_id)

Create Bulk Shipments

This operation creates a batch of bulk (larger quantities) shipments for single or multiple recipients. The shipments can be addressed to a single or multiple recipients with different combination of carrier, service special services and parcel type. `carrierAccountId`, `parcelType`, `serviceId` and `specialServices` are used as default when user do not wish to provide at shipment level. If user choose to provide these at Shipment level then it overrides the values provided at root level. At shipment level either you can wish to provide all of `carrierAccountId`, `parcelType`, `serviceId` and `specialServices` or not provide all of them if wants to use default ones from root level. If user do not provide any one out of `carrierAccountId`, `parcelType` and `serviceId` at shipment level it would result in validation error

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.bulk_shipment_response import BulkShipmentResponse
from shipping.models.create_bulk_shipments_api_request import CreateBulkShipmentsAPIRequest
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
    api_instance = shipping.BatchApi(api_client)
    body = shipping.CreateBulkShipmentsAPIRequest() # CreateBulkShipmentsAPIRequest | This is the Request body to create bulk shipments.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | This is the Developer Partner ID. When the developer is the only partner, this field is not required. (optional)

    try:
        # Create Bulk Shipments
        api_response = api_instance.create_bulk_shipments_api(body, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->create_bulk_shipments_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->create_bulk_shipments_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBulkShipmentsAPIRequest**](CreateBulkShipmentsAPIRequest.md)| This is the Request body to create bulk shipments. | 
 **x_pb_developer_partner_id** | **str**| This is the Developer Partner ID. When the developer is the only partner, this field is not required. | [optional] 

### Return type

[**BulkShipmentResponse**](BulkShipmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Batch Shipment has been created. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bulk_shipments_apierr**
> BulkShipmentResponseERR create_bulk_shipments_apierr(body, x_pb_developer_partner_id=x_pb_developer_partner_id)

Create Bulk Shipments ERR

ERR (Electronic Return Receipt) is an official United States Postal Service® (USPS) document designed to be equivalent to the hardcopy 'green card' Return Receipt. <br />    It provides the following information:   - Name of the Recipient     - Time when article is delivered   - Signature (image) of the Recipient     - Address where the item is delivered, and    - Date when the article gets delivered.      ERR is combined with certain classes and categories of mails, which are as follow:   - First-Class Mail®    - Priority Mail®     ERR Batch supports two types of Shipment Document format:    - Shipping Label    - Coversheet       This API \"Create Bulk Shipments with ERR\" operation requires the following information:   - Recipient (Single or Multiple)   - Carrier - USPS   - Service   - Parcel Type, and   - Special Service.    The ERR API works at two levels: Shipment level and Root level. Root level is marked as Default, where multiple shipments are processed and entities are common for all shipments. While at Shipment level, entities might differ. <br />   User can either define values for *CarrierAccountID*, *ParcelType*, *ServiceID*, and *SpecialService* respectively at the Root level for all shipments, or mention the values at Shipment level, i.e., for individual shipment(s).     If user does not provide values for the above-mentioned fields combinedly at Shipment level, then the default values for these fields provided at Root level will be considered. While, if user provides these values combinedly at Shipment Level for individual shipment(s), it will override the values defined at Root level. <br />   <br />   *Condition: The fields *CarrierAccountID*, *ParcelType*, *ServiceID* are treated as a combination, and values against each field must be provided if user selects Shipment level. In case any of these field(s) out of the mentioned combination is/are missing, it will return validation error.*    

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.bulk_shipment_response_err import BulkShipmentResponseERR
from shipping.models.create_bulk_shipments_apierr_request import CreateBulkShipmentsAPIERRRequest
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
    api_instance = shipping.BatchApi(api_client)
    body = shipping.CreateBulkShipmentsAPIERRRequest() # CreateBulkShipmentsAPIERRRequest | This is the request body to create Bulk Shipment for ERR.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer-Partner-ID is assigned by PB to uniquely identify a developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Create Bulk Shipments ERR
        api_response = api_instance.create_bulk_shipments_apierr(body, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->create_bulk_shipments_apierr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->create_bulk_shipments_apierr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBulkShipmentsAPIERRRequest**](CreateBulkShipmentsAPIERRRequest.md)| This is the request body to create Bulk Shipment for ERR. | 
 **x_pb_developer_partner_id** | **str**| The Developer-Partner-ID is assigned by PB to uniquely identify a developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**BulkShipmentResponseERR**](BulkShipmentResponseERR.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Bulk Shipment for ERR has been successfully created. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_status_api**
> GetStatusDetailedResponse get_batch_status_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Get Batch Status

This operation retrieves the status of an existing Batch using *Batch ID*. Once the Job status is completed, the URL received from Response can be used to download the shipping label in PDF format.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_status_detailed_response import GetStatusDetailedResponse
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
    api_instance = shipping.BatchApi(api_client)
    batch_id = 'batch_id_example' # str | This is a system-generated unique identifier assigned to the Batch while it is processed.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer-Partner- ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Get Batch Status
        api_response = api_instance.get_batch_status_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->get_batch_status_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_batch_status_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| This is a system-generated unique identifier assigned to the Batch while it is processed. | 
 **x_pb_developer_partner_id** | **str**| The Developer-Partner- ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**GetStatusDetailedResponse**](GetStatusDetailedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Here, is the status of the Batch ID. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_details_for_batch_api**
> GetShipmentsForBatch get_shipment_details_for_batch_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id, page=page, size=size, status=status, step=step)

Get Batch Shipment Details

\"This API operation provides the shipment details for those shipments which are SUCCESS or FAILED during batch processing at the following levels: - addressValidation - rating - labelGeneration, and - voidLabel  Based on fields/data mentioned in Query Parameter, user can check shipment details for particular status at any levels. <br /> If no values are provided in the fields mentioned in Query Parameter, the default for each will be: - Page: 1  - Size: 20 - Status: SUCCESS/FAILED. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.get_shipments_for_batch import GetShipmentsForBatch
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
    api_instance = shipping.BatchApi(api_client)
    batch_id = 'batch_id_example' # str | This is a system-generated unique identifier assigned to the Batch while it is processed
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer-Partner- ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)
    page = 56 # int | It returns detailed information for shipments status and it can cover in one or more pages. The default value for page number is 1. (optional)
    size = 56 # int | Indicates the number of records per page. The default value for records is 20. (optional)
    status = 'status_example' # str | The status of the shipment. Values can be Failed or Success. (optional)
    step = 'step_example' # str | Indicates various stages of the batch processing. (optional)

    try:
        # Get Batch Shipment Details
        api_response = api_instance.get_shipment_details_for_batch_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id, page=page, size=size, status=status, step=step)
        print("The response of BatchApi->get_shipment_details_for_batch_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_shipment_details_for_batch_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| This is a system-generated unique identifier assigned to the Batch while it is processed | 
 **x_pb_developer_partner_id** | **str**| The Developer-Partner- ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 
 **page** | **int**| It returns detailed information for shipments status and it can cover in one or more pages. The default value for page number is 1. | [optional] 
 **size** | **int**| Indicates the number of records per page. The default value for records is 20. | [optional] 
 **status** | **str**| The status of the shipment. Values can be Failed or Success. | [optional] 
 **step** | **str**| Indicates various stages of the batch processing. | [optional] 

### Return type

[**GetShipmentsForBatch**](GetShipmentsForBatch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed status of processed shipments for the batch. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_batch_api**
> ProcessShipmentResponse process_batch_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id)

Process Batch

This operation processes (executes) the existing Batch. The payload for this endpoint needs only an empty JSON object and no additional data is required in the request body. The BatchID parameter located in the endpoint specifies which batch of shipments to process.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.process_shipment_response import ProcessShipmentResponse
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
    api_instance = shipping.BatchApi(api_client)
    batch_id = 'batch_id_example' # str | This is a system-generated unique identifier assigned to the Batch while it is processed.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer-Partner-ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)

    try:
        # Process Batch
        api_response = api_instance.process_batch_api(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id)
        print("The response of BatchApi->process_batch_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->process_batch_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| This is a system-generated unique identifier assigned to the Batch while it is processed. | 
 **x_pb_developer_partner_id** | **str**| The Developer-Partner-ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 

### Return type

[**ProcessShipmentResponse**](ProcessShipmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Batch has been processed successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_shipping_label**
> VoidBatchResponse void_shipping_label(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id, void_batch_request=void_batch_request)

Void Batch Shipping Labels

This operation cancels (voids) shipments which are created using the Batch API operation `createBulkShipments`. <br /> If user wants to cancel specific shipment(s) of the Batch, then s/he needs to pass the *Shipment ID* for the selected shipments in the `shipmentIDs` array. While if user wants to cancel all shipments of the Batch, then s/he does not need to provide any *Shipment ID* in the array under request body.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.void_batch_request import VoidBatchRequest
from shipping.models.void_batch_response import VoidBatchResponse
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
    api_instance = shipping.BatchApi(api_client)
    batch_id = 'batch_id_example' # str | This is a system-generated unique identifier assigned to the Batch while it is processed.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer-Partner-ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field is not required. (optional)
    void_batch_request = shipping.VoidBatchRequest() # VoidBatchRequest |  This is the request body for cancelling the selected shipments or entire Batch of shipments*. (optional)

    try:
        # Void Batch Shipping Labels
        api_response = api_instance.void_shipping_label(batch_id, x_pb_developer_partner_id=x_pb_developer_partner_id, void_batch_request=void_batch_request)
        print("The response of BatchApi->void_shipping_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->void_shipping_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| This is a system-generated unique identifier assigned to the Batch while it is processed. | 
 **x_pb_developer_partner_id** | **str**| The Developer-Partner-ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field is not required. | [optional] 
 **void_batch_request** | [**VoidBatchRequest**](VoidBatchRequest.md)|  This is the request body for cancelling the selected shipments or entire Batch of shipments*. | [optional] 

### Return type

[**VoidBatchResponse**](VoidBatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The indicated shipment(s) of Batch have been successfully cancelled. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

