# BulkUpdateUsersRequestDtoFields


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
**external_squad_uuid** | **UUID** | Optional. External squad UUID. | [optional] 

## Example

```python
from supn_remnawave_panel.models.bulk_update_users_request_dto_fields import BulkUpdateUsersRequestDtoFields

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateUsersRequestDtoFields from a JSON string
bulk_update_users_request_dto_fields_instance = BulkUpdateUsersRequestDtoFields.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateUsersRequestDtoFields.to_json())

# convert the object into a dict
bulk_update_users_request_dto_fields_dict = bulk_update_users_request_dto_fields_instance.to_dict()
# create an instance of BulkUpdateUsersRequestDtoFields from a dict
bulk_update_users_request_dto_fields_from_dict = BulkUpdateUsersRequestDtoFields.from_dict(bulk_update_users_request_dto_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


