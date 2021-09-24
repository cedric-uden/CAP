import src.logs.Logging as log
from src.constants.Constants import SecretConstants, SettingConstants

import ftplib


class FTPUploader:
    _logger = log.get_logger(__name__)

    def __init__(self):
        self.ftp_path = SettingConstants().get_ftp_path()
        self.ftp_info = SecretConstants().get_ftp_dict()
