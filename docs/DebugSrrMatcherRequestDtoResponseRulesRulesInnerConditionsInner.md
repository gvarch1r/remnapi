# DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner

{\"markdownDescription\":\"Condition to check against the **headerName**.\",\"defaultSnippets\":[{\"label\":\"Examples: Check if header contains \\\"text/html\\\"\",\"markdownDescription\":\"Condition to check if **headerName** contains \\\"text/html\\\"\",\"body\":{\"headerName\":\"accept\",\"operator\":\"CONTAINS\",\"value\":\"text/html\",\"caseSensitive\":true}}]}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** | {\&quot;markdownDescription\&quot;:\&quot;**Name** of the HTTP header to check. Must comply with RFC 7230.\&quot;} | 
**operator** | **str** | {\&quot;errorMessage\&quot;:\&quot;Invalid operator. Please select a valid operator.\&quot;,\&quot;markdownDescription\&quot;:\&quot;Operator to use for comparing the &#x60;headerName&#x60; with &#x60;value&#x60;.\&quot;,\&quot;markdownEnumDescriptions\&quot;:[\&quot;Performs an exact, comparison between the header value and specified string. &#x60;string &#x3D;&#x3D;&#x3D; value&#x60;\&quot;,\&quot;Ensures the header value does not exactly match the specified string. &#x60;string !&#x3D;&#x3D; value&#x60;\&quot;,\&quot;Checks if the header value contains the specified string as a substring. &#x60;string.includes()&#x60;\&quot;,\&quot;Verifies the header value does not contain the specified string as a substring. &#x60;!string.includes()&#x60;\&quot;,\&quot;Validates that the header value begins with the specified string. &#x60;string.startsWith()&#x60;\&quot;,\&quot;Validates that the header value does not begin with the specified string. &#x60;!string.startsWith()&#x60;\&quot;,\&quot;Confirms the header value ends with the specified string. &#x60;string.endsWith()&#x60;\&quot;,\&quot;Confirms the header value does not end with the specified string. &#x60;!string.endsWith()&#x60;\&quot;,\&quot;Evaluates if the header value matches the specified regular expression pattern. &#x60;regex.test()&#x60;\&quot;,\&quot;Evaluates if the header value does not match the specified regular expression pattern. &#x60;!regex.test()&#x60;\&quot;]} | 
**value** | **str** | {\&quot;markdownDescription\&quot;:\&quot;**Value** to check against the **headerName**.\&quot;} | 
**case_sensitive** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;Whether the value is **case sensitive**. \\n\\n - &#x60;true&#x60;: the value will be compared as is. \\n\\n - &#x60;false&#x60;: the value will be lowercased **before** comparison.\&quot;} | 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner import DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner from a JSON string
debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner_instance = DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner.to_json())

# convert the object into a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner_dict = debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner_instance.to_dict()
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner from a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner_from_dict = DebugSrrMatcherRequestDtoResponseRulesRulesInnerConditionsInner.from_dict(debug_srr_matcher_request_dto_response_rules_rules_inner_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


