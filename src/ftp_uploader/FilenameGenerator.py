import src.logs.Logging as log
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.utils.FilenameSanitizer import FilenameSanitizer
from src.utils.TimeHandler import get_datetime_from_string

"""
Expects a video ID on creation and will look up the `video_detailed_info.pkl` file
to extract the final filename for the audio podcast.
"""


class FilenameGenerator:
    _logger = log.get_logger(__name__)

    def __init__(self, video_id):
        self.video_id = video_id
        self.detailed_info = PersistVideoInformation().get_video_info()

    def get_filename(self):
        youtube_date = self.get_date()
        youtube_title = self.get_title()
        youtube_title = FilenameSanitizer().clean_filename(youtube_title)
        final_filename = f"{youtube_date}-{self.video_id}-{youtube_title}.mp3"
        return final_filename

    def get_date(self):
        actual_start_time = self.detailed_info[self.video_id]['stream_start']
        datetime_object = get_datetime_from_string(actual_start_time)
        date_string = f"{datetime_object.strftime('%Y%m%d')}"
        return date_string

    def get_title(self):
        return self.detailed_info[self.video_id]['title']



