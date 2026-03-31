# BulkResetTrafficUsersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_reset_traffic_users_response_dto import BulkResetTrafficUsersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResetTrafficUsersResponseDto from a JSON string
bulk_reset_traffic_users_response_dto_instance = BulkResetTrafficUsersResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkResetTrafficUsersResponseDto.to_json())

# convert the object into a dict
bulk_reset_traffic_users_response_dto_dict = bulk_reset_traffic_users_response_dto_instance.to_dict()
# create an instance of BulkResetTrafficUsersResponseDto from a dict
bulk_reset_traffic_users_response_dto_from_dict = BulkResetTrafficUsersResponseDto.from_dict(bulk_reset_traffic_users_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


