# CreateNodeResponseDtoResponseConfigProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_config_profile_uuid** | **UUID** |  | 
**active_inbounds** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_config_profile import CreateNodeResponseDtoResponseConfigProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseConfigProfile from a JSON string
create_node_response_dto_response_config_profile_instance = CreateNodeResponseDtoResponseConfigProfile.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseConfigProfile.to_json())

# convert the object into a dict
create_node_response_dto_response_config_profile_dict = create_node_response_dto_response_config_profile_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseConfigProfile from a dict
create_node_response_dto_response_config_profile_from_dict = CreateNodeResponseDtoResponseConfigProfile.from_dict(create_node_response_dto_response_config_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


