# RemnawaveWebhookTorrentBlockerEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**RemnawaveWebhookTorrentBlockerEventsDtoData**](RemnawaveWebhookTorrentBlockerEventsDtoData.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_torrent_blocker_events_dto import RemnawaveWebhookTorrentBlockerEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookTorrentBlockerEventsDto from a JSON string
remnawave_webhook_torrent_blocker_events_dto_instance = RemnawaveWebhookTorrentBlockerEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookTorrentBlockerEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_torrent_blocker_events_dto_dict = remnawave_webhook_torrent_blocker_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookTorrentBlockerEventsDto from a dict
remnawave_webhook_torrent_blocker_events_dto_from_dict = RemnawaveWebhookTorrentBlockerEventsDto.from_dict(remnawave_webhook_torrent_blocker_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


