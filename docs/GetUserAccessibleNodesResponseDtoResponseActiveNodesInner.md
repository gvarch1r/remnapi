# GetUserAccessibleNodesResponseDtoResponseActiveNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**node_name** | **str** |  | 
**country_code** | **str** |  | 
**config_profile_uuid** | **UUID** |  | 
**config_profile_name** | **str** |  | 
**active_squads** | [**List[GetUserAccessibleNodesResponseDtoResponseActiveNodesInnerActiveSquadsInner]**](GetUserAccessibleNodesResponseDtoResponseActiveNodesInnerActiveSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_accessible_nodes_response_dto_response_active_nodes_inner import GetUserAccessibleNodesResponseDtoResponseActiveNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAccessibleNodesResponseDtoResponseActiveNodesInner from a JSON string
get_user_accessible_nodes_response_dto_response_active_nodes_inner_instance = GetUserAccessibleNodesResponseDtoResponseActiveNodesInner.from_json(json)
# print the JSON string representation of the object
print(GetUserAccessibleNodesResponseDtoResponseActiveNodesInner.to_json())

# convert the object into a dict
get_user_accessible_nodes_response_dto_response_active_nodes_inner_dict = get_user_accessible_nodes_response_dto_response_active_nodes_inner_instance.to_dict()
# create an instance of GetUserAccessibleNodesResponseDtoResponseActiveNodesInner from a dict
get_user_accessible_nodes_response_dto_response_active_nodes_inner_from_dict = GetUserAccessibleNodesResponseDtoResponseActiveNodesInner.from_dict(get_user_accessible_nodes_response_dto_response_active_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


