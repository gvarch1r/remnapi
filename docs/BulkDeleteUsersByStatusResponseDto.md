# BulkDeleteUsersByStatusResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_delete_users_by_status_response_dto import BulkDeleteUsersByStatusResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteUsersByStatusResponseDto from a JSON string
bulk_delete_users_by_status_response_dto_instance = BulkDeleteUsersByStatusResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteUsersByStatusResponseDto.to_json())

# convert the object into a dict
bulk_delete_users_by_status_response_dto_dict = bulk_delete_users_by_status_response_dto_instance.to_dict()
# create an instance of BulkDeleteUsersByStatusResponseDto from a dict
bulk_delete_users_by_status_response_dto_from_dict = BulkDeleteUsersByStatusResponseDto.from_dict(bulk_delete_users_by_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


