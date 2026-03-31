# CreateInfraBillingNodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_uuid** | **UUID** |  | 
**node_uuid** | **UUID** |  | 
**next_billing_at** | **datetime** | Next billing date. Format: 2025-01-17T15:38:45.065Z | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_infra_billing_node_request_dto import CreateInfraBillingNodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraBillingNodeRequestDto from a JSON string
create_infra_billing_node_request_dto_instance = CreateInfraBillingNodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateInfraBillingNodeRequestDto.to_json())

# convert the object into a dict
create_infra_billing_node_request_dto_dict = create_infra_billing_node_request_dto_instance.to_dict()
# create an instance of CreateInfraBillingNodeRequestDto from a dict
create_infra_billing_node_request_dto_from_dict = CreateInfraBillingNodeRequestDto.from_dict(create_infra_billing_node_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


