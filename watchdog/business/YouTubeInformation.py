from watchdog.queries.CheckYouTubeVideoInspector import CheckYouTubeVideoInspector
from watchdog.queries.MostRecentYouTubeVideos import MostRecentYouTubeVideos
import watchdog.logs.Logging as log


class YouTubeInformation:

    _logger = log.get_logger(__name__)

    def get_most_recent_yt_video_ids(self):
        all_videos = MostRecentYouTubeVideos().get_json()
        all_video_ids = set()
        for video in all_videos['items']:
            if len(video['contentDetails']) > 0:
                all_video_ids.add(video['contentDetails']['upload']['videoId'])

        self._logger.info(f"Most recent videos on channel: {str(all_video_ids)}")
        return all_video_ids

