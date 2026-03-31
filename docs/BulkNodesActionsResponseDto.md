# BulkNodesActionsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_nodes_actions_response_dto import BulkNodesActionsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkNodesActionsResponseDto from a JSON string
bulk_nodes_actions_response_dto_instance = BulkNodesActionsResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkNodesActionsResponseDto.to_json())

# convert the object into a dict
bulk_nodes_actions_response_dto_dict = bulk_nodes_actions_response_dto_instance.to_dict()
# create an instance of BulkNodesActionsResponseDto from a dict
bulk_nodes_actions_response_dto_from_dict = BulkNodesActionsResponseDto.from_dict(bulk_nodes_actions_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


