# GetExternalSquadsResponseDtoResponseExternalSquadsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**info** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerInfo**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerInfo.md) |  | 
**templates** | [**List[GetExternalSquadsResponseDtoResponseExternalSquadsInnerTemplatesInner]**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerTemplatesInner.md) |  | 
**subscription_settings** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings.md) |  | 
**host_overrides** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerHostOverrides**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerHostOverrides.md) |  | 
**response_headers** | **Dict[str, str]** |  | 
**hwid_settings** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings.md) |  | 
**custom_remarks** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks.md) |  | 
**subpage_config_uuid** | **UUID** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_external_squads_response_dto_response_external_squads_inner import GetExternalSquadsResponseDtoResponseExternalSquadsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInner from a JSON string
get_external_squads_response_dto_response_external_squads_inner_instance = GetExternalSquadsResponseDtoResponseExternalSquadsInner.from_json(json)
# print the JSON string representation of the object
print(GetExternalSquadsResponseDtoResponseExternalSquadsInner.to_json())

# convert the object into a dict
get_external_squads_response_dto_response_external_squads_inner_dict = get_external_squads_response_dto_response_external_squads_inner_instance.to_dict()
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInner from a dict
get_external_squads_response_dto_response_external_squads_inner_from_dict = GetExternalSquadsResponseDtoResponseExternalSquadsInner.from_dict(get_external_squads_response_dto_response_external_squads_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


