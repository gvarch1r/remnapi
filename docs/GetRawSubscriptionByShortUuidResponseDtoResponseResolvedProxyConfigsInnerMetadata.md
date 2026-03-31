# GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**tag** | **str** |  | 
**exclude_from_subscription_types** | **List[str]** |  | 
**inbound_tag** | **str** |  | 
**config_profile_uuid** | **UUID** |  | 
**config_profile_inbound_uuid** | **UUID** |  | 
**is_disabled** | **bool** |  | 
**is_hidden** | **bool** |  | 
**view_position** | **int** |  | 
**remark** | **str** |  | 
**vless_route_id** | **int** |  | 
**raw_inbound** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata import GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata from a JSON string
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata_instance = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata.from_json(json)
# print the JSON string representation of the object
print(GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata.to_json())

# convert the object into a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata_dict = get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata_instance.to_dict()
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata from a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata_from_dict = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata.from_dict(get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


