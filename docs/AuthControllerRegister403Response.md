# AuthControllerRegister403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | [optional] 
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.auth_controller_register403_response import AuthControllerRegister403Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthControllerRegister403Response from a JSON string
auth_controller_register403_response_instance = AuthControllerRegister403Response.from_json(json)
# print the JSON string representation of the object
print(AuthControllerRegister403Response.to_json())

# convert the object into a dict
auth_controller_register403_response_dict = auth_controller_register403_response_instance.to_dict()
# create an instance of AuthControllerRegister403Response from a dict
auth_controller_register403_response_from_dict = AuthControllerRegister403Response.from_dict(auth_controller_register403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


