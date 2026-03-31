# GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**level** | **float** |  | 
**protocol** | **str** |  | 
**network** | **str** |  | 
**source** | **str** |  | 
**destination** | **str** |  | 
**route_target** | **str** |  | 
**original_target** | **str** |  | 
**inbound_tag** | **str** |  | 
**inbound_name** | **str** |  | 
**inbound_local** | **str** |  | 
**outbound_tag** | **str** |  | 
**ts** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report import GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport from a JSON string
get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report_instance = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report_dict = get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport from a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report_from_dict = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport.from_dict(get_torrent_blocker_reports_response_dto_response_records_inner_report_xray_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


