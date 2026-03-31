# DeleteUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_user_response_dto import DeleteUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserResponseDto from a JSON string
delete_user_response_dto_instance = DeleteUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteUserResponseDto.to_json())

# convert the object into a dict
delete_user_response_dto_dict = delete_user_response_dto_instance.to_dict()
# create an instance of DeleteUserResponseDto from a dict
delete_user_response_dto_from_dict = DeleteUserResponseDto.from_dict(delete_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


