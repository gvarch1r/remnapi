# GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_remark** | **str** |  | 
**address** | **str** |  | 
**port** | **int** |  | 
**protocol** | **str** |  | 
**protocol_options** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerProtocolOptions**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerProtocolOptions.md) |  | 
**transport** | **str** |  | 
**transport_options** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions.md) |  | 
**security** | **str** |  | 
**security_options** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerSecurityOptions**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerSecurityOptions.md) |  | [optional] 
**stream_overrides** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerStreamOverrides**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerStreamOverrides.md) |  | 
**mux** | **object** |  | 
**client_overrides** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerClientOverrides**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerClientOverrides.md) |  | 
**metadata** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerMetadata.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner import GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner from a JSON string
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_instance = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner.from_json(json)
# print the JSON string representation of the object
print(GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner.to_json())

# convert the object into a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_dict = get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_instance.to_dict()
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner from a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_from_dict = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner.from_dict(get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


