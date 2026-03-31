# FetchUsersIpsResultResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FetchUsersIpsResultResponseDtoResponse**](FetchUsersIpsResultResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_users_ips_result_response_dto import FetchUsersIpsResultResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUsersIpsResultResponseDto from a JSON string
fetch_users_ips_result_response_dto_instance = FetchUsersIpsResultResponseDto.from_json(json)
# print the JSON string representation of the object
print(FetchUsersIpsResultResponseDto.to_json())

# convert the object into a dict
fetch_users_ips_result_response_dto_dict = fetch_users_ips_result_response_dto_instance.to_dict()
# create an instance of FetchUsersIpsResultResponseDto from a dict
fetch_users_ips_result_response_dto_from_dict = FetchUsersIpsResultResponseDto.from_dict(fetch_users_ips_result_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


