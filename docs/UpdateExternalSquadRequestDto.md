# UpdateExternalSquadRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**templates** | [**List[GetExternalSquadsResponseDtoResponseExternalSquadsInnerTemplatesInner]**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerTemplatesInner.md) |  | [optional] 
**subscription_settings** | [**UpdateExternalSquadRequestDtoSubscriptionSettings**](UpdateExternalSquadRequestDtoSubscriptionSettings.md) |  | [optional] 
**host_overrides** | [**UpdateExternalSquadRequestDtoHostOverrides**](UpdateExternalSquadRequestDtoHostOverrides.md) |  | [optional] 
**response_headers** | **Dict[str, str]** |  | [optional] 
**hwid_settings** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings.md) |  | [optional] 
**custom_remarks** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks.md) |  | [optional] 
**subpage_config_uuid** | **UUID** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_external_squad_request_dto import UpdateExternalSquadRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalSquadRequestDto from a JSON string
update_external_squad_request_dto_instance = UpdateExternalSquadRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalSquadRequestDto.to_json())

# convert the object into a dict
update_external_squad_request_dto_dict = update_external_squad_request_dto_instance.to_dict()
# create an instance of UpdateExternalSquadRequestDto from a dict
update_external_squad_request_dto_from_dict = UpdateExternalSquadRequestDto.from_dict(update_external_squad_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


