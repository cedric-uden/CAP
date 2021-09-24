from watchdog.queries.CheckYouTubeVideoInspector import CheckYouTubeVideoInspector
from watchdog.queries.MostRecentYouTubeVideos import MostRecentYouTubeVideos
from watchdog.utils.PersistVideoInformation import PersistVideoInformation
from watchdog.business.YouTubeVideoStates import YouTubeVideoStates as state
import watchdog.logs.Logging as log


class YouTubeInformation:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.all_video_ids = set()
        self.vid_info = PersistVideoInformation().get_video_information()

    def get_info(self):
        self.get_most_recent_yt_video_ids()
        self.add_new_videos_to_video_information_set()

    def get_most_recent_yt_video_ids(self):
        all_videos = MostRecentYouTubeVideos().get_json()
        for video in all_videos['items']:
            if len(video['contentDetails']) > 0:
                self.all_video_ids.add(video['contentDetails']['upload']['videoId'])

        self._logger.info(f"Most recent videos on channel: {str(self.all_video_ids)}")
        return self.all_video_ids

    def is_video_in_video_information_set(self, video_id):
        return True if self.vid_info.get(video_id) else False

    def add_new_videos_to_video_information_set(self):
        for video in self.all_video_ids:
            if not self.is_video_in_video_information_set(video):
                self.vid_info.update({video: state.NEW})
                self._logger.debug(f"Added video {video} to the information set.")
            PersistVideoInformation().store_video_information(self.vid_info)
            else:
                self._logger.debug(f"Video {video} was found in the video information set.")



