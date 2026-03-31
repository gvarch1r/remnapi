# CreateNodeResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | 
**is_connected** | **bool** |  | 
**is_disabled** | **bool** |  | 
**is_connecting** | **bool** |  | 
**last_status_change** | **datetime** |  | 
**last_status_message** | **str** |  | 
**is_traffic_tracking_active** | **bool** |  | 
**traffic_reset_day** | **int** |  | 
**traffic_limit_bytes** | **float** |  | 
**traffic_used_bytes** | **float** |  | 
**notify_percent** | **int** |  | 
**view_position** | **int** |  | 
**country_code** | **str** |  | 
**consumption_multiplier** | **float** |  | 
**tags** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**config_profile** | [**CreateNodeResponseDtoResponseConfigProfile**](CreateNodeResponseDtoResponseConfigProfile.md) |  | 
**provider_uuid** | **UUID** |  | 
**provider** | [**CreateNodeResponseDtoResponseProvider**](CreateNodeResponseDtoResponseProvider.md) |  | 
**active_plugin_uuid** | **UUID** |  | 
**system** | [**CreateNodeResponseDtoResponseSystem**](CreateNodeResponseDtoResponseSystem.md) |  | 
**versions** | [**CreateNodeResponseDtoResponseVersions**](CreateNodeResponseDtoResponseVersions.md) |  | 
**xray_uptime** | **float** |  | 
**users_online** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response import CreateNodeResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponse from a JSON string
create_node_response_dto_response_instance = CreateNodeResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponse.to_json())

# convert the object into a dict
create_node_response_dto_response_dict = create_node_response_dto_response_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponse from a dict
create_node_response_dto_response_from_dict = CreateNodeResponseDtoResponse.from_dict(create_node_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


