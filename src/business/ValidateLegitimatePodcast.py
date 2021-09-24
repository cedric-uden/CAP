from src.business.YouTubeVideoStates import YouTubeVideoStates as state
from src.queries.CheckYouTubeVideoInspector import CheckYouTubeVideoInspector
import src.logs.Logging as log
from src.constants.Constants import SettingConstants
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.business.HandleDetailedInfoFromVideos import HandleDetailedInfoFromVideos

import re


class ValidateLegitimatePodcast:

    _logger = log.get_logger(__name__)

    def __init__(self, videos_to_be_processed):
        self.videos_to_be_processed = videos_to_be_processed
        self.settings = SettingConstants()

    def validate_videos(self):
        for video_id in self.videos_to_be_processed:
            video_info = CheckYouTubeVideoInspector().get_json_from_youtube_id(video_id)
            HandleDetailedInfoFromVideos(video_info).store()
            valid_metadata = self.valid_metadata(video_id, video_info)
            valid_duration = self.valid_time(video_id, video_info)
            if valid_metadata and valid_duration:
                self._logger.info(f"Video '{video_id}' identified to be uploaded as MP3.")
                self.update_state(video_id, state.TO_BE_DOWNLOADED)
            elif valid_metadata and not valid_duration:
                self._logger.warn(f"Video '{video_id}' was identified as "
                                  f"not being a sermon.")
                self.update_state(video_id, state.NOT_A_SERMON)
            elif not valid_metadata and not valid_duration:
                self._logger.error(f"Error identifying '{video_id}'")

    def update_state(self, key, value):
        self._logger.debug(f"Going to update state for {key}")
        PersistVideoInformation().update_video_state(key, value)

    def valid_metadata(self, video_id, video_info):
        cond1 = (video_info['items'][0]['status']['uploadStatus'] == "processed")
        cond2 = (video_info['items'][0]['status']['privacyStatus'] == "public")
        cond3 = (video_info['items'][0]['processingDetails']['processingStatus'] == "succeeded")
        result = cond1 and cond2 and cond3
        if not result:
            self._logger.warn(f"Metadata for video '{video_id}' was not matched.")
        return result

    def valid_time(self, video_id, video_info):
        # time_string expected in format like `PT36M25S`
        time_string = video_info['items'][0]['contentDetails']['duration']
        time_split = time_string.split("M")
        time_in_minutes = re.findall(r'\d+', time_split[0])
        time_in_minutes = int(time_in_minutes[0])

        lower_bound = self.settings.get_podcast_min_duration()
        upper_bound = self.settings.get_podcast_max_duration()
        result = (lower_bound < time_in_minutes < upper_bound)
        if not result:
            self._logger.warn(f"Length for video to validate podcast for video "
                              f"{video_id} was not matched.")
        return result
