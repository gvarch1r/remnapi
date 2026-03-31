# GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_report** | [**GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport**](GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport.md) |  | 
**xray_report** | [**GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport**](GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportXrayReport.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto_response_records_inner_report import GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport from a JSON string
get_torrent_blocker_reports_response_dto_response_records_inner_report_instance = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_dict = get_torrent_blocker_reports_response_dto_response_records_inner_report_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport from a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_from_dict = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport.from_dict(get_torrent_blocker_reports_response_dto_response_records_inner_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


