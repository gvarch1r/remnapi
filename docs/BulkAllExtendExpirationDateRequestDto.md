# BulkAllExtendExpirationDateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend_days** | **int** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_all_extend_expiration_date_request_dto import BulkAllExtendExpirationDateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAllExtendExpirationDateRequestDto from a JSON string
bulk_all_extend_expiration_date_request_dto_instance = BulkAllExtendExpirationDateRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkAllExtendExpirationDateRequestDto.to_json())

# convert the object into a dict
bulk_all_extend_expiration_date_request_dto_dict = bulk_all_extend_expiration_date_request_dto_instance.to_dict()
# create an instance of BulkAllExtendExpirationDateRequestDto from a dict
bulk_all_extend_expiration_date_request_dto_from_dict = BulkAllExtendExpirationDateRequestDto.from_dict(bulk_all_extend_expiration_date_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


