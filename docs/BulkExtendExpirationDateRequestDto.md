# BulkExtendExpirationDateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**extend_days** | **int** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_extend_expiration_date_request_dto import BulkExtendExpirationDateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkExtendExpirationDateRequestDto from a JSON string
bulk_extend_expiration_date_request_dto_instance = BulkExtendExpirationDateRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkExtendExpirationDateRequestDto.to_json())

# convert the object into a dict
bulk_extend_expiration_date_request_dto_dict = bulk_extend_expiration_date_request_dto_instance.to_dict()
# create an instance of BulkExtendExpirationDateRequestDto from a dict
bulk_extend_expiration_date_request_dto_from_dict = BulkExtendExpirationDateRequestDto.from_dict(bulk_extend_expiration_date_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


