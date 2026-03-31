# DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications

{\"examples\":[{\"headers\":[{\"key\":\"X-Custom-Header\",\"value\":\"CustomValue\"}]}],\"markdownDescription\":\"Response modifications to be applied when the rule is matched. Optional.\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModificationsHeadersInner]**](DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModificationsHeadersInner.md) | {\&quot;defaultSnippets\&quot;:[{\&quot;label\&quot;:\&quot;Examples: Add custom header\&quot;,\&quot;markdownDescription\&quot;:\&quot;Add a custom header to the response\&quot;,\&quot;body\&quot;:[{\&quot;key\&quot;:\&quot;X-Custom-Header\&quot;,\&quot;value\&quot;:\&quot;CustomValue\&quot;}]}],\&quot;markdownDescription\&quot;:\&quot;Array of headers to be added when the rule is matched.\&quot;} | [optional] 
**apply_headers_to_end** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;By default, headers are added when forming the response. In some cases, headers set in SRR may be overridden by headers from other parts of the system. If you set this flag to **true**, headers from SRR will be added at the very end, just before the response is sent. In this case, SRR headers may override headers from other sections.\&quot;} | [optional] 
**subscription_template** | **str** | {\&quot;markdownDescription\&quot;:\&quot;Override the subscription template with the given name. If not provided, the default subscription template will be used. If the template name is not found, the default subscription template for this type will be used. **This modification have higher priority than settings from External Squads.**\&quot;} | [optional] 
**ignore_host_xray_json_template** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;Each Host may have its own Xray Json Template. If you set this flag to **true**, the Xray Json Template defined by the SRR will be used. **The Host&#39;s Xray Json Template will be ignored.**\&quot;} | [optional] 
**ignore_serve_json_at_base_subscription** | **bool** | {\&quot;markdownDescription\&quot;:\&quot;If you set this flag to **true**, the **Serve JSON at Base Subscription** setting will be ignored (set to **false**).\&quot;} | [optional] 
**additional_extended_clients_regex** | **List[str]** | {\&quot;markdownDescription\&quot;:\&quot;Additional regex patterns to match extended clients. Matched clients will receive &#x60;serverDescription&#x60; in the subscription response.\\n\\n**Default Mihomo extended clients:**\\n- &#x60;^FlClash ?X/&#x60;\\n- &#x60;^Flowvy/&#x60;\\n- &#x60;^prizrak-box/&#x60;\\n- &#x60;^koala-clash/&#x60;\\n\\n**Default Xray extended clients:**\\n- &#x60;^Happ/&#x60;\\n- &#x60;^INCY/&#x60;\\n\\n**Example:** &#x60;[\\\&quot;^MyClient/\\\&quot;, \\\&quot;^CustomApp\\\\\\/v2\\\&quot;]&#x60;\&quot;} | [optional] 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications import DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications from a JSON string
debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications_instance = DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications.to_json())

# convert the object into a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications_dict = debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications_instance.to_dict()
# create an instance of DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications from a dict
debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications_from_dict = DebugSrrMatcherRequestDtoResponseRulesRulesInnerResponseModifications.from_dict(debug_srr_matcher_request_dto_response_rules_rules_inner_response_modifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


