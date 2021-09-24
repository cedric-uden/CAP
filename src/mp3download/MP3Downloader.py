import src.logs.Logging as log
from src.utils.PersistVideoInformation import PersistVideoInformation
from src.business.YouTubeVideoStates import YouTubeVideoStates as state
from src.constants.Constants import SettingConstants

import subprocess


class MP3Downloader:
    _logger = log.get_logger(__name__)

    def __init__(self):
        self.all_video_information = PersistVideoInformation().get_video_information()
        self.videos_to_be_uploaded = set()
        self.settings = SettingConstants()
        self.check_videos_to_be_uploaded()

    def check_videos_to_be_uploaded(self):
        for video, status in self.all_video_information.items():
            if status == state.TO_BE_UPLOADED:
                self.videos_to_be_uploaded.add(video)
        self._logger.debug(f"Podcasts want to be downloaded as MP3:"
                           f"{str(self.videos_to_be_uploaded)}")

    def download(self):
        for video_id in self.videos_to_be_uploaded:
            cmd = self.build_youtubedl_command(video_id)
            cmd_output = self.run_cmd(cmd)
            self.verify_command_output(cmd_output)

    def build_youtubedl_command(self, video_id):
        return f"{self.settings.get_youtubedl_path()} --extract-audio " \
               f"--audio-format mp3 {video_id}"

    def run_cmd(self, run_this_cmd):
        self._logger.info(f"Running youtube-dl with command: {run_this_cmd}")
        out = subprocess.run(run_this_cmd.split(" "), capture_output=True)
        return out.stdout.decode()

    def verify_command_output(self, cmd_output):
        self._logger.info(cmd_output)
