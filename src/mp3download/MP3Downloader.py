import src.logs.Logging as log
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.business.YouTubeVideoStates import YouTubeVideoStates as state


class MP3Downloader:
    _logger = log.get_logger(__name__)

    def __init__(self):
        self.all_video_information = PersistVideoInformation().get_video_information()
        self.videos_to_be_uploaded = set()
        self.check_videos_to_be_uploaded()

    def check_videos_to_be_uploaded(self):
        for video, status in self.all_video_information.items():
            if status == state.TO_BE_UPLOADED:
                self.videos_to_be_uploaded.add(video)
        self._logger.debug(f"Podcasts want to be downloaded as MP3:"
                           f"{str(self.videos_to_be_uploaded)}")


