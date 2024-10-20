# shipping.DefaultsApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_defaults**](DefaultsApi.md#create_defaults) | **POST** /api/v1/defaults | Create Defaults
[**delete_defaults_by_id**](DefaultsApi.md#delete_defaults_by_id) | **DELETE** /api/v1/defaults/{defaultID} | Delete Defaults by ID
[**get_all_defaults**](DefaultsApi.md#get_all_defaults) | **GET** /api/v1/defaults | Get All Defaults
[**get_defaults_by_id**](DefaultsApi.md#get_defaults_by_id) | **GET** /api/v1/defaults/{defaultID} | Get Defaults By ID
[**put_defaults_by_id**](DefaultsApi.md#put_defaults_by_id) | **PUT** /api/v1/defaults/{defaultID} | Update Defaults


# **create_defaults**
> CreateDefaultsResponse create_defaults(create_defaults)

Create Defaults

While creating shipment, a few columns/ fields information are used mandatorily, and if the value for those columns are used repetitively, then it is always better to save last used values. And hence, this API has been introduced. Using this API, default values can be set up for frequently used columns/fields information like carrier, its linked services, and special services.  Setting up the defaults will save both time and efforts. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_defaults import CreateDefaults
from shipping.models.create_defaults_response import CreateDefaultsResponse
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
    api_instance = shipping.DefaultsApi(api_client)
    create_defaults = shipping.CreateDefaults() # CreateDefaults | 

    try:
        # Create Defaults
        api_response = api_instance.create_defaults(create_defaults)
        print("The response of DefaultsApi->create_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultsApi->create_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_defaults** | [**CreateDefaults**](CreateDefaults.md)|  | 

### Return type

[**CreateDefaultsResponse**](CreateDefaultsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Defaults (i.e., default values) have been created successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_defaults_by_id**
> delete_defaults_by_id(default_id)

Delete Defaults by ID

This operation deletes the existing Defaults.

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
    api_instance = shipping.DefaultsApi(api_client)
    default_id = 'default_id_example' # str | This is unique identifier assigned to Defaults while its creation using CreateDefaults API.

    try:
        # Delete Defaults by ID
        api_instance.delete_defaults_by_id(default_id)
    except Exception as e:
        print("Exception when calling DefaultsApi->delete_defaults_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_id** | **str**| This is unique identifier assigned to Defaults while its creation using CreateDefaults API. | 

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
**200** | Defaults (i.e., default values) have been deleted successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_defaults**
> AllDefaults get_all_defaults(x_pb_developer_partner_id=x_pb_developer_partner_id, page=page, size=size)

Get All Defaults

The operation fetches all created Defaults. If query parameters are not provided, it will consider default page as 1 and default size as 10.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.all_defaults import AllDefaults
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
    api_instance = shipping.DefaultsApi(api_client)
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    page = 'page_example' # str | The page of the Defaults search result list. (optional)
    size = 'size_example' # str | The size/count of the searched result list. (optional)

    try:
        # Get All Defaults
        api_response = api_instance.get_all_defaults(x_pb_developer_partner_id=x_pb_developer_partner_id, page=page, size=size)
        print("The response of DefaultsApi->get_all_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultsApi->get_all_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **page** | **str**| The page of the Defaults search result list. | [optional] 
 **size** | **str**| The size/count of the searched result list. | [optional] 

### Return type

[**AllDefaults**](AllDefaults.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Defaults. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_defaults_by_id**
> DefaultResponse get_defaults_by_id(default_id)

Get Defaults By ID

This operation fetches the values set for the Defaults.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.default_response import DefaultResponse
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
    api_instance = shipping.DefaultsApi(api_client)
    default_id = 'default_id_example' # str | This is unique identifier assigned to Defaults while its creation using CreateDefaults API.

    try:
        # Get Defaults By ID
        api_response = api_instance.get_defaults_by_id(default_id)
        print("The response of DefaultsApi->get_defaults_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultsApi->get_defaults_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_id** | **str**| This is unique identifier assigned to Defaults while its creation using CreateDefaults API. | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Defaults values have been retrieved successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_defaults_by_id**
> put_defaults_by_id(default_id, create_defaults)

Update Defaults

This operation updates the values set for Defaults.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_defaults import CreateDefaults
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
    api_instance = shipping.DefaultsApi(api_client)
    default_id = 'default_id_example' # str | This is unique identifier assigned to Defaults while its creation using CreateDefaults API.
    create_defaults = shipping.CreateDefaults() # CreateDefaults | 

    try:
        # Update Defaults
        api_instance.put_defaults_by_id(default_id, create_defaults)
    except Exception as e:
        print("Exception when calling DefaultsApi->put_defaults_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_id** | **str**| This is unique identifier assigned to Defaults while its creation using CreateDefaults API. | 
 **create_defaults** | [**CreateDefaults**](CreateDefaults.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Defaults (i.e., default values) have been updated successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | The request could not be authorized. |  -  |
**500** | The request could not be completed due to an internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

