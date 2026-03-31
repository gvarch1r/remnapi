# GetInfraProvidersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInfraProvidersResponseDtoResponse**](GetInfraProvidersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_providers_response_dto import GetInfraProvidersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraProvidersResponseDto from a JSON string
get_infra_providers_response_dto_instance = GetInfraProvidersResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetInfraProvidersResponseDto.to_json())

# convert the object into a dict
get_infra_providers_response_dto_dict = get_infra_providers_response_dto_instance.to_dict()
# create an instance of GetInfraProvidersResponseDto from a dict
get_infra_providers_response_dto_from_dict = GetInfraProvidersResponseDto.from_dict(get_infra_providers_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


