# BulkNodesActionsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**action** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_nodes_actions_request_dto import BulkNodesActionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkNodesActionsRequestDto from a JSON string
bulk_nodes_actions_request_dto_instance = BulkNodesActionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkNodesActionsRequestDto.to_json())

# convert the object into a dict
bulk_nodes_actions_request_dto_dict = bulk_nodes_actions_request_dto_instance.to_dict()
# create an instance of BulkNodesActionsRequestDto from a dict
bulk_nodes_actions_request_dto_from_dict = BulkNodesActionsRequestDto.from_dict(bulk_nodes_actions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


