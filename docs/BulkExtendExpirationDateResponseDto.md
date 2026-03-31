# BulkExtendExpirationDateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_extend_expiration_date_response_dto import BulkExtendExpirationDateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkExtendExpirationDateResponseDto from a JSON string
bulk_extend_expiration_date_response_dto_instance = BulkExtendExpirationDateResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkExtendExpirationDateResponseDto.to_json())

# convert the object into a dict
bulk_extend_expiration_date_response_dto_dict = bulk_extend_expiration_date_response_dto_instance.to_dict()
# create an instance of BulkExtendExpirationDateResponseDto from a dict
bulk_extend_expiration_date_response_dto_from_dict = BulkExtendExpirationDateResponseDto.from_dict(bulk_extend_expiration_date_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


