# FindAllApiTokensResponseDtoResponseApiKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**token** | **str** |  | 
**token_name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.find_all_api_tokens_response_dto_response_api_keys_inner import FindAllApiTokensResponseDtoResponseApiKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of FindAllApiTokensResponseDtoResponseApiKeysInner from a JSON string
find_all_api_tokens_response_dto_response_api_keys_inner_instance = FindAllApiTokensResponseDtoResponseApiKeysInner.from_json(json)
# print the JSON string representation of the object
print(FindAllApiTokensResponseDtoResponseApiKeysInner.to_json())

# convert the object into a dict
find_all_api_tokens_response_dto_response_api_keys_inner_dict = find_all_api_tokens_response_dto_response_api_keys_inner_instance.to_dict()
# create an instance of FindAllApiTokensResponseDtoResponseApiKeysInner from a dict
find_all_api_tokens_response_dto_response_api_keys_inner_from_dict = FindAllApiTokensResponseDtoResponseApiKeysInner.from_dict(find_all_api_tokens_response_dto_response_api_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


