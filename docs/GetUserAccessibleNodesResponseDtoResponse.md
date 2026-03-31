# GetUserAccessibleNodesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **UUID** |  | 
**active_nodes** | [**List[GetUserAccessibleNodesResponseDtoResponseActiveNodesInner]**](GetUserAccessibleNodesResponseDtoResponseActiveNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_accessible_nodes_response_dto_response import GetUserAccessibleNodesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAccessibleNodesResponseDtoResponse from a JSON string
get_user_accessible_nodes_response_dto_response_instance = GetUserAccessibleNodesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserAccessibleNodesResponseDtoResponse.to_json())

# convert the object into a dict
get_user_accessible_nodes_response_dto_response_dict = get_user_accessible_nodes_response_dto_response_instance.to_dict()
# create an instance of GetUserAccessibleNodesResponseDtoResponse from a dict
get_user_accessible_nodes_response_dto_response_from_dict = GetUserAccessibleNodesResponseDtoResponse.from_dict(get_user_accessible_nodes_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


