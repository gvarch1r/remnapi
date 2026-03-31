# FetchUsersIpsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FetchIpsResponseDtoResponse**](FetchIpsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_users_ips_response_dto import FetchUsersIpsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUsersIpsResponseDto from a JSON string
fetch_users_ips_response_dto_instance = FetchUsersIpsResponseDto.from_json(json)
# print the JSON string representation of the object
print(FetchUsersIpsResponseDto.to_json())

# convert the object into a dict
fetch_users_ips_response_dto_dict = fetch_users_ips_response_dto_instance.to_dict()
# create an instance of FetchUsersIpsResponseDto from a dict
fetch_users_ips_response_dto_from_dict = FetchUsersIpsResponseDto.from_dict(fetch_users_ips_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


