# UpdateSubscriptionSettingsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionSettingsResponseDtoResponse**](GetSubscriptionSettingsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_subscription_settings_response_dto import UpdateSubscriptionSettingsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionSettingsResponseDto from a JSON string
update_subscription_settings_response_dto_instance = UpdateSubscriptionSettingsResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionSettingsResponseDto.to_json())

# convert the object into a dict
update_subscription_settings_response_dto_dict = update_subscription_settings_response_dto_instance.to_dict()
# create an instance of UpdateSubscriptionSettingsResponseDto from a dict
update_subscription_settings_response_dto_from_dict = UpdateSubscriptionSettingsResponseDto.from_dict(update_subscription_settings_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


