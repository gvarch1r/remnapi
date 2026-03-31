# CreateInfraProviderResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInfraProvidersResponseDtoResponseProvidersInner**](GetInfraProvidersResponseDtoResponseProvidersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_infra_provider_response_dto import CreateInfraProviderResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraProviderResponseDto from a JSON string
create_infra_provider_response_dto_instance = CreateInfraProviderResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateInfraProviderResponseDto.to_json())

# convert the object into a dict
create_infra_provider_response_dto_dict = create_infra_provider_response_dto_instance.to_dict()
# create an instance of CreateInfraProviderResponseDto from a dict
create_infra_provider_response_dto_from_dict = CreateInfraProviderResponseDto.from_dict(create_infra_provider_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


