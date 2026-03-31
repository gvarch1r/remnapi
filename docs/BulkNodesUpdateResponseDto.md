# BulkNodesUpdateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_nodes_update_response_dto import BulkNodesUpdateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkNodesUpdateResponseDto from a JSON string
bulk_nodes_update_response_dto_instance = BulkNodesUpdateResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkNodesUpdateResponseDto.to_json())

# convert the object into a dict
bulk_nodes_update_response_dto_dict = bulk_nodes_update_response_dto_instance.to_dict()
# create an instance of BulkNodesUpdateResponseDto from a dict
bulk_nodes_update_response_dto_from_dict = BulkNodesUpdateResponseDto.from_dict(bulk_nodes_update_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


