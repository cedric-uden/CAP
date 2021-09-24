import src.logs.Logging as log
from src.constants.Constants import SecretConstants, SettingConstants
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.utils.FilenameSanitizer import FilenameSanitizer
from src.business.YouTubeVideoStates import YouTubeVideoStates as state

import ftplib
import os

DOWNLOAD_FOLDER = "downloads"

class FTPUploader:
    _logger = log.get_logger(__name__)

    def __init__(self):
        self.ftp_path = SettingConstants().get_ftp_path()
        self.ftp_info = SecretConstants().get_ftp_dict()
        self.all_videos = PersistVideoInformation().get_video_information()
        self.videos_to_be_uploaded = set()
        self.all_files_dict = {}

        self.get_files_to_upload()

    def get_files_to_upload(self):
        for video_id, status in self.all_videos.items():
            if status == state.DOWNLOADED_NOT_UPLOADED:
                self.videos_to_be_uploaded.add(video_id)
                self._logger.debug(f"Found video {video_id} "
                                   f"to be uploaded to FTP.")

    def match_ids_to_files(self):
        all_files = os.listdir(DOWNLOAD_FOLDER)
        for file in all_files:
            if file != ".gitkeep":
                file_split = file.split("-")
                video_id_from_file = file_split[1]
                self.all_files_dict.update({video_id_from_file: file})

    def upload(self):
        self.match_ids_to_files()
        self.upload_files_in_set()

    def upload_files_in_set(self):
        for video_id in self.videos_to_be_uploaded:
            self.upload_this_file(video_id)

    def upload_this_file(self, video_id):
        server = self.ftp_info['server']
        port = self.ftp_info['port']
        user = self.ftp_info['user']
        pw = self.ftp_info['password']

        self._logger.debug(f"Attempting to upload {video_id} to FTP")
        session = ftplib.FTP()
        session.connect(server, port)
        session.login(user, pw)

        local_filename = self.all_files_dict.get(video_id)
        local_filepath = f"{DOWNLOAD_FOLDER}/{local_filename}"
        file = open(local_filepath, 'rb')
        filepath_on_ftp = f"{self.ftp_path}/{local_filename}"
        session.storbinary(f"STOR {filepath_on_ftp}", file)
        file.close()
        session.quit()
        self._logger.info(f"Uploaded {video_id} to FTP")

