# FetchUsersIpsResultResponseDtoResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**node_uuid** | **UUID** |  | 
**users** | [**List[FetchUsersIpsResultResponseDtoResponseResultUsersInner]**](FetchUsersIpsResultResponseDtoResponseResultUsersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_users_ips_result_response_dto_response_result import FetchUsersIpsResultResponseDtoResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUsersIpsResultResponseDtoResponseResult from a JSON string
fetch_users_ips_result_response_dto_response_result_instance = FetchUsersIpsResultResponseDtoResponseResult.from_json(json)
# print the JSON string representation of the object
print(FetchUsersIpsResultResponseDtoResponseResult.to_json())

# convert the object into a dict
fetch_users_ips_result_response_dto_response_result_dict = fetch_users_ips_result_response_dto_response_result_instance.to_dict()
# create an instance of FetchUsersIpsResultResponseDtoResponseResult from a dict
fetch_users_ips_result_response_dto_response_result_from_dict = FetchUsersIpsResultResponseDtoResponseResult.from_dict(fetch_users_ips_result_response_dto_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


