# ReorderNodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[ReorderSubscriptionPageConfigsRequestDtoItemsInner]**](ReorderSubscriptionPageConfigsRequestDtoItemsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_node_request_dto import ReorderNodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderNodeRequestDto from a JSON string
reorder_node_request_dto_instance = ReorderNodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReorderNodeRequestDto.to_json())

# convert the object into a dict
reorder_node_request_dto_dict = reorder_node_request_dto_instance.to_dict()
# create an instance of ReorderNodeRequestDto from a dict
reorder_node_request_dto_from_dict = ReorderNodeRequestDto.from_dict(reorder_node_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


