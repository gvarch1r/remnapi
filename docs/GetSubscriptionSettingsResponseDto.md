# GetSubscriptionSettingsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionSettingsResponseDtoResponse**](GetSubscriptionSettingsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_settings_response_dto import GetSubscriptionSettingsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionSettingsResponseDto from a JSON string
get_subscription_settings_response_dto_instance = GetSubscriptionSettingsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionSettingsResponseDto.to_json())

# convert the object into a dict
get_subscription_settings_response_dto_dict = get_subscription_settings_response_dto_instance.to_dict()
# create an instance of GetSubscriptionSettingsResponseDto from a dict
get_subscription_settings_response_dto_from_dict = GetSubscriptionSettingsResponseDto.from_dict(get_subscription_settings_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


