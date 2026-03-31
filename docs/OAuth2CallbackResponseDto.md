# OAuth2CallbackResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LoginResponseDtoResponse**](LoginResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.o_auth2_callback_response_dto import OAuth2CallbackResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2CallbackResponseDto from a JSON string
o_auth2_callback_response_dto_instance = OAuth2CallbackResponseDto.from_json(json)
# print the JSON string representation of the object
print(OAuth2CallbackResponseDto.to_json())

# convert the object into a dict
o_auth2_callback_response_dto_dict = o_auth2_callback_response_dto_instance.to_dict()
# create an instance of OAuth2CallbackResponseDto from a dict
o_auth2_callback_response_dto_from_dict = OAuth2CallbackResponseDto.from_dict(o_auth2_callback_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


