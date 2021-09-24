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
            if status == state.TO_BE_DOWNLOADED:
                self.videos_to_be_uploaded.add(video)
        self._logger.debug(f"Podcasts want to be downloaded as MP3:"
                           f"{str(self.videos_to_be_uploaded)}")

        if len(self.videos_to_be_uploaded) == 0:
            self._logger.info("No videos to be downloaded from YouTube found.")

    def download(self):
        for video_id in self.videos_to_be_uploaded:
            cmd = self.build_youtubedl_command(video_id)
            cmd_output = self.run_cmd(cmd)
            if self.check_if_successfully_downloaded(cmd_output):
                self.update_state(video_id, state.DOWNLOADED_NOT_UPLOADED)

    def build_youtubedl_command(self, video_id):
        return f"{self.settings.get_youtubedl_path()} " \
               f"--extract-audio " \
               f"--audio-format mp3 " \
               f"--audio-quality 0 " \
               f"-o downloads/%(upload_date)s-%(id)s-%(title)s.%(ext)s " \
               f"https://www.youtube.com/watch?v={video_id}"

    def run_cmd(self, run_this_cmd):
        self._logger.info(f"Running youtube-dl with command: {run_this_cmd}")
        out = subprocess.run(run_this_cmd.split(" "), capture_output=True)
        return out.stdout.decode()

    def check_if_successfully_downloaded(self, cmd_output):
        cmd_output_lines = cmd_output.split("\n")
        downloaded_successfully = False

        for line in cmd_output_lines:
            if "[download] 100%" in line:
                downloaded_successfully = True

        if downloaded_successfully:
            self._logger.debug("Successfully downloaded MP3.")
        else:
            self._logger.error(f"Could not download MP3. `youtube-dl` "
                               f"output: {cmd_output}")

        return downloaded_successfully

    def update_state(self, key, value):
        self._logger.debug(f"Going to update state for {key}")
        PersistVideoInformation().update_video_information(key, value)
