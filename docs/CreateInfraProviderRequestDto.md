# CreateInfraProviderRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**favicon_link** | **str** |  | [optional] 
**login_url** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_infra_provider_request_dto import CreateInfraProviderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraProviderRequestDto from a JSON string
create_infra_provider_request_dto_instance = CreateInfraProviderRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateInfraProviderRequestDto.to_json())

# convert the object into a dict
create_infra_provider_request_dto_dict = create_infra_provider_request_dto_instance.to_dict()
# create an instance of CreateInfraProviderRequestDto from a dict
create_infra_provider_request_dto_from_dict = CreateInfraProviderRequestDto.from_dict(create_infra_provider_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


