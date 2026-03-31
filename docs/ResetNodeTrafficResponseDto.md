# ResetNodeTrafficResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reset_node_traffic_response_dto import ResetNodeTrafficResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResetNodeTrafficResponseDto from a JSON string
reset_node_traffic_response_dto_instance = ResetNodeTrafficResponseDto.from_json(json)
# print the JSON string representation of the object
print(ResetNodeTrafficResponseDto.to_json())

# convert the object into a dict
reset_node_traffic_response_dto_dict = reset_node_traffic_response_dto_instance.to_dict()
# create an instance of ResetNodeTrafficResponseDto from a dict
reset_node_traffic_response_dto_from_dict = ResetNodeTrafficResponseDto.from_dict(reset_node_traffic_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


