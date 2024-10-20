# JobStatusPrintStatusTransactionInner

The Array containing print statuses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The status transaction ID of the Print document. | [optional] 
**status** | **str** | Status of the Print document. | [optional] 

## Example

```python
from shipping.models.job_status_print_status_transaction_inner import JobStatusPrintStatusTransactionInner

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusPrintStatusTransactionInner from a JSON string
job_status_print_status_transaction_inner_instance = JobStatusPrintStatusTransactionInner.from_json(json)
# print the JSON string representation of the object
print(JobStatusPrintStatusTransactionInner.to_json())

# convert the object into a dict
job_status_print_status_transaction_inner_dict = job_status_print_status_transaction_inner_instance.to_dict()
# create an instance of JobStatusPrintStatusTransactionInner from a dict
job_status_print_status_transaction_inner_from_dict = JobStatusPrintStatusTransactionInner.from_dict(job_status_print_status_transaction_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


