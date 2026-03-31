# BulkResetTrafficUsersRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_reset_traffic_users_request_dto import BulkResetTrafficUsersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResetTrafficUsersRequestDto from a JSON string
bulk_reset_traffic_users_request_dto_instance = BulkResetTrafficUsersRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkResetTrafficUsersRequestDto.to_json())

# convert the object into a dict
bulk_reset_traffic_users_request_dto_dict = bulk_reset_traffic_users_request_dto_instance.to_dict()
# create an instance of BulkResetTrafficUsersRequestDto from a dict
bulk_reset_traffic_users_request_dto_from_dict = BulkResetTrafficUsersRequestDto.from_dict(bulk_reset_traffic_users_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


