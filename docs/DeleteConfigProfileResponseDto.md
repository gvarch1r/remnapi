# DeleteConfigProfileResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_config_profile_response_dto import DeleteConfigProfileResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConfigProfileResponseDto from a JSON string
delete_config_profile_response_dto_instance = DeleteConfigProfileResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteConfigProfileResponseDto.to_json())

# convert the object into a dict
delete_config_profile_response_dto_dict = delete_config_profile_response_dto_instance.to_dict()
# create an instance of DeleteConfigProfileResponseDto from a dict
delete_config_profile_response_dto_from_dict = DeleteConfigProfileResponseDto.from_dict(delete_config_profile_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


