# UpdateConfigProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_config_profile_request_dto import UpdateConfigProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigProfileRequestDto from a JSON string
update_config_profile_request_dto_instance = UpdateConfigProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateConfigProfileRequestDto.to_json())

# convert the object into a dict
update_config_profile_request_dto_dict = update_config_profile_request_dto_instance.to_dict()
# create an instance of UpdateConfigProfileRequestDto from a dict
update_config_profile_request_dto_from_dict = UpdateConfigProfileRequestDto.from_dict(update_config_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


