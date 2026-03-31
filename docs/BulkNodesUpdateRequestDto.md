# BulkNodesUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**fields** | [**BulkNodesUpdateRequestDtoFields**](BulkNodesUpdateRequestDtoFields.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_nodes_update_request_dto import BulkNodesUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkNodesUpdateRequestDto from a JSON string
bulk_nodes_update_request_dto_instance = BulkNodesUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkNodesUpdateRequestDto.to_json())

# convert the object into a dict
bulk_nodes_update_request_dto_dict = bulk_nodes_update_request_dto_instance.to_dict()
# create an instance of BulkNodesUpdateRequestDto from a dict
bulk_nodes_update_request_dto_from_dict = BulkNodesUpdateRequestDto.from_dict(bulk_nodes_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


