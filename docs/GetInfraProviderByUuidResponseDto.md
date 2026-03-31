# GetInfraProviderByUuidResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInfraProvidersResponseDtoResponseProvidersInner**](GetInfraProvidersResponseDtoResponseProvidersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_provider_by_uuid_response_dto import GetInfraProviderByUuidResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraProviderByUuidResponseDto from a JSON string
get_infra_provider_by_uuid_response_dto_instance = GetInfraProviderByUuidResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetInfraProviderByUuidResponseDto.to_json())

# convert the object into a dict
get_infra_provider_by_uuid_response_dto_dict = get_infra_provider_by_uuid_response_dto_instance.to_dict()
# create an instance of GetInfraProviderByUuidResponseDto from a dict
get_infra_provider_by_uuid_response_dto_from_dict = GetInfraProviderByUuidResponseDto.from_dict(get_infra_provider_by_uuid_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


