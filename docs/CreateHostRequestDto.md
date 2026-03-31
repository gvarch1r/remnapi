# CreateHostRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | [**CreateHostRequestDtoInbound**](CreateHostRequestDtoInbound.md) |  | 
**remark** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | 
**path** | **str** |  | [optional] 
**sni** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**alpn** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] [default to False]
**security_layer** | **str** |  | [optional] [default to 'DEFAULT']
**x_http_extra_params** | **object** |  | [optional] 
**mux_params** | **object** |  | [optional] 
**sockopt_params** | **object** |  | [optional] 
**final_mask** | **object** |  | [optional] 
**server_description** | **str** |  | [optional] 
**tag** | **str** | Optional. Host tag for categorization. Max 32 characters, uppercase letters, numbers, underscores and colons are allowed. | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**override_sni_from_address** | **bool** |  | [optional] [default to False]
**keep_sni_blank** | **bool** |  | [optional] [default to False]
**allow_insecure** | **bool** |  | [optional] [default to False]
**vless_route_id** | **int** |  | [optional] 
**shuffle_host** | **bool** |  | [optional] [default to False]
**mihomo_x25519** | **bool** |  | [optional] [default to False]
**nodes** | **List[UUID]** |  | [optional] 
**xray_json_template_uuid** | **UUID** |  | [optional] 
**excluded_internal_squads** | **List[UUID]** | Optional. Internal squads from which the host will be excluded. | [optional] 
**exclude_from_subscription_types** | **List[str]** | Optional. Subscription types from which the host will be excluded from. | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_host_request_dto import CreateHostRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostRequestDto from a JSON string
create_host_request_dto_instance = CreateHostRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateHostRequestDto.to_json())

# convert the object into a dict
create_host_request_dto_dict = create_host_request_dto_instance.to_dict()
# create an instance of CreateHostRequestDto from a dict
create_host_request_dto_from_dict = CreateHostRequestDto.from_dict(create_host_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


