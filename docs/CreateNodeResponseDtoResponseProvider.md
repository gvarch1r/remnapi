# CreateNodeResponseDtoResponseProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | 
**favicon_link** | **str** |  | 
**login_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_provider import CreateNodeResponseDtoResponseProvider

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseProvider from a JSON string
create_node_response_dto_response_provider_instance = CreateNodeResponseDtoResponseProvider.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseProvider.to_json())

# convert the object into a dict
create_node_response_dto_response_provider_dict = create_node_response_dto_response_provider_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseProvider from a dict
create_node_response_dto_response_provider_from_dict = CreateNodeResponseDtoResponseProvider.from_dict(create_node_response_dto_response_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


