import src.logs.Logging as log
from src.utils.PersistVideoInformation import PersistVideoInformation


class HandleDetailedInfoFromVideos:
    _logger = log.get_logger(__name__)

    def __init__(self, json):
        self.json = json

    def store(self):
        all_info = self.get_info()
        video_id = list(all_info.keys())[0]
        video_info_dict = all_info.get(video_id)
        PersistVideoInformation().update_video_info(video_id, video_info_dict)

    def get_info(self):
        video_id = self.json['items'][0]['id']
        upload_status = self.json['items'][0]['status']['uploadStatus']
        privacy_status = self.json['items'][0]['status']['privacyStatus']
        stream_start = self.json['items'][0]['liveStreamingDetails']['actualStartTime']
        title = self.json['items'][0]['snippet']['title']
        all_info = {
            video_id: {
                'title': title,
                'upload_status': upload_status,
                'privacy_status': privacy_status,
                "stream_start": stream_start,
            }
        }
        return all_info

