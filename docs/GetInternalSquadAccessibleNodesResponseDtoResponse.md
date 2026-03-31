# GetInternalSquadAccessibleNodesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**squad_uuid** | **UUID** |  | 
**accessible_nodes** | [**List[GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner]**](GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_internal_squad_accessible_nodes_response_dto_response import GetInternalSquadAccessibleNodesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInternalSquadAccessibleNodesResponseDtoResponse from a JSON string
get_internal_squad_accessible_nodes_response_dto_response_instance = GetInternalSquadAccessibleNodesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetInternalSquadAccessibleNodesResponseDtoResponse.to_json())

# convert the object into a dict
get_internal_squad_accessible_nodes_response_dto_response_dict = get_internal_squad_accessible_nodes_response_dto_response_instance.to_dict()
# create an instance of GetInternalSquadAccessibleNodesResponseDtoResponse from a dict
get_internal_squad_accessible_nodes_response_dto_response_from_dict = GetInternalSquadAccessibleNodesResponseDtoResponse.from_dict(get_internal_squad_accessible_nodes_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


