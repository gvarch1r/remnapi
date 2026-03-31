# OAuth2CallbackRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**code** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.o_auth2_callback_request_dto import OAuth2CallbackRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2CallbackRequestDto from a JSON string
o_auth2_callback_request_dto_instance = OAuth2CallbackRequestDto.from_json(json)
# print the JSON string representation of the object
print(OAuth2CallbackRequestDto.to_json())

# convert the object into a dict
o_auth2_callback_request_dto_dict = o_auth2_callback_request_dto_instance.to_dict()
# create an instance of OAuth2CallbackRequestDto from a dict
o_auth2_callback_request_dto_from_dict = OAuth2CallbackRequestDto.from_dict(o_auth2_callback_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


