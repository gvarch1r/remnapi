# RevokeUserSubscriptionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.revoke_user_subscription_response_dto import RevokeUserSubscriptionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeUserSubscriptionResponseDto from a JSON string
revoke_user_subscription_response_dto_instance = RevokeUserSubscriptionResponseDto.from_json(json)
# print the JSON string representation of the object
print(RevokeUserSubscriptionResponseDto.to_json())

# convert the object into a dict
revoke_user_subscription_response_dto_dict = revoke_user_subscription_response_dto_instance.to_dict()
# create an instance of RevokeUserSubscriptionResponseDto from a dict
revoke_user_subscription_response_dto_from_dict = RevokeUserSubscriptionResponseDto.from_dict(revoke_user_subscription_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


