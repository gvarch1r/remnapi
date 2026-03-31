# VerifyPasskeyRegistrationResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**VerifyPasskeyRegistrationResponseDtoResponse**](VerifyPasskeyRegistrationResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.verify_passkey_registration_response_dto import VerifyPasskeyRegistrationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPasskeyRegistrationResponseDto from a JSON string
verify_passkey_registration_response_dto_instance = VerifyPasskeyRegistrationResponseDto.from_json(json)
# print the JSON string representation of the object
print(VerifyPasskeyRegistrationResponseDto.to_json())

# convert the object into a dict
verify_passkey_registration_response_dto_dict = verify_passkey_registration_response_dto_instance.to_dict()
# create an instance of VerifyPasskeyRegistrationResponseDto from a dict
verify_passkey_registration_response_dto_from_dict = VerifyPasskeyRegistrationResponseDto.from_dict(verify_passkey_registration_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


