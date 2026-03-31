# UpdateInfraBillingNodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**next_billing_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.update_infra_billing_node_request_dto import UpdateInfraBillingNodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfraBillingNodeRequestDto from a JSON string
update_infra_billing_node_request_dto_instance = UpdateInfraBillingNodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInfraBillingNodeRequestDto.to_json())

# convert the object into a dict
update_infra_billing_node_request_dto_dict = update_infra_billing_node_request_dto_instance.to_dict()
# create an instance of UpdateInfraBillingNodeRequestDto from a dict
update_infra_billing_node_request_dto_from_dict = UpdateInfraBillingNodeRequestDto.from_dict(update_infra_billing_node_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


