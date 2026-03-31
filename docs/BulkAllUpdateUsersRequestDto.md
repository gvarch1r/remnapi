# BulkAllUpdateUsersRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ACTIVE']
**traffic_limit_bytes** | **int** | Traffic limit in bytes. 0 - unlimited | [optional] 
**traffic_limit_strategy** | **str** | Traffic limit reset strategy | [optional] 
**expire_at** | **datetime** | Expiration date: 2025-01-17T15:38:45.065Z | [optional] 
**description** | **str** |  | [optional] 
**telegram_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**hwid_device_limit** | **int** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.bulk_all_update_users_request_dto import BulkAllUpdateUsersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAllUpdateUsersRequestDto from a JSON string
bulk_all_update_users_request_dto_instance = BulkAllUpdateUsersRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkAllUpdateUsersRequestDto.to_json())

# convert the object into a dict
bulk_all_update_users_request_dto_dict = bulk_all_update_users_request_dto_instance.to_dict()
# create an instance of BulkAllUpdateUsersRequestDto from a dict
bulk_all_update_users_request_dto_from_dict = BulkAllUpdateUsersRequestDto.from_dict(bulk_all_update_users_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


