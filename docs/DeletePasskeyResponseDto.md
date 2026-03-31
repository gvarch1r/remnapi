# DeletePasskeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetAllPasskeysResponseDtoResponse**](GetAllPasskeysResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_passkey_response_dto import DeletePasskeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePasskeyResponseDto from a JSON string
delete_passkey_response_dto_instance = DeletePasskeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeletePasskeyResponseDto.to_json())

# convert the object into a dict
delete_passkey_response_dto_dict = delete_passkey_response_dto_instance.to_dict()
# create an instance of DeletePasskeyResponseDto from a dict
delete_passkey_response_dto_from_dict = DeletePasskeyResponseDto.from_dict(delete_passkey_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


