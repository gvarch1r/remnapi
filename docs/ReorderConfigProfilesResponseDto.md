# ReorderConfigProfilesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponse**](GetConfigProfilesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_config_profiles_response_dto import ReorderConfigProfilesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderConfigProfilesResponseDto from a JSON string
reorder_config_profiles_response_dto_instance = ReorderConfigProfilesResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderConfigProfilesResponseDto.to_json())

# convert the object into a dict
reorder_config_profiles_response_dto_dict = reorder_config_profiles_response_dto_instance.to_dict()
# create an instance of ReorderConfigProfilesResponseDto from a dict
reorder_config_profiles_response_dto_from_dict = ReorderConfigProfilesResponseDto.from_dict(reorder_config_profiles_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


