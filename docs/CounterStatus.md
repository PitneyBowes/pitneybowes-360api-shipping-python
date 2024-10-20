# CounterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The number of items that were successfully processed. | [optional] 
**failed** | **float** | The number of items that failed processing. | [optional] 
**pending** | **float** | The number of items that are pending processing. | [optional] 

## Example

```python
from shipping.models.counter_status import CounterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CounterStatus from a JSON string
counter_status_instance = CounterStatus.from_json(json)
# print the JSON string representation of the object
print(CounterStatus.to_json())

# convert the object into a dict
counter_status_dict = counter_status_instance.to_dict()
# create an instance of CounterStatus from a dict
counter_status_from_dict = CounterStatus.from_dict(counter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


