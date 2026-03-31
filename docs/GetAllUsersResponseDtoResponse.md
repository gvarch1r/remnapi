# GetAllUsersResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[CreateUserResponseDtoResponse]**](CreateUserResponseDtoResponse.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_users_response_dto_response import GetAllUsersResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllUsersResponseDtoResponse from a JSON string
get_all_users_response_dto_response_instance = GetAllUsersResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllUsersResponseDtoResponse.to_json())

# convert the object into a dict
get_all_users_response_dto_response_dict = get_all_users_response_dto_response_instance.to_dict()
# create an instance of GetAllUsersResponseDtoResponse from a dict
get_all_users_response_dto_response_from_dict = GetAllUsersResponseDtoResponse.from_dict(get_all_users_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


