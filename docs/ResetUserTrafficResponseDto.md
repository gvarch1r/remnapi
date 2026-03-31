# ResetUserTrafficResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reset_user_traffic_response_dto import ResetUserTrafficResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResetUserTrafficResponseDto from a JSON string
reset_user_traffic_response_dto_instance = ResetUserTrafficResponseDto.from_json(json)
# print the JSON string representation of the object
print(ResetUserTrafficResponseDto.to_json())

# convert the object into a dict
reset_user_traffic_response_dto_dict = reset_user_traffic_response_dto_instance.to_dict()
# create an instance of ResetUserTrafficResponseDto from a dict
reset_user_traffic_response_dto_from_dict = ResetUserTrafficResponseDto.from_dict(reset_user_traffic_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


