# CreateApiTokenResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**uuid** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.create_api_token_response_dto_response import CreateApiTokenResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiTokenResponseDtoResponse from a JSON string
create_api_token_response_dto_response_instance = CreateApiTokenResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateApiTokenResponseDtoResponse.to_json())

# convert the object into a dict
create_api_token_response_dto_response_dict = create_api_token_response_dto_response_instance.to_dict()
# create an instance of CreateApiTokenResponseDtoResponse from a dict
create_api_token_response_dto_response_from_dict = CreateApiTokenResponseDtoResponse.from_dict(create_api_token_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


