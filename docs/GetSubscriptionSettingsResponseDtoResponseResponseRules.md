# GetSubscriptionSettingsResponseDtoResponseResponseRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | {\&quot;title\&quot;:\&quot;Response Rules Config Version\&quot;,\&quot;markdownDescription\&quot;:\&quot;Version of the **response rules** config. Currently supported version is **1**.\&quot;} | 
**settings** | [**DebugSrrMatcherRequestDtoResponseRulesSettings**](DebugSrrMatcherRequestDtoResponseRulesSettings.md) |  | [optional] 
**rules** | [**List[DebugSrrMatcherRequestDtoResponseRulesRulesInner]**](DebugSrrMatcherRequestDtoResponseRulesRulesInner.md) | {\&quot;title\&quot;:\&quot;Response Rules\&quot;,\&quot;markdownDescription\&quot;:\&quot;Array of **response rules**. Rules are evaluated in order and the first rule that matches is applied. If no rule matches, request will be blocked by default.\\n\\n**Example:**\\n&#x60;&#x60;&#x60;json\\n[\\n  {\\n    \\\&quot;name\\\&quot;: \\\&quot;Blank rule\\\&quot;,\\n    \\\&quot;description\\\&quot;: \\\&quot;Blank rule\\\&quot;,\\n    \\\&quot;operator\\\&quot;: \\\&quot;AND\\\&quot;,\\n    \\\&quot;enabled\\\&quot;: true,\\n    \\\&quot;conditions\\\&quot;: [],\\n    \\\&quot;responseType\\\&quot;: \\\&quot;BLOCK\\\&quot;,\\n    \\\&quot;responseModifications\\\&quot;: {\\n      \\\&quot;headers\\\&quot;: []\\n    }\\n  }\\n]\\n&#x60;&#x60;&#x60;\&quot;,\&quot;defaultSnippets\&quot;:[]} | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_settings_response_dto_response_response_rules import GetSubscriptionSettingsResponseDtoResponseResponseRules

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionSettingsResponseDtoResponseResponseRules from a JSON string
get_subscription_settings_response_dto_response_response_rules_instance = GetSubscriptionSettingsResponseDtoResponseResponseRules.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionSettingsResponseDtoResponseResponseRules.to_json())

# convert the object into a dict
get_subscription_settings_response_dto_response_response_rules_dict = get_subscription_settings_response_dto_response_response_rules_instance.to_dict()
# create an instance of GetSubscriptionSettingsResponseDtoResponseResponseRules from a dict
get_subscription_settings_response_dto_response_response_rules_from_dict = GetSubscriptionSettingsResponseDtoResponseResponseRules.from_dict(get_subscription_settings_response_dto_response_response_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


