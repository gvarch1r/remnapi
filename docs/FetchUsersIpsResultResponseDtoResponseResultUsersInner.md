# FetchUsersIpsResultResponseDtoResponseResultUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**ips** | [**List[FetchIpsResultResponseDtoResponseResultNodesInnerIpsInner]**](FetchIpsResultResponseDtoResponseResultNodesInnerIpsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_users_ips_result_response_dto_response_result_users_inner import FetchUsersIpsResultResponseDtoResponseResultUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUsersIpsResultResponseDtoResponseResultUsersInner from a JSON string
fetch_users_ips_result_response_dto_response_result_users_inner_instance = FetchUsersIpsResultResponseDtoResponseResultUsersInner.from_json(json)
# print the JSON string representation of the object
print(FetchUsersIpsResultResponseDtoResponseResultUsersInner.to_json())

# convert the object into a dict
fetch_users_ips_result_response_dto_response_result_users_inner_dict = fetch_users_ips_result_response_dto_response_result_users_inner_instance.to_dict()
# create an instance of FetchUsersIpsResultResponseDtoResponseResultUsersInner from a dict
fetch_users_ips_result_response_dto_response_result_users_inner_from_dict = FetchUsersIpsResultResponseDtoResponseResultUsersInner.from_dict(fetch_users_ips_result_response_dto_response_result_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


