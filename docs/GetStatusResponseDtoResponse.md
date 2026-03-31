# GetStatusResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_login_allowed** | **bool** |  | 
**is_register_allowed** | **bool** |  | 
**authentication** | [**GetStatusResponseDtoResponseAuthentication**](GetStatusResponseDtoResponseAuthentication.md) |  | 
**branding** | [**GetStatusResponseDtoResponseBranding**](GetStatusResponseDtoResponseBranding.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_status_response_dto_response import GetStatusResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusResponseDtoResponse from a JSON string
get_status_response_dto_response_instance = GetStatusResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatusResponseDtoResponse.to_json())

# convert the object into a dict
get_status_response_dto_response_dict = get_status_response_dto_response_instance.to_dict()
# create an instance of GetStatusResponseDtoResponse from a dict
get_status_response_dto_response_from_dict = GetStatusResponseDtoResponse.from_dict(get_status_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


