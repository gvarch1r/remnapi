# UpdatePasskeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetAllPasskeysResponseDtoResponse**](GetAllPasskeysResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_passkey_response_dto import UpdatePasskeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasskeyResponseDto from a JSON string
update_passkey_response_dto_instance = UpdatePasskeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePasskeyResponseDto.to_json())

# convert the object into a dict
update_passkey_response_dto_dict = update_passkey_response_dto_instance.to_dict()
# create an instance of UpdatePasskeyResponseDto from a dict
update_passkey_response_dto_from_dict = UpdatePasskeyResponseDto.from_dict(update_passkey_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


