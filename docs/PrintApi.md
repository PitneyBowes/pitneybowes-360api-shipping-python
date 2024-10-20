# shipping.PrintApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_printer_mapping**](PrintApi.md#delete_printer_mapping) | **DELETE** /api/v1/printer/mapping | Delete Printer mapping
[**get_printer_mapping**](PrintApi.md#get_printer_mapping) | **GET** /api/v1/printer/mapping | Get Printer mapping
[**job_status**](PrintApi.md#job_status) | **GET** /api/v1/jobs/{jobId} | Job status
[**print_document**](PrintApi.md#print_document) | **POST** /api/v1/document/print | Print Document
[**printer_mapping**](PrintApi.md#printer_mapping) | **POST** /api/v1/printer/mapping | Printer mapping


# **delete_printer_mapping**
> delete_printer_mapping(alias, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Delete Printer mapping

delete printer mapping document

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
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
    api_instance = shipping.PrintApi(api_client)
    alias = 'alias_example' # str | Refers to a printer connected (directly or via network) to a computer.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique transaction Id provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Delete Printer mapping
        api_instance.delete_printer_mapping(alias, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
    except Exception as e:
        print("Exception when calling PrintApi->delete_printer_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Refers to a printer connected (directly or via network) to a computer. | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique transaction Id provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted printer mapping |  -  |
**401** | The request could not be authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printer_mapping**
> PrinterMappingGetResponse get_printer_mapping(alias, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Get Printer mapping

Get printer mapping document

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.printer_mapping_get_response import PrinterMappingGetResponse
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
    api_instance = shipping.PrintApi(api_client)
    alias = 'alias_example' # str | Refers to a printer connected (directly or via network) to a computer.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique transaction Id provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Get Printer mapping
        api_response = api_instance.get_printer_mapping(alias, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of PrintApi->get_printer_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintApi->get_printer_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Refers to a printer connected (directly or via network) to a computer. | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique transaction Id provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**PrinterMappingGetResponse**](PrinterMappingGetResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping printer Get Successfully |  -  |
**401** | The request could not be authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_status**
> JobStatus job_status(job_id, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Job status

job status

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.job_status import JobStatus
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
    api_instance = shipping.PrintApi(api_client)
    job_id = 'job_id_example' # str | The jobId, a unique identifier assigned for the job.
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique transaction Id provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Job status
        api_response = api_instance.job_status(job_id, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of PrintApi->job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintApi->job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The jobId, a unique identifier assigned for the job. | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique transaction Id provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document has been printed successfully. |  -  |
**401** | The request could not be authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_document**
> PrintDocumentResponse print_document(print_document_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Print Document

It contains information about a label or a document, e.g. a shipping label, a customs form, manifest report etc., that pertains to a shipment or manifest.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.print_document_request import PrintDocumentRequest
from shipping.models.print_document_response import PrintDocumentResponse
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
    api_instance = shipping.PrintApi(api_client)
    print_document_request = shipping.PrintDocumentRequest() # PrintDocumentRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique Transaction ID provided by the partner, which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Print Document
        api_response = api_instance.print_document(print_document_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of PrintApi->print_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintApi->print_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_document_request** | [**PrintDocumentRequest**](PrintDocumentRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique Transaction ID provided by the partner, which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**PrintDocumentResponse**](PrintDocumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document has been printed successfully. |  -  |
**401** | The request could not be authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printer_mapping**
> PrinterMappingResponse printer_mapping(printer_mapping_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Printer mapping

printer mapping document

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.printer_mapping_request import PrinterMappingRequest
from shipping.models.printer_mapping_response import PrinterMappingResponse
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
    api_instance = shipping.PrintApi(api_client)
    printer_mapping_request = shipping.PrinterMappingRequest() # PrinterMappingRequest | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique transaction Id provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Printer mapping
        api_response = api_instance.printer_mapping(printer_mapping_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of PrintApi->printer_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintApi->printer_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_mapping_request** | [**PrinterMappingRequest**](PrinterMappingRequest.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique transaction Id provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**PrinterMappingResponse**](PrinterMappingResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully mapped printer |  -  |
**401** | The request could not be authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

