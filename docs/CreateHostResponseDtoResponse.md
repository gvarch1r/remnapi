# CreateHostResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**remark** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | 
**path** | **str** |  | 
**sni** | **str** |  | 
**host** | **str** |  | 
**alpn** | **str** |  | 
**fingerprint** | **str** |  | 
**is_disabled** | **bool** |  | [optional] [default to False]
**security_layer** | **str** |  | [optional] [default to 'DEFAULT']
**x_http_extra_params** | **object** |  | 
**mux_params** | **object** |  | 
**sockopt_params** | **object** |  | 
**final_mask** | **object** |  | 
**inbound** | [**CreateHostResponseDtoResponseInbound**](CreateHostResponseDtoResponseInbound.md) |  | 
**server_description** | **str** |  | 
**tag** | **str** |  | 
**is_hidden** | **bool** |  | [optional] [default to False]
**override_sni_from_address** | **bool** |  | [optional] [default to False]
**keep_sni_blank** | **bool** |  | [optional] [default to False]
**vless_route_id** | **int** |  | 
**allow_insecure** | **bool** |  | [optional] [default to False]
**shuffle_host** | **bool** |  | 
**mihomo_x25519** | **bool** |  | 
**nodes** | **List[UUID]** |  | 
**xray_json_template_uuid** | **UUID** |  | 
**excluded_internal_squads** | **List[UUID]** |  | 
**exclude_from_subscription_types** | **List[str]** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_host_response_dto_response import CreateHostResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostResponseDtoResponse from a JSON string
create_host_response_dto_response_instance = CreateHostResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHostResponseDtoResponse.to_json())

# convert the object into a dict
create_host_response_dto_response_dict = create_host_response_dto_response_instance.to_dict()
# create an instance of CreateHostResponseDtoResponse from a dict
create_host_response_dto_response_from_dict = CreateHostResponseDtoResponse.from_dict(create_host_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


