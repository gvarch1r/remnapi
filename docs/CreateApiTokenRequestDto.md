# CreateApiTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_name** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.create_api_token_request_dto import CreateApiTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiTokenRequestDto from a JSON string
create_api_token_request_dto_instance = CreateApiTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateApiTokenRequestDto.to_json())

# convert the object into a dict
create_api_token_request_dto_dict = create_api_token_request_dto_instance.to_dict()
# create an instance of CreateApiTokenRequestDto from a dict
create_api_token_request_dto_from_dict = CreateApiTokenRequestDto.from_dict(create_api_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


