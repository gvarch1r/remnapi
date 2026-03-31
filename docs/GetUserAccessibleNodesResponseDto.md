# GetUserAccessibleNodesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetUserAccessibleNodesResponseDtoResponse**](GetUserAccessibleNodesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_accessible_nodes_response_dto import GetUserAccessibleNodesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAccessibleNodesResponseDto from a JSON string
get_user_accessible_nodes_response_dto_instance = GetUserAccessibleNodesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserAccessibleNodesResponseDto.to_json())

# convert the object into a dict
get_user_accessible_nodes_response_dto_dict = get_user_accessible_nodes_response_dto_instance.to_dict()
# create an instance of GetUserAccessibleNodesResponseDto from a dict
get_user_accessible_nodes_response_dto_from_dict = GetUserAccessibleNodesResponseDto.from_dict(get_user_accessible_nodes_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


