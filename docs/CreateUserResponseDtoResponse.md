# CreateUserResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**id** | **float** |  | 
**short_uuid** | **str** |  | 
**username** | **str** |  | 
**status** | **str** |  | [optional] [default to 'ACTIVE']
**traffic_limit_bytes** | **int** |  | [optional] [default to 0]
**traffic_limit_strategy** | **str** | Available reset periods | [optional] [default to 'NO_RESET']
**expire_at** | **datetime** |  | 
**telegram_id** | **int** |  | 
**email** | **str** |  | 
**description** | **str** |  | 
**tag** | **str** |  | 
**hwid_device_limit** | **int** |  | 
**external_squad_uuid** | **UUID** |  | 
**trojan_password** | **str** |  | 
**vless_uuid** | **UUID** |  | 
**ss_password** | **str** |  | 
**last_triggered_threshold** | **int** |  | [optional] [default to 0]
**sub_revoked_at** | **datetime** |  | 
**last_traffic_reset_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**subscription_url** | **str** |  | 
**active_internal_squads** | [**List[CreateUserResponseDtoResponseActiveInternalSquadsInner]**](CreateUserResponseDtoResponseActiveInternalSquadsInner.md) |  | 
**user_traffic** | [**CreateUserResponseDtoResponseUserTraffic**](CreateUserResponseDtoResponseUserTraffic.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_user_response_dto_response import CreateUserResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserResponseDtoResponse from a JSON string
create_user_response_dto_response_instance = CreateUserResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserResponseDtoResponse.to_json())

# convert the object into a dict
create_user_response_dto_response_dict = create_user_response_dto_response_instance.to_dict()
# create an instance of CreateUserResponseDtoResponse from a dict
create_user_response_dto_response_from_dict = CreateUserResponseDtoResponse.from_dict(create_user_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


