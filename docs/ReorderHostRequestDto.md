# ReorderHostRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ReorderSubscriptionPageConfigsRequestDtoItemsInner]**](ReorderSubscriptionPageConfigsRequestDtoItemsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_host_request_dto import ReorderHostRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderHostRequestDto from a JSON string
reorder_host_request_dto_instance = ReorderHostRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReorderHostRequestDto.to_json())

# convert the object into a dict
reorder_host_request_dto_dict = reorder_host_request_dto_instance.to_dict()
# create an instance of ReorderHostRequestDto from a dict
reorder_host_request_dto_from_dict = ReorderHostRequestDto.from_dict(reorder_host_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


