# GetAllPasskeysResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passkeys** | [**List[GetAllPasskeysResponseDtoResponsePasskeysInner]**](GetAllPasskeysResponseDtoResponsePasskeysInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_passkeys_response_dto_response import GetAllPasskeysResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPasskeysResponseDtoResponse from a JSON string
get_all_passkeys_response_dto_response_instance = GetAllPasskeysResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllPasskeysResponseDtoResponse.to_json())

# convert the object into a dict
get_all_passkeys_response_dto_response_dict = get_all_passkeys_response_dto_response_instance.to_dict()
# create an instance of GetAllPasskeysResponseDtoResponse from a dict
get_all_passkeys_response_dto_response_from_dict = GetAllPasskeysResponseDtoResponse.from_dict(get_all_passkeys_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


