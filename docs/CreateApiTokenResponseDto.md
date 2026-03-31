# CreateApiTokenResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateApiTokenResponseDtoResponse**](CreateApiTokenResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_api_token_response_dto import CreateApiTokenResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiTokenResponseDto from a JSON string
create_api_token_response_dto_instance = CreateApiTokenResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateApiTokenResponseDto.to_json())

# convert the object into a dict
create_api_token_response_dto_dict = create_api_token_response_dto_instance.to_dict()
# create an instance of CreateApiTokenResponseDto from a dict
create_api_token_response_dto_from_dict = CreateApiTokenResponseDto.from_dict(create_api_token_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


