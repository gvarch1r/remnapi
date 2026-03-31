# UpdateHostRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**inbound** | [**CreateHostRequestDtoInbound**](CreateHostRequestDtoInbound.md) |  | [optional] 
**remark** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**sni** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**alpn** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**security_layer** | **str** |  | [optional] 
**x_http_extra_params** | **object** |  | [optional] 
**mux_params** | **object** |  | [optional] 
**sockopt_params** | **object** |  | [optional] 
**final_mask** | **object** |  | [optional] 
**server_description** | **str** |  | [optional] 
**tag** | **str** | Optional. Host tag for categorization. Max 32 characters, uppercase letters, numbers, underscores and colons are allowed. | [optional] 
**is_hidden** | **bool** |  | [optional] 
**override_sni_from_address** | **bool** |  | [optional] 
**keep_sni_blank** | **bool** |  | [optional] 
**vless_route_id** | **int** |  | [optional] 
**allow_insecure** | **bool** |  | [optional] 
**shuffle_host** | **bool** |  | [optional] 
**mihomo_x25519** | **bool** |  | [optional] 
**nodes** | **List[UUID]** |  | [optional] 
**xray_json_template_uuid** | **UUID** |  | [optional] 
**excluded_internal_squads** | **List[UUID]** | Optional. Internal squads from which the host will be excluded. | [optional] 
**exclude_from_subscription_types** | **List[str]** | Optional. Subscription types from which the host will be excluded from. | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_host_request_dto import UpdateHostRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostRequestDto from a JSON string
update_host_request_dto_instance = UpdateHostRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateHostRequestDto.to_json())

# convert the object into a dict
update_host_request_dto_dict = update_host_request_dto_instance.to_dict()
# create an instance of UpdateHostRequestDto from a dict
update_host_request_dto_from_dict = UpdateHostRequestDto.from_dict(update_host_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


