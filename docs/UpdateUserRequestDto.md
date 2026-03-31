# UpdateUserRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username of the user | [optional] 
**uuid** | **UUID** | UUID of the user. UUID has higher priority than username, so if both are provided, username will be ignored. | [optional] 
**status** | **str** |  | [optional] 
**traffic_limit_bytes** | **int** | Traffic limit in bytes. 0 - unlimited | [optional] 
**traffic_limit_strategy** | **str** | Available reset periods | [optional] [default to 'NO_RESET']
**expire_at** | **datetime** | Expiration date: 2025-01-17T15:38:45.065Z | [optional] 
**description** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**telegram_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**hwid_device_limit** | **int** |  | [optional] 
**active_internal_squads** | **List[UUID]** |  | [optional] 
**external_squad_uuid** | **UUID** | Optional. External squad UUID. | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_user_request_dto import UpdateUserRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestDto from a JSON string
update_user_request_dto_instance = UpdateUserRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestDto.to_json())

# convert the object into a dict
update_user_request_dto_dict = update_user_request_dto_instance.to_dict()
# create an instance of UpdateUserRequestDto from a dict
update_user_request_dto_from_dict = UpdateUserRequestDto.from_dict(update_user_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


