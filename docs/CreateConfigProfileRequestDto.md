# CreateConfigProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**config** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.create_config_profile_request_dto import CreateConfigProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigProfileRequestDto from a JSON string
create_config_profile_request_dto_instance = CreateConfigProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateConfigProfileRequestDto.to_json())

# convert the object into a dict
create_config_profile_request_dto_dict = create_config_profile_request_dto_instance.to_dict()
# create an instance of CreateConfigProfileRequestDto from a dict
create_config_profile_request_dto_from_dict = CreateConfigProfileRequestDto.from_dict(create_config_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


