# shipping.ShipmentByRateShopApi

All URIs are relative to *https://api-sandbox.sendpro360.pitneybowes.com/shipping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_shipment_by_id_v2**](ShipmentByRateShopApi.md#cancel_shipment_by_id_v2) | **POST** /api/v2/shipments/cancel | Cancel Shipment
[**create_shipment_v2**](ShipmentByRateShopApi.md#create_shipment_v2) | **POST** /api/v2/shipments | Create Shipment
[**reprint_shipment_by_id_v2**](ShipmentByRateShopApi.md#reprint_shipment_by_id_v2) | **POST** /api/v2/shipments/reprint | Reprint Shipment


# **cancel_shipment_by_id_v2**
> CancelShipmentV2 cancel_shipment_by_id_v2(shipment_cancel_v2, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Cancel Shipment

The operation cancel/void shipment.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.cancel_shipment_v2 import CancelShipmentV2
from shipping.models.shipment_cancel_v2 import ShipmentCancelV2
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
    api_instance = shipping.ShipmentByRateShopApi(api_client)
    shipment_cancel_v2 = shipping.ShipmentCancelV2() # ShipmentCancelV2 | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique Transaction ID provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Cancel Shipment
        api_response = api_instance.cancel_shipment_by_id_v2(shipment_cancel_v2, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of ShipmentByRateShopApi->cancel_shipment_by_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentByRateShopApi->cancel_shipment_by_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_cancel_v2** | [**ShipmentCancelV2**](ShipmentCancelV2.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique Transaction ID provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**CancelShipmentV2**](CancelShipmentV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_shipment_v2**
> DomesticShipmentResponseV2 create_shipment_v2(create_shipment_v2_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Create Shipment

The operation creates a new Shipment or generate a Shipment Label. - To create a domestic shipment, the operation requires   - Domestic addresses 'To' and 'From' locations respectively within the same country   - carrier services, and   - associated special services. - While for the International shipment, the operation requires   - International address(es) for delivery, that is 'To' address must be the international country location(s) and not the same country mentioned in 'From' address   - supported international carrier services   - associated special service(s), and    - customs information. 

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.create_shipment_v2_request import CreateShipmentV2Request
from shipping.models.domestic_shipment_response_v2 import DomesticShipmentResponseV2
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
    api_instance = shipping.ShipmentByRateShopApi(api_client)
    create_shipment_v2_request = shipping.CreateShipmentV2Request() # CreateShipmentV2Request | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique Transaction ID provided by the partner, which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Create Shipment
        api_response = api_instance.create_shipment_v2(create_shipment_v2_request, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of ShipmentByRateShopApi->create_shipment_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentByRateShopApi->create_shipment_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shipment_v2_request** | [**CreateShipmentV2Request**](CreateShipmentV2Request.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique Transaction ID provided by the partner, which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**DomesticShipmentResponseV2**](DomesticShipmentResponseV2.md)

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

# **reprint_shipment_by_id_v2**
> ReprintShipmentV2 reprint_shipment_by_id_v2(shipment_reprint_v2, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)

Reprint Shipment

The operation reprints Shipment by the shipmentId. It retrieves an existing shipping label to reprint. The API sends the shipmentID returned by the original created shipment request. Use this only if the shipping label in the Create Shipment response is missing or lost.

### Example

* Bearer Authentication (bearerAuth):

```python
import shipping
from shipping.models.reprint_shipment_v2 import ReprintShipmentV2
from shipping.models.shipment_reprint_v2 import ShipmentReprintV2
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
    api_instance = shipping.ShipmentByRateShopApi(api_client)
    shipment_reprint_v2 = shipping.ShipmentReprintV2() # ShipmentReprintV2 | 
    x_pb_developer_partner_id = 'x_pb_developer_partner_id_example' # str | The Developer Partner ID is assigned by PB to uniquely identify a Developer's strategic business partners. If the developer is the sole business partner, this field isn't required. (optional)
    x_pb_location_id = 'x_pb_location_id_example' # str | This is the Location ID assigned as per the Developer's and Partner's parsed locations, to which all transactions will be billed. <br /> Partner's location will be used for billing if it is configured, however, in case Partner's location is not given, then the Developer's location will be taken. Developer's location will be the default value. <br /> Additionally, Developers and Partners can use carriers belong to this location only. (optional)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique transaction Id provided by the partner which is used to enable debugging and linking between the client's transaction and the system. (optional)

    try:
        # Reprint Shipment
        api_response = api_instance.reprint_shipment_by_id_v2(shipment_reprint_v2, x_pb_developer_partner_id=x_pb_developer_partner_id, x_pb_location_id=x_pb_location_id, x_pb_transaction_id=x_pb_transaction_id)
        print("The response of ShipmentByRateShopApi->reprint_shipment_by_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentByRateShopApi->reprint_shipment_by_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_reprint_v2** | [**ShipmentReprintV2**](ShipmentReprintV2.md)|  | 
 **x_pb_developer_partner_id** | **str**| The Developer Partner ID is assigned by PB to uniquely identify a Developer&#39;s strategic business partners. If the developer is the sole business partner, this field isn&#39;t required. | [optional] 
 **x_pb_location_id** | **str**| This is the Location ID assigned as per the Developer&#39;s and Partner&#39;s parsed locations, to which all transactions will be billed. &lt;br /&gt; Partner&#39;s location will be used for billing if it is configured, however, in case Partner&#39;s location is not given, then the Developer&#39;s location will be taken. Developer&#39;s location will be the default value. &lt;br /&gt; Additionally, Developers and Partners can use carriers belong to this location only. | [optional] 
 **x_pb_transaction_id** | **str**| A unique transaction Id provided by the partner which is used to enable debugging and linking between the client&#39;s transaction and the system. | [optional] 

### Return type

[**ReprintShipmentV2**](ReprintShipmentV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

