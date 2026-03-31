# CreateInfraBillingHistoryRecordRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_uuid** | **UUID** |  | 
**amount** | **float** |  | 
**billed_at** | **datetime** | Billing date. Format: 2025-01-17T15:38:45.065Z | 

## Example

```python
from supn_remnawave_panel.models.create_infra_billing_history_record_request_dto import CreateInfraBillingHistoryRecordRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraBillingHistoryRecordRequestDto from a JSON string
create_infra_billing_history_record_request_dto_instance = CreateInfraBillingHistoryRecordRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateInfraBillingHistoryRecordRequestDto.to_json())

# convert the object into a dict
create_infra_billing_history_record_request_dto_dict = create_infra_billing_history_record_request_dto_instance.to_dict()
# create an instance of CreateInfraBillingHistoryRecordRequestDto from a dict
create_infra_billing_history_record_request_dto_from_dict = CreateInfraBillingHistoryRecordRequestDto.from_dict(create_infra_billing_history_record_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


