# CreateNodeRequestDtoConfigProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_config_profile_uuid** | **UUID** |  | 
**active_inbounds** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_request_dto_config_profile import CreateNodeRequestDtoConfigProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeRequestDtoConfigProfile from a JSON string
create_node_request_dto_config_profile_instance = CreateNodeRequestDtoConfigProfile.from_json(json)
# print the JSON string representation of the object
print(CreateNodeRequestDtoConfigProfile.to_json())

# convert the object into a dict
create_node_request_dto_config_profile_dict = create_node_request_dto_config_profile_instance.to_dict()
# create an instance of CreateNodeRequestDtoConfigProfile from a dict
create_node_request_dto_config_profile_from_dict = CreateNodeRequestDtoConfigProfile.from_dict(create_node_request_dto_config_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


