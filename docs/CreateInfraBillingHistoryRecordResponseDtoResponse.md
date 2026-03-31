# CreateInfraBillingHistoryRecordResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner]**](CreateInfraBillingHistoryRecordResponseDtoResponseRecordsInner.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.create_infra_billing_history_record_response_dto_response import CreateInfraBillingHistoryRecordResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfraBillingHistoryRecordResponseDtoResponse from a JSON string
create_infra_billing_history_record_response_dto_response_instance = CreateInfraBillingHistoryRecordResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateInfraBillingHistoryRecordResponseDtoResponse.to_json())

# convert the object into a dict
create_infra_billing_history_record_response_dto_response_dict = create_infra_billing_history_record_response_dto_response_instance.to_dict()
# create an instance of CreateInfraBillingHistoryRecordResponseDtoResponse from a dict
create_infra_billing_history_record_response_dto_response_from_dict = CreateInfraBillingHistoryRecordResponseDtoResponse.from_dict(create_infra_billing_history_record_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


