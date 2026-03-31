# BulkRevokeUsersSubscriptionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_revoke_users_subscription_request_dto import BulkRevokeUsersSubscriptionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRevokeUsersSubscriptionRequestDto from a JSON string
bulk_revoke_users_subscription_request_dto_instance = BulkRevokeUsersSubscriptionRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkRevokeUsersSubscriptionRequestDto.to_json())

# convert the object into a dict
bulk_revoke_users_subscription_request_dto_dict = bulk_revoke_users_subscription_request_dto_instance.to_dict()
# create an instance of BulkRevokeUsersSubscriptionRequestDto from a dict
bulk_revoke_users_subscription_request_dto_from_dict = BulkRevokeUsersSubscriptionRequestDto.from_dict(bulk_revoke_users_subscription_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


