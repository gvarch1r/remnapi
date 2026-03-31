# BulkAllUpdateUsersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_all_update_users_response_dto import BulkAllUpdateUsersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAllUpdateUsersResponseDto from a JSON string
bulk_all_update_users_response_dto_instance = BulkAllUpdateUsersResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkAllUpdateUsersResponseDto.to_json())

# convert the object into a dict
bulk_all_update_users_response_dto_dict = bulk_all_update_users_response_dto_instance.to_dict()
# create an instance of BulkAllUpdateUsersResponseDto from a dict
bulk_all_update_users_response_dto_from_dict = BulkAllUpdateUsersResponseDto.from_dict(bulk_all_update_users_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


