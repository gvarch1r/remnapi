# UpdateInfraProviderResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInfraProvidersResponseDtoResponseProvidersInner**](GetInfraProvidersResponseDtoResponseProvidersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_infra_provider_response_dto import UpdateInfraProviderResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfraProviderResponseDto from a JSON string
update_infra_provider_response_dto_instance = UpdateInfraProviderResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInfraProviderResponseDto.to_json())

# convert the object into a dict
update_infra_provider_response_dto_dict = update_infra_provider_response_dto_instance.to_dict()
# create an instance of UpdateInfraProviderResponseDto from a dict
update_infra_provider_response_dto_from_dict = UpdateInfraProviderResponseDto.from_dict(update_infra_provider_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


