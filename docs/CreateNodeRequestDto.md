# CreateNodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | [optional] 
**is_traffic_tracking_active** | **bool** |  | [optional] [default to False]
**traffic_limit_bytes** | **int** |  | [optional] 
**notify_percent** | **int** |  | [optional] 
**traffic_reset_day** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] [default to 'XX']
**consumption_multiplier** | **float** |  | [optional] 
**config_profile** | [**CreateNodeRequestDtoConfigProfile**](CreateNodeRequestDtoConfigProfile.md) |  | 
**provider_uuid** | **UUID** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**active_plugin_uuid** | **UUID** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_node_request_dto import CreateNodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeRequestDto from a JSON string
create_node_request_dto_instance = CreateNodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateNodeRequestDto.to_json())

# convert the object into a dict
create_node_request_dto_dict = create_node_request_dto_instance.to_dict()
# create an instance of CreateNodeRequestDto from a dict
create_node_request_dto_from_dict = CreateNodeRequestDto.from_dict(create_node_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


