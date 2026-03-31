# ReorderNodePluginsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReorderSubscriptionPageConfigsRequestDtoItemsInner]**](ReorderSubscriptionPageConfigsRequestDtoItemsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_node_plugins_request_dto import ReorderNodePluginsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderNodePluginsRequestDto from a JSON string
reorder_node_plugins_request_dto_instance = ReorderNodePluginsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReorderNodePluginsRequestDto.to_json())

# convert the object into a dict
reorder_node_plugins_request_dto_dict = reorder_node_plugins_request_dto_instance.to_dict()
# create an instance of ReorderNodePluginsRequestDto from a dict
reorder_node_plugins_request_dto_from_dict = ReorderNodePluginsRequestDto.from_dict(reorder_node_plugins_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


