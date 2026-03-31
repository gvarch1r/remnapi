# UpdateNodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**is_traffic_tracking_active** | **bool** |  | [optional] 
**traffic_limit_bytes** | **float** |  | [optional] 
**notify_percent** | **float** |  | [optional] 
**traffic_reset_day** | **float** |  | [optional] 
**country_code** | **str** |  | [optional] 
**consumption_multiplier** | **float** |  | [optional] 
**config_profile** | [**CreateNodeRequestDtoConfigProfile**](CreateNodeRequestDtoConfigProfile.md) |  | [optional] 
**provider_uuid** | **UUID** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**active_plugin_uuid** | **UUID** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_node_request_dto import UpdateNodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodeRequestDto from a JSON string
update_node_request_dto_instance = UpdateNodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateNodeRequestDto.to_json())

# convert the object into a dict
update_node_request_dto_dict = update_node_request_dto_instance.to_dict()
# create an instance of UpdateNodeRequestDto from a dict
update_node_request_dto_from_dict = UpdateNodeRequestDto.from_dict(update_node_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


