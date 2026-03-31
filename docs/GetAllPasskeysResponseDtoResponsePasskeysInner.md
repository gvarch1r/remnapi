# GetAllPasskeysResponseDtoResponsePasskeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** | Created date. Format: 2025-01-17T15:38:45.065Z | 
**last_used_at** | **datetime** | Last used date. Format: 2025-01-17T15:38:45.065Z | 

## Example

```python
from supn_remnawave_panel.models.get_all_passkeys_response_dto_response_passkeys_inner import GetAllPasskeysResponseDtoResponsePasskeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPasskeysResponseDtoResponsePasskeysInner from a JSON string
get_all_passkeys_response_dto_response_passkeys_inner_instance = GetAllPasskeysResponseDtoResponsePasskeysInner.from_json(json)
# print the JSON string representation of the object
print(GetAllPasskeysResponseDtoResponsePasskeysInner.to_json())

# convert the object into a dict
get_all_passkeys_response_dto_response_passkeys_inner_dict = get_all_passkeys_response_dto_response_passkeys_inner_instance.to_dict()
# create an instance of GetAllPasskeysResponseDtoResponsePasskeysInner from a dict
get_all_passkeys_response_dto_response_passkeys_inner_from_dict = GetAllPasskeysResponseDtoResponsePasskeysInner.from_dict(get_all_passkeys_response_dto_response_passkeys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


