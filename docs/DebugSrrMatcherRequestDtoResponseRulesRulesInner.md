# DebugSrrMatcherRequestDtoResponseRulesRulesInner

{\"defaultSnippets\":[{\"label\":\"Examples: Blank rule\",\"markdownDescription\":\"Simple blank rule with no conditions or modifications.\\n```json\\n{\\n  \\\"name\\\": \\\"Blank rule\\\",\\n  \\\"description\\\": \\\"Blank rule\\\",\\n  \\\"operator\\\": \\\"AND\\\",\\n  \\\"enabled\\\": true,\\n  \\\"conditions\\\": [],\\n  \\\"responseType\\\": \\\"BLOCK\\\",\\n  \\\"responseModifications\\\": {\\n    \\\"headers\\\": []\\n  }\\n}\\n```\",\"body\":{\"name\":\"Blank rule\",\"description\":\"Blank rule\",\"operator\":\"AND\",\"enabled\":true,\"conditions\":[],\"responseType\":\"BLOCK\",\"responseModifications\":{\"headers\":[]}}},{\"label\":\"Examples: Block Legacy Clients\",\"markdownDescription\":\"Block requests from legacy clients\\n```json\\n{\\n  \\\"name\\\": \\\"Block Legacy Clients\\\",\\n  \\\"description\\\": \\\"Block requests from legacy clients\\\",\\n  \\\"enabled\\\": true,\\n  \\\"operator\\\": \\\"OR\\\",\\n  \\\"conditions\\\": [\\n    {\\n      \\\"headerName\\\": \\\"user-agent\\\",\\n      \\\"operator\\\": \\\"CONTAINS\\\",\\n      \\\"value\\\": \\\"Hiddify\\\",\\n      \\\"caseSensitive\\\": true\\n    },\\n    {\\n      \\\"headerName\\\": \\\"user-agent\\\",\\n      \\\"operator\\\": \\\"CONTAINS\\\",\\n      \\\"value\\\": \\\"FoxRay\\\",\\n      \\\"caseSensitive\\\": true\\n    }\\n  ],\\n  \\\"responseType\\\": \\\"BLOCK\\\"\\n}\\n```\",\"body\":{\"name\":\"Block Legacy Clients\",\"description\":\"Block requests from legacy clients\",\"enabled\":true,\"operator\":\"OR\",\"conditions\":[{\"headerName\":\"user-agent\",\"operator\":\"CONTAINS\",\"value\":\"Hiddify\",\"caseSensitive\":true},{\"headerName\":\"user-agent\",\"operator\":\"CONTAINS\",\"value\":\"FoxRay\",\"caseSensitive\":true}],\"responseType\":\"BLOCK\"}}],\"title\":\"Response Rule\",\"markdownDescription\":\"Response rule configuration.\\n\\n**Fields:**\\n- **name**: Name of the response rule.\\n- **description**: Description of the response rule. Optional.\\n- **enabled**: Control whether the response rule is enabled or disabled. \\n\\n - `true` the rule will be applied. \\n\\n - `false` the rule will be always ignored.\\n- **operator**: Operator to use for combining conditions in the rule.\\n- **conditions**: Array of conditions to check against the request headers. Conditions are applied with **operator**. If conditions are empty, the rule will be matched.\\n- **responseType**: Type of the response. Determines the type of **response** to be returned when the rule is matched.\\n- **responseModifications**: Response modifications to be applied when the rule is matched. Optional.\\n\\n**Example:**\\n```json\\n{\\n  \\\"name\\\": \\\"Block Legacy Clients\\\",\\n  \\\"description\\\": \\\"Block requests from legacy clients\\\",\\n  \\\"enabled\\\": true,\\n  \\\"operator\\\": \\\"OR\\\",\\n  \\\"conditions\\\": [\\n    {\\n      \\\"headerName\\\": \\\"user-agent\\\",\\n      \\\"operator\\\": \\\"CONTAINS\\\",\\n      \\\"value\\\": \\\"Hiddify\\\",\\n      \\\"caseSensitive\\\": true\\n    },\\n    {\\n      \\\"headerName\\\": \\\"user-agent\\\",\\n      \\\"operator\\\": \\\"CONTAINS\\\",\\n      \\\"value\\\": \\\"FoxRay\\\",\\n      \\\"caseSensitive\\\": true\\n    }\\n  ],\\n  \\\"responseType\\\": \\\"BLOCK\\\"\\n}\\n```\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | {\&quot;markdownDescription\&quot;:\&quot;Name of the response rule.\&quot;} | 
**description** | **str** | {\&quot;markdownDescription\&quot;:\&quot;Description of the response rule. Optional.\&quot;} | [optional] 
**enabled** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;Control whether the response rule is enabled or disabled. \\n\\n - &#x60;true&#x60; the rule will be applied. \\n\\n - &#x60;false&#x60; the rule will be always ignored.\&quot;} | 
**operator** | **str** | {\&quot;markdownDescription\&quot;:\&quot;Operator to use for combining conditions in the rule.\&quot;} | 
**conditions** | [**List[DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner]**](DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner.md) | {\&quot;markdownDescription\&quot;:\&quot;Array of conditions to check against the request headers. Conditions are applied with **operator**. If conditions are empty, the rule will be matched.\&quot;} | 
**response_type** | **str** | {\&quot;errorMessage\&quot;:\&quot;Invalid response type. Please select a valid response type.\&quot;,\&quot;markdownDescription\&quot;:\&quot;Type of the response. Determines the type of **response** to be returned when the rule is matched.\&quot;,\&quot;markdownEnumDescriptions\&quot;:[\&quot;Return **subscription** in XRAY-JSON format. (Using &#x60;Xray Json&#x60; template)\&quot;,\&quot;Return **subscription** in BASE64 encoded string. Compatible with most client application with Xray core.\&quot;,\&quot;Return **subscription** in Mihomo format. (Using &#x60;Mihomo&#x60; template)\&quot;,\&quot;Return **subscription** in Stash format. (Using &#x60;Stash&#x60; template)\&quot;,\&quot;Return **subscription** in Clash format. (Using &#x60;Clash&#x60; template) Useful for client application that use Legacy Clash core.\&quot;,\&quot;Return **subscription** in Singbox format. (Using &#x60;Singbox&#x60; template) Format which is used by Singbox client application.\&quot;,\&quot;Return **subscription** as browser format. The same as on &#x60;/info&#x60; route.\&quot;,\&quot;**Drop** request and return &#x60;403&#x60; status code.\&quot;,\&quot;**Drop** request and return &#x60;404&#x60; status code.\&quot;,\&quot;**Drop** request and return &#x60;451&#x60; status code.\&quot;,\&quot;**Drop** the socket connection.\&quot;]} | 
**response_modifications** | [**DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications**](DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_request_dto_response_rules_rules_inner import DebugSrrMatcherRequestDtoResponseRulesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInner from a JSON string
debug_srr_matcher_request_dto_response_rules_rules_inner_instance = DebugSrrMatcherRequestDtoResponseRulesRulesInner.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherRequestDtoResponseRulesRulesInner.to_json())

# convert the object into a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_dict = debug_srr_matcher_request_dto_response_rules_rules_inner_instance.to_dict()
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInner from a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_from_dict = DebugSrrMatcherRequestDtoResponseRulesRulesInner.from_dict(debug_srr_matcher_request_dto_response_rules_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


