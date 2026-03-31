# CreateInfraBillingNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInfraBillingNodesResponseDtoResponse**](GetInfraBillingNodesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_infra_billing_node_response_dto import CreateInfraBillingNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraBillingNodeResponseDto from a JSON string
create_infra_billing_node_response_dto_instance = CreateInfraBillingNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateInfraBillingNodeResponseDto.to_json())

# convert the object into a dict
create_infra_billing_node_response_dto_dict = create_infra_billing_node_response_dto_instance.to_dict()
# create an instance of CreateInfraBillingNodeResponseDto from a dict
create_infra_billing_node_response_dto_from_dict = CreateInfraBillingNodeResponseDto.from_dict(create_infra_billing_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


