# BulkRevokeUsersSubscriptionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_revoke_users_subscription_response_dto import BulkRevokeUsersSubscriptionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRevokeUsersSubscriptionResponseDto from a JSON string
bulk_revoke_users_subscription_response_dto_instance = BulkRevokeUsersSubscriptionResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkRevokeUsersSubscriptionResponseDto.to_json())

# convert the object into a dict
bulk_revoke_users_subscription_response_dto_dict = bulk_revoke_users_subscription_response_dto_instance.to_dict()
# create an instance of BulkRevokeUsersSubscriptionResponseDto from a dict
bulk_revoke_users_subscription_response_dto_from_dict = BulkRevokeUsersSubscriptionResponseDto.from_dict(bulk_revoke_users_subscription_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


