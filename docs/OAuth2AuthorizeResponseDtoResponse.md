# OAuth2AuthorizeResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.o_auth2_authorize_response_dto_response import OAuth2AuthorizeResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AuthorizeResponseDtoResponse from a JSON string
o_auth2_authorize_response_dto_response_instance = OAuth2AuthorizeResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2AuthorizeResponseDtoResponse.to_json())

# convert the object into a dict
o_auth2_authorize_response_dto_response_dict = o_auth2_authorize_response_dto_response_instance.to_dict()
# create an instance of OAuth2AuthorizeResponseDtoResponse from a dict
o_auth2_authorize_response_dto_response_from_dict = OAuth2AuthorizeResponseDtoResponse.from_dict(o_auth2_authorize_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


