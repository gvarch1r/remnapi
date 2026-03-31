# GetOneHostResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateHostResponseDtoResponse**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_one_host_response_dto import GetOneHostResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetOneHostResponseDto from a JSON string
get_one_host_response_dto_instance = GetOneHostResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetOneHostResponseDto.to_json())

# convert the object into a dict
get_one_host_response_dto_dict = get_one_host_response_dto_instance.to_dict()
# create an instance of GetOneHostResponseDto from a dict
get_one_host_response_dto_from_dict = GetOneHostResponseDto.from_dict(get_one_host_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


