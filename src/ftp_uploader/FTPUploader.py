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
        self.all_videos = PersistVideoInformation().get_video_state()
        self.videos_to_be_uploaded = set()
        self.all_files_dict = {}

        self.get_youtube_ids_to_upload()

    def get_youtube_ids_to_upload(self):
        for video_id, status in self.all_videos.items():
            if status == state.DOWNLOADED_NOT_UPLOADED:
                self.videos_to_be_uploaded.add(video_id)
                self._logger.debug(f"Found video {video_id} "
                                   f"to be uploaded to FTP.")

        if len(self.videos_to_be_uploaded) == 0:
            self._logger.info("No podcasts to be uploaded to FTP found.")

    def upload(self):
        self.upload_files_in_set()

    def upload_files_in_set(self):
        for video_id in self.videos_to_be_uploaded:
            self.upload_this_file(video_id)
            self.update_state(video_id, state.UPLOADED)

    def open_and_return_FTP_session(self):
        server = self.ftp_info['server']
        port = self.ftp_info['port']
        user = self.ftp_info['user']
        pw = self.ftp_info['password']

        self._logger.debug(f"Connecting to FTP Server {server} at port {port} with user {user}.")
        session = ftplib.FTP()
        session.connect(server, port)
        session.login(user, pw)
        return session

    def upload_this_file(self, video_id):

        session = self.open_and_return_FTP_session()

        self._logger.debug(f"Attempting to upload {video_id} to FTP")

        local_filename = self.all_files_dict.get(video_id)
        local_filepath = f"{DOWNLOAD_FOLDER}/{local_filename}"
        file = open(local_filepath, 'rb')
        filepath_on_ftp = f"{self.ftp_path}/{local_filename}"
        session.storbinary(f"STOR {filepath_on_ftp}", file)
        file.close()
        session.quit()
        self._logger.info(f"Uploaded {video_id} to FTP")

    def update_state(self, key, value):
        self._logger.debug(f"Going to update state for {key}")
        PersistVideoInformation().update_video_state(key, value)

