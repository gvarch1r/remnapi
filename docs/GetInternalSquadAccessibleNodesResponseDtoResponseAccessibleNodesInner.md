# GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**node_name** | **str** |  | 
**country_code** | **str** |  | 
**config_profile_uuid** | **UUID** |  | 
**config_profile_name** | **str** |  | 
**active_inbounds** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner import GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner from a JSON string
get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner_instance = GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner.from_json(json)
# print the JSON string representation of the object
print(GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner.to_json())

# convert the object into a dict
get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner_dict = get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner_instance.to_dict()
# create an instance of GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner from a dict
get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner_from_dict = GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner.from_dict(get_internal_squad_accessible_nodes_response_dto_response_accessible_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


