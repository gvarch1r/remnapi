# UpdateInfraProviderRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**favicon_link** | **str** |  | [optional] 
**login_url** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_infra_provider_request_dto import UpdateInfraProviderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfraProviderRequestDto from a JSON string
update_infra_provider_request_dto_instance = UpdateInfraProviderRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInfraProviderRequestDto.to_json())

# convert the object into a dict
update_infra_provider_request_dto_dict = update_infra_provider_request_dto_instance.to_dict()
# create an instance of UpdateInfraProviderRequestDto from a dict
update_infra_provider_request_dto_from_dict = UpdateInfraProviderRequestDto.from_dict(update_infra_provider_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


