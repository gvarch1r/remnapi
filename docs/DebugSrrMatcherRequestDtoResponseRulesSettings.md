# DebugSrrMatcherRequestDtoResponseRulesSettings

{\"markdownDescription\":\"Settings for the **response rules** config. Optional.\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_subscription_access_by_path** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;Usually, a user&#39;s subscription may also be available via additional paths such as **/json**, **/stash**, or **/mihomo**. If this flag is set to **true**, access via these additional paths will be disabled.\&quot;} | [optional] 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_request_dto_response_rules_settings import DebugSrrMatcherRequestDtoResponseRulesSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherRequestDtoResponseRulesSettings from a JSON string
debug_srr_matcher_request_dto_response_rules_settings_instance = DebugSrrMatcherRequestDtoResponseRulesSettings.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherRequestDtoResponseRulesSettings.to_json())

# convert the object into a dict
debug_srr_matcher_request_dto_response_rules_settings_dict = debug_srr_matcher_request_dto_response_rules_settings_instance.to_dict()
# create an instance of DebugSrrMatcherRequestDtoResponseRulesSettings from a dict
debug_srr_matcher_request_dto_response_rules_settings_from_dict = DebugSrrMatcherRequestDtoResponseRulesSettings.from_dict(debug_srr_matcher_request_dto_response_rules_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


