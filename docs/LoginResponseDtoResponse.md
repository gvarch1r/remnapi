# LoginResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.login_response_dto_response import LoginResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponseDtoResponse from a JSON string
login_response_dto_response_instance = LoginResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(LoginResponseDtoResponse.to_json())

# convert the object into a dict
login_response_dto_response_dict = login_response_dto_response_instance.to_dict()
# create an instance of LoginResponseDtoResponse from a dict
login_response_dto_response_from_dict = LoginResponseDtoResponse.from_dict(login_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


