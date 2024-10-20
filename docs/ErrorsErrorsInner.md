# ErrorsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Error code(s) that appear due to HTTP  400- Invalid or Bad Request, e.g. validation-error. | [optional] 
**error_description** | **str** | The HTTP 400 Bad Request response status code indicates that the server cannot process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [optional] 
**additional_code** | **str** | A unique identifier for the error, for example 1101055, 0100008, or 1021126. | [optional] 
**additional_info** | **str** | This is an additional information about the error. This error &#39;Invalid Request&#39; might appear due to invalid dimension, weight, or serviceid, or if the information is missing. | [optional] 
**additional_parameters** | **List[str]** |  | [optional] 

## Example

```python
from shipping.models.errors_errors_inner import ErrorsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsErrorsInner from a JSON string
errors_errors_inner_instance = ErrorsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorsErrorsInner.to_json())

# convert the object into a dict
errors_errors_inner_dict = errors_errors_inner_instance.to_dict()
# create an instance of ErrorsErrorsInner from a dict
errors_errors_inner_from_dict = ErrorsErrorsInner.from_dict(errors_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


