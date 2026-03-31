# GetInfraProvidersResponseDtoResponseProvidersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | 
**favicon_link** | **str** |  | 
**login_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**billing_history** | [**GetInfraProvidersResponseDtoResponseProvidersInnerBillingHistory**](GetInfraProvidersResponseDtoResponseProvidersInnerBillingHistory.md) |  | 
**billing_nodes** | [**List[GetInfraProvidersResponseDtoResponseProvidersInnerBillingNodesInner]**](GetInfraProvidersResponseDtoResponseProvidersInnerBillingNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_providers_response_dto_response_providers_inner import GetInfraProvidersResponseDtoResponseProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraProvidersResponseDtoResponseProvidersInner from a JSON string
get_infra_providers_response_dto_response_providers_inner_instance = GetInfraProvidersResponseDtoResponseProvidersInner.from_json(json)
# print the JSON string representation of the object
print(GetInfraProvidersResponseDtoResponseProvidersInner.to_json())

# convert the object into a dict
get_infra_providers_response_dto_response_providers_inner_dict = get_infra_providers_response_dto_response_providers_inner_instance.to_dict()
# create an instance of GetInfraProvidersResponseDtoResponseProvidersInner from a dict
get_infra_providers_response_dto_response_providers_inner_from_dict = GetInfraProvidersResponseDtoResponseProvidersInner.from_dict(get_infra_providers_response_dto_response_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


