import src.logs.Logging as log
import os


class FilenameSanitizer:
    _logger = log.get_logger(__name__)

    def clean_filename(self, filepath):
        new_filepath = self.replace_whitespace(filepath)
        new_filepath = self.replace_pipe(new_filepath)
        if filepath != new_filepath:
            os.rename(filepath, new_filepath)
            self._logger.debug(f"Renamed {filepath} to {new_filepath}")

    def replace_pipe(self, filepath):
        while "|" in filepath:
            filepath = filepath.replace("|", "-")
        return filepath

    def replace_whitespace(self, filepath):
        while " " in filepath:
            filepath = filepath.replace(" ", "_")
        return filepath
