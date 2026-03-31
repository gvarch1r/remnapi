# CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**provider_uuid** | **UUID** |  | 
**amount** | **float** |  | 
**billed_at** | **datetime** |  | 
**provider** | [**CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInnerProvider**](CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInnerProvider.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_infra_billing_history_record_response_dto_response_records_inner import CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner from a JSON string
create_infra_billing_history_record_response_dto_response_records_inner_instance = CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner.to_json())

# convert the object into a dict
create_infra_billing_history_record_response_dto_response_records_inner_dict = create_infra_billing_history_record_response_dto_response_records_inner_instance.to_dict()
# create an instance of CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner from a dict
create_infra_billing_history_record_response_dto_response_records_inner_from_dict = CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner.from_dict(create_infra_billing_history_record_response_dto_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


