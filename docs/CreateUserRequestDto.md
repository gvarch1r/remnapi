# CreateUserRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Unique username for the user. Required. Must be 3-36 characters long and contain only letters, numbers, underscores and dashes. | 
**status** | **str** | Optional. User account status. Defaults to ACTIVE. | [optional] [default to 'ACTIVE']
**short_uuid** | **str** | Optional. Short UUID identifier for the user. | [optional] 
**trojan_password** | **str** | Optional. Password for Trojan protocol. Must be 8-32 characters. | [optional] 
**vless_uuid** | **UUID** | Optional. UUID for VLESS protocol. Must be a valid UUID format. | [optional] 
**ss_password** | **str** | Optional. Password for Shadowsocks protocol. Must be 8-32 characters. | [optional] 
**traffic_limit_bytes** | **int** | Optional. Traffic limit in bytes. Set to 0 for unlimited traffic. | [optional] 
**traffic_limit_strategy** | **str** | Available reset periods | [optional] [default to 'NO_RESET']
**expire_at** | **datetime** | Account expiration date. Required. Format: 2025-01-17T15:38:45.065Z | 
**created_at** | **datetime** | Optional. Account creation date. Format: 2025-01-17T15:38:45.065Z | [optional] 
**last_traffic_reset_at** | **datetime** | Optional. Date of last traffic reset. Format: 2025-01-17T15:38:45.065Z | [optional] 
**description** | **str** | Optional. Additional notes or description for the user account. | [optional] 
**tag** | **str** | Optional. User tag for categorization. Max 16 characters, uppercase letters, numbers and underscores only. | [optional] 
**telegram_id** | **int** | Optional. Telegram user ID for notifications. Must be an integer. | [optional] 
**email** | **str** | Optional. User email address. Must be a valid email format. | [optional] 
**hwid_device_limit** | **int** | Optional. Maximum number of hardware devices allowed. Must be a positive integer. | [optional] 
**active_internal_squads** | **List[UUID]** | Optional. Array of UUIDs representing enabled internal squads. | [optional] 
**uuid** | **UUID** | Optional. Pass UUID to create user with specific UUID, otherwise it will be generated automatically. | [optional] 
**external_squad_uuid** | **UUID** | Optional. External squad UUID. | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_user_request_dto import CreateUserRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestDto from a JSON string
create_user_request_dto_instance = CreateUserRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequestDto.to_json())

# convert the object into a dict
create_user_request_dto_dict = create_user_request_dto_instance.to_dict()
# create an instance of CreateUserRequestDto from a dict
create_user_request_dto_from_dict = CreateUserRequestDto.from_dict(create_user_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


