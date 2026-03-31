# FindAllApiTokensResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[FindAllApiTokensResponseDtoResponseApiKeysInner]**](FindAllApiTokensResponseDtoResponseApiKeysInner.md) |  | 
**docs** | [**FindAllApiTokensResponseDtoResponseDocs**](FindAllApiTokensResponseDtoResponseDocs.md) |  | 

## Example

```python
from supn_remnawave_panel.models.find_all_api_tokens_response_dto_response import FindAllApiTokensResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindAllApiTokensResponseDtoResponse from a JSON string
find_all_api_tokens_response_dto_response_instance = FindAllApiTokensResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(FindAllApiTokensResponseDtoResponse.to_json())

# convert the object into a dict
find_all_api_tokens_response_dto_response_dict = find_all_api_tokens_response_dto_response_instance.to_dict()
# create an instance of FindAllApiTokensResponseDtoResponse from a dict
find_all_api_tokens_response_dto_response_from_dict = FindAllApiTokensResponseDtoResponse.from_dict(find_all_api_tokens_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


