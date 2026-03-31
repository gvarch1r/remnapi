# GetTemplatesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetTemplatesResponseDtoResponse**](GetTemplatesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_templates_response_dto import GetTemplatesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesResponseDto from a JSON string
get_templates_response_dto_instance = GetTemplatesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetTemplatesResponseDto.to_json())

# convert the object into a dict
get_templates_response_dto_dict = get_templates_response_dto_instance.to_dict()
# create an instance of GetTemplatesResponseDto from a dict
get_templates_response_dto_from_dict = GetTemplatesResponseDto.from_dict(get_templates_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


