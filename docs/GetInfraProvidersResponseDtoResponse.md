# GetInfraProvidersResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**providers** | [**List[GetInfraProvidersResponseDtoResponseProvidersInner]**](GetInfraProvidersResponseDtoResponseProvidersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_providers_response_dto_response import GetInfraProvidersResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraProvidersResponseDtoResponse from a JSON string
get_infra_providers_response_dto_response_instance = GetInfraProvidersResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetInfraProvidersResponseDtoResponse.to_json())

# convert the object into a dict
get_infra_providers_response_dto_response_dict = get_infra_providers_response_dto_response_instance.to_dict()
# create an instance of GetInfraProvidersResponseDtoResponse from a dict
get_infra_providers_response_dto_response_from_dict = GetInfraProvidersResponseDtoResponse.from_dict(get_infra_providers_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


