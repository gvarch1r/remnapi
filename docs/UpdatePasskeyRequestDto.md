# UpdatePasskeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.update_passkey_request_dto import UpdatePasskeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasskeyRequestDto from a JSON string
update_passkey_request_dto_instance = UpdatePasskeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePasskeyRequestDto.to_json())

# convert the object into a dict
update_passkey_request_dto_dict = update_passkey_request_dto_instance.to_dict()
# create an instance of UpdatePasskeyRequestDto from a dict
update_passkey_request_dto_from_dict = UpdatePasskeyRequestDto.from_dict(update_passkey_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


