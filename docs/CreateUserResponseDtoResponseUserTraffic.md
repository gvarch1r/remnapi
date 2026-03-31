# CreateUserResponseDtoResponseUserTraffic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_traffic_bytes** | **float** |  | 
**lifetime_used_traffic_bytes** | **float** |  | 
**online_at** | **datetime** |  | 
**first_connected_at** | **datetime** |  | 
**last_connected_node_uuid** | **UUID** |  | 

## Example

```python
from supn_remnawave_panel.models.create_user_response_dto_response_user_traffic import CreateUserResponseDtoResponseUserTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserResponseDtoResponseUserTraffic from a JSON string
create_user_response_dto_response_user_traffic_instance = CreateUserResponseDtoResponseUserTraffic.from_json(json)
# print the JSON string representation of the object
print(CreateUserResponseDtoResponseUserTraffic.to_json())

# convert the object into a dict
create_user_response_dto_response_user_traffic_dict = create_user_response_dto_response_user_traffic_instance.to_dict()
# create an instance of CreateUserResponseDtoResponseUserTraffic from a dict
create_user_response_dto_response_user_traffic_from_dict = CreateUserResponseDtoResponseUserTraffic.from_dict(create_user_response_dto_response_user_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


