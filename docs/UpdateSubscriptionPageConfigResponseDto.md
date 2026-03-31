# UpdateSubscriptionPageConfigResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionPageConfigResponseDtoResponse**](GetSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_subscription_page_config_response_dto import UpdateSubscriptionPageConfigResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionPageConfigResponseDto from a JSON string
update_subscription_page_config_response_dto_instance = UpdateSubscriptionPageConfigResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionPageConfigResponseDto.to_json())

# convert the object into a dict
update_subscription_page_config_response_dto_dict = update_subscription_page_config_response_dto_instance.to_dict()
# create an instance of UpdateSubscriptionPageConfigResponseDto from a dict
update_subscription_page_config_response_dto_from_dict = UpdateSubscriptionPageConfigResponseDto.from_dict(update_subscription_page_config_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


