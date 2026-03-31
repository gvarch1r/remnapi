# FetchUsersIpsResultResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_completed** | **bool** |  | 
**is_failed** | **bool** |  | 
**result** | [**FetchUsersIpsResultResponseDtoResponseResult**](FetchUsersIpsResultResponseDtoResponseResult.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_users_ips_result_response_dto_response import FetchUsersIpsResultResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUsersIpsResultResponseDtoResponse from a JSON string
fetch_users_ips_result_response_dto_response_instance = FetchUsersIpsResultResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(FetchUsersIpsResultResponseDtoResponse.to_json())

# convert the object into a dict
fetch_users_ips_result_response_dto_response_dict = fetch_users_ips_result_response_dto_response_instance.to_dict()
# create an instance of FetchUsersIpsResultResponseDtoResponse from a dict
fetch_users_ips_result_response_dto_response_from_dict = FetchUsersIpsResultResponseDtoResponse.from_dict(fetch_users_ips_result_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


