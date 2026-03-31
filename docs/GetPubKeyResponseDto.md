# GetPubKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetPubKeyResponseDtoResponse**](GetPubKeyResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_pub_key_response_dto import GetPubKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetPubKeyResponseDto from a JSON string
get_pub_key_response_dto_instance = GetPubKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetPubKeyResponseDto.to_json())

# convert the object into a dict
get_pub_key_response_dto_dict = get_pub_key_response_dto_instance.to_dict()
# create an instance of GetPubKeyResponseDto from a dict
get_pub_key_response_dto_from_dict = GetPubKeyResponseDto.from_dict(get_pub_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


