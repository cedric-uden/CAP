import src.logs.Logging as log
from src.constants.Constants import SecretConstants, SettingConstants
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.business.YouTubeVideoStates import YouTubeVideoStates as state

import ftplib
import os


class FTPUploader:
    _logger = log.get_logger(__name__)

    def __init__(self):
        self.ftp_path = SettingConstants().get_ftp_path()
        self.ftp_info = SecretConstants().get_ftp_dict()
        self.all_videos = PersistVideoInformation().get_video_information()
        self.videos_to_be_uploaded = set()
        self.get_files_to_upload()
        self.all_files_dict = {}

    def get_files_to_upload(self):
        for video_id, status in self.all_videos.items():
            if status == state.DOWNLOADED_NOT_UPLOADED:
                self.videos_to_be_uploaded.add(video_id)
                self._logger.debug(f"Found video {video_id} "
                                   f"to be uploaded to FTP.")

    def match_ids_to_files(self):
        all_files = os.listdir('downloads/')
        for file in all_files:
            if file != ".gitkeep":
                file_split = file.split("-")
                video_id_from_file = file_split[1]
                self.all_files_dict.update({video_id_from_file: file})

    def upload(self):
        self.match_ids_to_files()
